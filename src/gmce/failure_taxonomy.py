from __future__ import annotations

FAILURE_LABELS = {
    "identity_drift": "Object/category appears to change across rendered views.",
    "attribute_drift": "Prompt-specified attributes such as color/material/part count change across views.",
    "missing_backside": "Back or occluded side is incomplete, collapsed, or semantically unrelated.",
    "janus_artifact": "Multiple conflicting fronts/faces or duplicated canonical sides appear.",
    "floating_artifacts": "Disconnected Gaussians or geometry float away from the main object/scene.",
    "broken_topology": "Object parts are disconnected, fused incorrectly, or structurally impossible.",
    "relation_mismatch": "Prompt-specified object relations are absent or inconsistent.",
    "context_mismatch": "Completion/outpainting result does not match the provided context.",
}
