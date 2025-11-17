# File: curriculum/base_curriculum.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class BaseCurriculum(ABC):
    """Abstract base class for curriculum learning strategies."""

    def __init__(self, env_names: List[str], **kwargs):
        """
        Initialize curriculum.

        Args:
            env_names: List of environment names in the curriculum
            **kwargs: Additional curriculum-specific parameters
        """
        self.env_names = env_names
        self.current_index = 0
        self.config = kwargs
        self.history: List[Dict[str, Any]] = []

    @abstractmethod
    def get_next_env(self) -> Optional[str]:
        """
        Get the next environment in the curriculum.

        Returns:
            Environment name, or None if curriculum is complete
        """
        pass

    @abstractmethod
    def update(self, performance: Dict[str, float]) -> bool:
        """
        Update curriculum based on performance metrics.

        Args:
            performance: Dictionary with performance metrics (e.g., success_rate)

        Returns:
            True if curriculum advanced to next environment, False otherwise
        """
        pass

    def reset(self):
        """Reset curriculum to beginning."""
        self.current_index = 0
        self.history = []

    def is_complete(self) -> bool:
        """Check if curriculum has been completed."""
        return self.current_index >= len(self.env_names)
