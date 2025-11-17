# File: evaluation/evaluator.py

from typing import Dict, List, Any, Optional, Callable
import numpy as np
from pathlib import Path
import json


class Evaluator:
    """Evaluate curriculum learning experiments."""

    def __init__(self, output_dir: Optional[Path] = None):
        """
        Initialize evaluator.

        Args:
            output_dir: Directory to save results (default: current directory)
        """
        self.output_dir = output_dir or Path.cwd()
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results: List[Dict[str, Any]] = []

    def evaluate_curriculum(
        self,
        curriculum_name: str,
        train_function: Callable,
        num_trials: int = 5,
        seed_start: int = 0
    ) -> Dict[str, Any]:
        """
        Evaluate a curriculum strategy across multiple trials.

        Args:
            curriculum_name: Name of the curriculum strategy
            train_function: Function that trains and returns metrics
            num_trials: Number of independent trials
            seed_start: Starting seed value

        Returns:
            Aggregated results across trials
        """
        trial_results = []

        for trial in range(num_trials):
            seed = seed_start + trial
            result = train_function(seed=seed)
            result['trial'] = trial
            result['seed'] = seed
            trial_results.append(result)

        aggregated = self._aggregate_results(trial_results)
        aggregated['curriculum'] = curriculum_name
        aggregated['num_trials'] = num_trials

        self.results.append(aggregated)
        return aggregated

    def _aggregate_results(self, trial_results: List[Dict]) -> Dict[str, Any]:
        """Aggregate metrics across trials."""
        if not trial_results:
            return {}

        metric_keys = [k for k in trial_results[0].keys() if k not in [
            'trial', 'seed']]
        aggregated = {}

        for key in metric_keys:
            values = [r[key] for r in trial_results if key in r]
            if values and isinstance(values[0], (int, float)):
                aggregated[f'{key}_mean'] = float(np.mean(values))
                aggregated[f'{key}_std'] = float(np.std(values))
                aggregated[f'{key}_min'] = float(np.min(values))
                aggregated[f'{key}_max'] = float(np.max(values))

        return aggregated

    def save_results(self, filename: str = 'results.json'):
        """Save evaluation results to JSON file."""
        output_path = self.output_dir / filename
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        return output_path
