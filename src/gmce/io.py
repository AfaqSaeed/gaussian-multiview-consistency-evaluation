from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass(frozen=True)
class RenderedSample:
    """A generated 3D sample represented by multiple rendered views."""

    sample_id: str
    view_paths: List[Path]
    prompt: str | None = None


def collect_rendered_samples(renders_dir: str | Path, prompts: Dict[str, str] | None = None) -> List[RenderedSample]:
    """Collect rendered samples from a directory.

    Expected layout:

    data/renders/
      sample_001/
        front.png
        left.png
        back.png
      sample_002/
        front.png
        left.png

    Args:
        renders_dir: Directory containing one subfolder per sample.
        prompts: Optional mapping from sample_id to prompt.

    Returns:
        List of RenderedSample objects.
    """
    root = Path(renders_dir)
    prompts = prompts or {}
    if not root.exists():
        return []

    samples: List[RenderedSample] = []
    for sample_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        view_paths = sorted(
            [p for p in sample_dir.iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}]
        )
        if view_paths:
            samples.append(RenderedSample(sample_id=sample_dir.name, view_paths=view_paths, prompt=prompts.get(sample_dir.name)))
    return samples
