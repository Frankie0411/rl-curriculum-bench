# File: environments/pistonball.py

from typing import Dict, Any, Tuple
import numpy as np
from pettingzoo.butterfly import pistonball_v6
from .base import BaseEnvironmentWrapper
from ..metrics.graph_metrics import GraphMetrics


class PistonballWrapper(BaseEnvironmentWrapper):
    """Wrapper for PettingZoo Pistonball environment."""

    DIFFICULTY_CONFIGS = {
        'easy': {'n_pistons': 10, 'time_penalty': -0.1, 'continuous': True, 'max_cycles': 125},
        'medium': {'n_pistons': 15, 'time_penalty': -0.5, 'continuous': True, 'max_cycles': 125},
        'hard': {'n_pistons': 20, 'time_penalty': -1.0, 'continuous': True, 'max_cycles': 125}
    }

    def __init__(self, difficulty: str = "medium", **kwargs):
        super().__init__("pistonball", difficulty, **kwargs)

        config = self.DIFFICULTY_CONFIGS.get(
            difficulty, self.DIFFICULTY_CONFIGS['medium'])
        config.update(kwargs)

        self._env = pistonball_v6.parallel_env(render_mode=None, **config)
        self.n_pistons = config['n_pistons']
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
        """Compute complexity metrics for Pistonball environment."""
        edges = [(i, i+1) for i in range(self.n_pistons - 1)]

        metrics = {
            'num_agents': self.n_pistons,
            'graph_density': GraphMetrics.compute_density(edges, self.n_pistons),
            'coordination_chain_length': self.n_pistons
        }

        return metrics
