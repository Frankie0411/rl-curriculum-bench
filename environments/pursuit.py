# File: environments/pursuit.py

from typing import Dict, Any, Tuple
import numpy as np
from pettingzoo.sisl import pursuit_v4
from .base import BaseEnvironmentWrapper
from ..metrics.graph_metrics import GraphMetrics


class PursuitWrapper(BaseEnvironmentWrapper):
    """Wrapper for PettingZoo Pursuit environment."""

    DIFFICULTY_CONFIGS = {
        'easy': {'n_pursuers': 4, 'n_evaders': 2, 'max_cycles': 500},
        'medium': {'n_pursuers': 8, 'n_evaders': 4, 'max_cycles': 500},
        'hard': {'n_pursuers': 8, 'n_evaders': 8, 'max_cycles': 500}
    }

    def __init__(self, difficulty: str = "medium", **kwargs):
        super().__init__("pursuit", difficulty, **kwargs)

        config = self.DIFFICULTY_CONFIGS.get(
            difficulty, self.DIFFICULTY_CONFIGS['medium'])
        config.update(kwargs)

        self._env = pursuit_v4.parallel_env(**config)
        self.n_pursuers = config['n_pursuers']
        self.n_evaders = config['n_evaders']
        self.agents = None

    def reset(self):
        obs, info = self._env.reset()
        self.agents = self._env.agents
        return obs

    def step(self, actions: Dict):
        obs, rewards, terminations, truncations, infos = self._env.step(
            actions)

        done = all(terminations.values()) or all(truncations.values())
        total_reward = sum(rewards.values())

        return obs, total_reward, done, infos

    def get_complexity_metrics(self) -> Dict[str, float]:
        """Compute complexity metrics for Pursuit environment."""
        num_agents = self.n_pursuers + self.n_evaders

        edges = []
        for i in range(self.n_pursuers):
            for j in range(i + 1, self.n_pursuers):
                edges.append((i, j))

        metrics = {
            'num_agents': num_agents,
            'num_pursuers': self.n_pursuers,
            'num_evaders': self.n_evaders,
            'graph_density': GraphMetrics.compute_density(edges, self.n_pursuers),
        }

        return metrics
