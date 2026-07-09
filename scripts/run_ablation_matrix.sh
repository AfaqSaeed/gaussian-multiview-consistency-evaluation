#!/usr/bin/env bash
set -euo pipefail

# Placeholder script for GaussianGPT or another generated-3D model.
# Fill in REPO_ROOT and generation commands once the upstream model is installed.

ABLATIONS=(
  baseline
  high_temperature
  restricted_top_k
  position_token_noise
  feature_token_noise
  early_attention_off
  late_attention_off
  context_removed
)

for ABLATION in "${ABLATIONS[@]}"; do
  echo "Running ablation: ${ABLATION}"
  # Example future command:
  # python external/gaussiangpt/generate_chunks.py \
  #   --config configs/gaussiangpt_${ABLATION}.yaml \
  #   --output data/generated/${ABLATION}
  echo "TODO: add generation command for ${ABLATION}"
done
