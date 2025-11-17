# File: curriculum/complexity_based.py

from typing import List, Dict, Optional, Callable
from .base_curriculum import BaseCurriculum


class ComplexityBasedCurriculum(BaseCurriculum):
    """Curriculum that orders environments by complexity metrics."""

    def __init__(self, env_complexities: Dict[str, float], ascending: bool = True, **kwargs):
        """
        Initialize complexity-based curriculum.

        Args:
            env_complexities: Dict mapping env names to complexity scores
            ascending: If True, sort easy→hard; if False, sort hard→easy
        """
        sorted_envs = sorted(
            env_complexities.items(),
            key=lambda x: x[1],
            reverse=not ascending
        )
        env_names = [env for env, _ in sorted_envs]

        super().__init__(env_names, **kwargs)
        self.complexities = env_complexities
        self.ascending = ascending

    def get_next_env(self) -> Optional[str]:
        """Return next environment in complexity order."""
        if self.is_complete():
            return None
        return self.env_names[self.current_index]

    def update(self, performance: Dict[str, float]) -> bool:
        """Advance to next environment (automatic progression)."""
        self.history.append({
            'env': self.env_names[self.current_index],
            'complexity': self.complexities[self.env_names[self.current_index]],
            'performance': performance
        })
        self.current_index += 1
        return True
