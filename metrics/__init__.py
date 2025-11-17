# File: metrics/__init__.py

from typing import Dict, Any
from .graph_metrics import GraphMetrics
from .task_metrics import TaskMetrics
from .composite import CompositeMetric
from ..environments import make_env


def compute_complexity(
    env_name: str,
    difficulty: str = "medium",
    metric_names: list = None,
    **env_kwargs
) -> Dict[str, float]:
    """
    Compute complexity metrics for an environment.

    Args:
        env_name: Name of environment
        difficulty: Difficulty level
        metric_names: Specific metrics to compute (None = all available)
        **env_kwargs: Additional environment parameters

    Returns:
        Dictionary of computed metrics
    """
    env = make_env(env_name, difficulty=difficulty, **env_kwargs)

    try:
        metrics = env.get_complexity_metrics()

        if metric_names is not None:
            metrics = {k: v for k, v in metrics.items() if k in metric_names}

        return metrics
    finally:
        env.close()
