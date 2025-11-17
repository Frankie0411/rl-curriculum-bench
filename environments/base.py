#/ "environments" / "base.py
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, Tuple
import numpy as np


class BaseEnvironmentWrapper(ABC):
    """Abstract base class for environment wrappers."""
    
    def __init__(self, env_name: str, difficulty: str = "medium", **kwargs):
        self.env_name = env_name
        self.difficulty = difficulty
        self.config = kwargs
        self._env = None
        
    @abstractmethod
    def reset(self) -> Any:
        """Reset the environment and return initial observation."""
        pass
    
    @abstractmethod
    def step(self, action: Any) -> Tuple[Any, float, bool, Dict]:
        """Execute one step in the environment."""
        pass
    
    @abstractmethod
    def get_complexity_metrics(self) -> Dict[str, float]:
        """Compute and return complexity metrics for this environment."""
        pass
    
    def close(self):
        if self._env is not None:
            self._env.close()