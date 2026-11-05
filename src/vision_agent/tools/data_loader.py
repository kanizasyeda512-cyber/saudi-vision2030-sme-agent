import json
from pathlib import Path
from typing import Dict, Any


def load_dataset(dataset_name: str) -> Dict[str, Any]:
    """Load sample datasets from data/sample/ directory."""
    base_path = Path(__file__).resolve().parents[3] / "data" / "sample"
    file_path = base_path / f"{dataset_name}.json"
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset {dataset_name} not found at {file_path}")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return {"status": "success", "dataset": dataset_name, "data": data}
