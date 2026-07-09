# Prompt-Grounded Multi-View Consistency for Generated 3D Gaussians

This repository is a public, NDA-safe research scaffold for evaluating whether generated 3D Gaussian objects/scenes remain semantically and geometrically coherent across rendered viewpoints.

The project is motivated by a limitation of common generative-3D evaluation metrics such as FID, KID, COV, and MMD: these scores are useful for distribution-level appearance and geometry evaluation, but they do not directly measure whether prompt-specified entities, attributes, parts, and spatial relations remain stable across views.

## Core question

Can we detect generation failures that are not well captured by FID/KID/COV/MMD, such as:

- object identity drift across views,
- missing or inconsistent backsides,
- prompt-attribute mismatch,
- broken part structure,
- floating or disconnected Gaussians,
- inconsistent object relations in scene completions,
- plausible-looking but semantically wrong generations?

## Planned contribution

This repository will contain:

1. A small evaluation pipeline for rendered multi-view images from generated 3D Gaussians.
2. A failure taxonomy for prompt-grounded multi-view generation errors.
3. Ablation scripts for comparing baseline generation against sampling, token, and layer-level interventions.
4. Metrics that complement FID/KID/COV/MMD with semantic and consistency-focused checks.
5. A public results gallery that can be linked from a personal website or PhD application.

## NDA-safe positioning

This repository does not contain proprietary data, internal results, or confidential company material. It is designed as a public analogue of a broader research interest in evaluating the reliability of generated multi-view visual data.

## Repository structure

```text
configs/             Experiment and evaluation configs
data/                Placeholder folders for public/generated data
src/gmce/            Python package for metrics and utility code
scripts/             CLI scripts for evaluation and ablation studies
results/             CSV/JSON outputs and generated reports
docs/                GitHub Pages project showcase
assets/              Diagrams and static figures
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

Run a placeholder evaluation over rendered views:

```bash
python scripts/evaluate_renders.py \
  --renders data/renders \
  --prompts configs/prompts.json \
  --output results/example_metrics.csv
```

## Planned metrics

| Metric group | Purpose |
|---|---|
| Prompt alignment | Check whether each rendered view matches the text/context prompt. |
| Cross-view semantic consistency | Check whether object identity, attributes, and parts remain stable across views. |
| Geometry sanity | Flag disconnected components, floating artifacts, depth/normal inconsistencies, and invalid structure. |
| Relation consistency | Check whether multi-object spatial relations remain valid across views. |
| Failure taxonomy | Assign interpretable labels such as identity drift, missing backside, Janus artifact, or relation mismatch. |

## Planned ablations

- Sampling-level: temperature, top-k, top-p, seed sensitivity.
- Token-level: perturb position tokens vs feature tokens.
- Context-level: completion/outpainting with partial context removed.
- Transformer-level: attention/MLP/block ablations in early, middle, and late layers.

## Research claim

FID, KID, COV, and MMD are necessary but not sufficient. This project evaluates complementary failure modes: prompt-grounded semantic correctness, multi-view identity stability, part coherence, physical plausibility, and relation preservation.

