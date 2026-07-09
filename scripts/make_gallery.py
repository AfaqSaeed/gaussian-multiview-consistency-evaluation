from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageDraw


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a simple contact-sheet gallery from rendered views.")
    parser.add_argument("--renders", type=Path, default=Path("data/renders"))
    parser.add_argument("--output", type=Path, default=Path("results/gallery.png"))
    parser.add_argument("--thumb-size", type=int, default=192)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sample_dirs = sorted([p for p in args.renders.iterdir() if p.is_dir()]) if args.renders.exists() else []
    thumbs = []
    labels = []

    for sample_dir in sample_dirs:
        for view in sorted(sample_dir.glob("*.png"))[:8]:
            img = Image.open(view).convert("RGB").resize((args.thumb_size, args.thumb_size))
            thumbs.append(img)
            labels.append(f"{sample_dir.name}/{view.stem}")

    if not thumbs:
        print("No rendered views found. Add images under data/renders/<sample_id>/*.png")
        return

    cols = 4
    rows = (len(thumbs) + cols - 1) // cols
    label_h = 24
    sheet = Image.new("RGB", (cols * args.thumb_size, rows * (args.thumb_size + label_h)), "white")
    draw = ImageDraw.Draw(sheet)

    for idx, thumb in enumerate(thumbs):
        x = (idx % cols) * args.thumb_size
        y = (idx // cols) * (args.thumb_size + label_h)
        sheet.paste(thumb, (x, y))
        draw.text((x + 4, y + args.thumb_size + 4), labels[idx][:28], fill=(0, 0, 0))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output)
    print(f"Wrote gallery to {args.output}")


if __name__ == "__main__":
    main()
