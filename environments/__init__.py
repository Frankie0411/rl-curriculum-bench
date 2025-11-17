# File: environments/__init__.py

from typing import Dict, Type, Optional
from .pursuit import PursuitWrapper
from .cooperative_pong import CooperativePongWrapper
from .pistonball import PistonballWrapper


ENVIRONMENT_REGISTRY: Dict[str, Type] = {
    'pursuit': PursuitWrapper,
    'cooperative_pong': CooperativePongWrapper,
    'pistonball': PistonballWrapper
}


def make_env(env_name: str, difficulty: str = "medium", **kwargs):
    """
    Create an environment by name.

    Args:
        env_name: Name of the environment
        difficulty: Difficulty level (easy, medium, hard)
        **kwargs: Additional environment-specific parameters

    Returns:
        Environment wrapper instance
    """
    if env_name not in ENVIRONMENT_REGISTRY:
        available = list(ENVIRONMENT_REGISTRY.keys())
        raise ValueError(
            f"Environment '{env_name}' not found. Available: {available}")

    env_class = ENVIRONMENT_REGISTRY[env_name]
    return env_class(difficulty=difficulty, **kwargs)


def list_environments():
    """List all available environments."""
    return list(ENVIRONMENT_REGISTRY.keys())
