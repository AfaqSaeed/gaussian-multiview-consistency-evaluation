from __future__ import annotations

from itertools import combinations
from pathlib import Path
from typing import Dict, Iterable, List

import cv2
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim


def load_image(path: str | Path, size: tuple[int, int] = (256, 256)) -> np.ndarray:
    """Load image as RGB float array in [0, 1]."""
    image = Image.open(path).convert("RGB").resize(size)
    return np.asarray(image).astype(np.float32) / 255.0


def color_histogram(image: np.ndarray, bins: int = 16) -> np.ndarray:
    """Simple color histogram feature used as a lightweight placeholder.

    Replace this with DINOv2/CLIP/SigLIP embeddings for the final experiment.
    """
    hist_features = []
    for channel in range(3):
        hist, _ = np.histogram(image[..., channel], bins=bins, range=(0.0, 1.0), density=True)
        hist_features.append(hist)
    feature = np.concatenate(hist_features)
    norm = np.linalg.norm(feature) + 1e-8
    return feature / norm


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / ((np.linalg.norm(a) * np.linalg.norm(b)) + 1e-8))


def pairwise_feature_consistency(view_paths: Iterable[str | Path]) -> Dict[str, float]:
    """Compute cross-view consistency using simple histogram features.

    This is intentionally lightweight and should later be replaced or complemented
    with frozen vision-model features such as DINOv2, CLIP, or SigLIP.
    """
    paths = list(view_paths)
    if len(paths) < 2:
        return {"feature_consistency_mean": np.nan, "feature_consistency_min": np.nan}

    features = [color_histogram(load_image(path)) for path in paths]
    sims = [cosine_similarity(features[i], features[j]) for i, j in combinations(range(len(features)), 2)]
    return {
        "feature_consistency_mean": float(np.mean(sims)),
        "feature_consistency_min": float(np.min(sims)),
    }


def pairwise_ssim_consistency(view_paths: Iterable[str | Path]) -> Dict[str, float]:
    """Compute rough image-level cross-view similarity using SSIM.

    Note: SSIM across different viewpoints is not a final metric. It is included
    only as a sanity placeholder and diagnostic baseline.
    """
    paths = list(view_paths)
    if len(paths) < 2:
        return {"ssim_consistency_mean": np.nan, "ssim_consistency_min": np.nan}

    gray_images = []
    for path in paths:
        image = load_image(path)
        gray = cv2.cvtColor((image * 255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
        gray_images.append(gray)

    scores = [ssim(gray_images[i], gray_images[j]) for i, j in combinations(range(len(gray_images)), 2)]
    return {
        "ssim_consistency_mean": float(np.mean(scores)),
        "ssim_consistency_min": float(np.min(scores)),
    }


def placeholder_prompt_alignment(prompt: str | None, view_paths: Iterable[str | Path]) -> Dict[str, float]:
    """Placeholder for prompt-alignment scoring.

    Final version should use CLIP/SigLIP or a captioner+VLM judge.
    For now, this returns NaN to avoid pretending we measured semantics.
    """
    return {"prompt_alignment_placeholder": np.nan if prompt else np.nan}
