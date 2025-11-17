# File: utils/seeds.py

import random
import numpy as np
from typing import Optional


class SeedManager:
    """Manage random seeds for reproducibility."""

    @staticmethod
    def set_global_seed(seed: int):
        """
        Set global random seed for reproducibility.

        Args:
            seed: Random seed value
        """
        random.seed(seed)
        np.random.seed(seed)

        try:
            import torch
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed_all(seed)
        except ImportError:
            pass

    @staticmethod
    def get_random_state() -> dict:
        """
        Get current random state for all RNGs.

        Returns:
            Dictionary containing random states
        """
        state = {
            'python': random.getstate(),
            'numpy': np.random.get_state()
        }

        try:
            import torch
            state['torch'] = torch.get_rng_state()
            if torch.cuda.is_available():
                state['torch_cuda'] = torch.cuda.get_rng_state_all()
        except ImportError:
            pass

        return state

    @staticmethod
    def set_random_state(state: dict):
        """
        Restore random state for all RNGs.

        Args:
            state: Dictionary containing random states
        """
        if 'python' in state:
            random.setstate(state['python'])
        if 'numpy' in state:
            np.random.set_state(state['numpy'])

        try:
            import torch
            if 'torch' in state:
                torch.set_rng_state(state['torch'])
            if 'torch_cuda' in state:
                torch.cuda.set_rng_state_all(state['torch_cuda'])
        except ImportError:
            pass
