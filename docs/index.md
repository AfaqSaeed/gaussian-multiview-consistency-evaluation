# Prompt-Grounded Multi-View Consistency for Generated 3D Gaussians

This page is a public research showcase for evaluating whether generated 3D Gaussian objects/scenes remain semantically and geometrically coherent across rendered views.

## Motivation

Standard metrics such as FID, KID, COV, and MMD are useful but incomplete. They evaluate distribution-level visual quality, geometric diversity, or rough geometric fidelity. They do not directly test whether a generated sample preserves the same prompt-grounded entities, attributes, parts, and spatial relations across views.

## Planned experiment

1. Generate or collect 3D Gaussian samples.
2. Render each sample from multiple viewpoints.
3. Compare standard metrics against prompt-grounded multi-view consistency metrics.
4. Run controlled ablations in the generation process.
5. Identify failures that standard metrics under-report.

## Planned failure taxonomy

- Identity drift
- Attribute drift
- Missing backside
- Janus artifact
- Floating artifacts
- Broken topology
- Relation mismatch
- Context mismatch

## Status

Scaffold created. Results will be added after baseline generation and ablation experiments.
