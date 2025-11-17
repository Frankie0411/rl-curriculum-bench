# File: curriculum/manual.py

from typing import List, Dict, Optional
from .base_curriculum import BaseCurriculum


class ManualCurriculum(BaseCurriculum):
    """Fixed sequence curriculum - environments in specified order."""

    def get_next_env(self) -> Optional[str]:
        """Return next environment in fixed sequence."""
        if self.is_complete():
            return None
        return self.env_names[self.current_index]

    def update(self, performance: Dict[str, float]) -> bool:
        """Advance to next environment (ignores performance)."""
        self.history.append({
            'env': self.env_names[self.current_index],
            'performance': performance
        })
        self.current_index += 1
        return True
