# File: metrics/composite.py

from typing import Dict, List, Optional
import numpy as np


class CompositeMetric:
    """Compose multiple metrics into a single complexity score."""

    def __init__(self, metric_names: List[str], weights: Optional[List[float]] = None):
        """
        Initialize composite metric.

        Args:
            metric_names: List of metric names to combine
            weights: Optional weights for each metric (defaults to equal weights)
        """
        self.metric_names = metric_names

        if weights is None:
            self.weights = [1.0 / len(metric_names)] * len(metric_names)
        else:
            if len(weights) != len(metric_names):
                raise ValueError(
                    "Number of weights must match number of metrics")
            total = sum(weights)
            self.weights = [w / total for w in weights]

    def compute(self, metrics: Dict[str, float]) -> float:
        """
        Compute weighted combination of metrics.

        Args:
            metrics: Dictionary mapping metric names to values

        Returns:
            Combined complexity score
        """
        score = 0.0
        for name, weight in zip(self.metric_names, self.weights):
            if name not in metrics:
                raise KeyError(
                    f"Metric '{name}' not found in provided metrics")
            score += weight * metrics[name]

        return score
