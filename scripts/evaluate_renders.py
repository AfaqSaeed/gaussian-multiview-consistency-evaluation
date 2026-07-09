from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from gmce.io import collect_rendered_samples
from gmce.metrics import pairwise_feature_consistency, pairwise_ssim_consistency, placeholder_prompt_alignment


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate rendered multi-view samples.")
    parser.add_argument("--renders", type=Path, default=Path("data/renders"), help="Directory with sample render folders.")
    parser.add_argument("--prompts", type=Path, default=Path("configs/prompts.json"), help="JSON mapping sample IDs to prompts.")
    parser.add_argument("--output", type=Path, default=Path("results/metrics.csv"), help="Output CSV path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    prompts = json.loads(args.prompts.read_text(encoding="utf-8")) if args.prompts.exists() else {}
    samples = collect_rendered_samples(args.renders, prompts)

    rows = []
    for sample in samples:
        row = {
            "sample_id": sample.sample_id,
            "prompt": sample.prompt or "",
            "num_views": len(sample.view_paths),
        }
        row.update(pairwise_feature_consistency(sample.view_paths))
        row.update(pairwise_ssim_consistency(sample.view_paths))
        row.update(placeholder_prompt_alignment(sample.prompt, sample.view_paths))
        rows.append(row)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(rows).to_csv(args.output, index=False)
    print(f"Wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
