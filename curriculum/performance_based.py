# File: curriculum/performance_based.py

from typing import List, Dict, Optional
from .base_curriculum import BaseCurriculum


class PerformanceBasedCurriculum(BaseCurriculum):
    """Curriculum that advances based on performance threshold."""

    def __init__(self, env_names: List[str], threshold: float = 0.7, **kwargs):
        """
        Initialize performance-based curriculum.

        Args:
            env_names: List of environment names
            threshold: Success rate threshold to advance (default 0.7)
        """
        super().__init__(env_names, **kwargs)
        self.threshold = threshold
        self.current_performance = 0.0

    def get_next_env(self) -> Optional[str]:
        """Return current environment (stays on same env until threshold met)."""
        if self.is_complete():
            return None
        return self.env_names[self.current_index]

    def update(self, performance: Dict[str, float]) -> bool:
        """
        Advance only if performance exceeds threshold.

        Args:
            performance: Must contain 'success_rate' key

        Returns:
            True if advanced to next env, False if staying on current
        """
        success_rate = performance.get('success_rate', 0.0)
        self.current_performance = success_rate

        self.history.append({
            'env': self.env_names[self.current_index],
            'performance': performance,
            'advanced': success_rate >= self.threshold
        })

        if success_rate >= self.threshold:
            self.current_index += 1
            return True

        return False
