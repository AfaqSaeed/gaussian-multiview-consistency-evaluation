# Project plan

## Phase 1: Public scaffold

- Publish repository with NDA-safe framing.
- Add placeholder metrics and project page.
- Link from personal website showcase page.

## Phase 2: Baseline sample generation

- Use released generated-3D / Gaussian Splatting checkpoints where available.
- Generate a small sample set with fixed seeds.
- Render 4-8 views per sample.

## Phase 3: Standard metric baseline

- Record FID/KID where applicable.
- Record COV/MMD/Chamfer where geometry extraction is available.
- Save rendered-view examples for qualitative inspection.

## Phase 4: Consistency metric

- Add CLIP/SigLIP/DINOv2 image features.
- Add caption-based prompt alignment.
- Add view-to-view caption/entity consistency.
- Add failure taxonomy annotations.

## Phase 5: Ablation study

- Sampling-level ablations: temperature/top-k/top-p.
- Token-level ablations: position vs feature token perturbation.
- Context-level ablations: completion/outpainting with context removed.
- Layer-level ablations: early/mid/late attention or MLP removal.

## Phase 6: Application-ready results

- Build a compact results table.
- Show 3-5 failure case panels.
- Add a short discussion: what standard metrics miss and where the proposed score helps.
