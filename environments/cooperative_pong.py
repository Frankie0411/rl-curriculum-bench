# File: environments/cooperative_pong.py

from typing import Dict, Any, Tuple
import numpy as np
from pettingzoo.butterfly import cooperative_pong_v5
from .base import BaseEnvironmentWrapper
from ..metrics.graph_metrics import GraphMetrics


class CooperativePongWrapper(BaseEnvironmentWrapper):
    """Wrapper for PettingZoo Cooperative Pong environment."""

    DIFFICULTY_CONFIGS = {
        'easy': {'ball_speed': 9, 'left_paddle_speed': 12, 'right_paddle_speed': 12, 'max_cycles': 900},
        'medium': {'ball_speed': 13, 'left_paddle_speed': 12, 'right_paddle_speed': 12, 'max_cycles': 900},
        'hard': {'ball_speed': 18, 'left_paddle_speed': 12, 'right_paddle_speed': 12, 'max_cycles': 900}
    }

    def __init__(self, difficulty: str = "medium", **kwargs):
        super().__init__("cooperative_pong", difficulty, **kwargs)

        config = self.DIFFICULTY_CONFIGS.get(
            difficulty, self.DIFFICULTY_CONFIGS['medium'])
        config.update(kwargs)

        self._env = cooperative_pong_v5.parallel_env(**config)
        self.ball_speed = config['ball_speed']
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
        """Compute complexity metrics for Cooperative Pong environment."""
        num_agents = 2

        edges = [(0, 1)]

        metrics = {
            'num_agents': num_agents,
            'ball_speed': self.ball_speed,
            'graph_density': GraphMetrics.compute_density(edges, num_agents),
            'coordination_required': 1.0
        }

        return metrics
