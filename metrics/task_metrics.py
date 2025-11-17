# File: metrics/task_metrics.py

import numpy as np
from typing import Any, Dict


class TaskMetrics:
    """Compute task-based complexity metrics for environments."""

    @staticmethod
    def compute_state_space_size(observation_space: Any) -> float:
        """
        Estimate state space size from observation space.

        Args:
            observation_space: Gym-style observation space

        Returns:
            Log of estimated state space size
        """
        if hasattr(observation_space, 'shape'):
            total_dims = np.prod(observation_space.shape)
            return float(np.log10(total_dims + 1))
        return 0.0

    @staticmethod
    def compute_action_space_complexity(action_space: Any) -> float:
        """
        Compute action space complexity.

        Args:
            action_space: Gym-style action space

        Returns:
            Log of action space size
        """
        if hasattr(action_space, 'n'):
            return float(np.log10(action_space.n))
        elif hasattr(action_space, 'shape'):
            total_dims = np.prod(action_space.shape)
            return float(np.log10(total_dims + 1))
        return 0.0

    @staticmethod
    def compute_reward_sparsity(rewards: np.ndarray) -> float:
        """
        Compute reward sparsity: fraction of zero/near-zero rewards.

        Args:
            rewards: Array of rewards from episodes

        Returns:
            Sparsity value between 0 and 1
        """
        if len(rewards) == 0:
            return 0.0

        near_zero = np.abs(rewards) < 1e-6
        return float(np.mean(near_zero))
