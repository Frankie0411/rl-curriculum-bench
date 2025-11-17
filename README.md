# RL Curriculum Bench

A benchmark suite for curriculum learning in multi-agent reinforcement learning (MARL). This library provides standardized environments, complexity metrics, and curriculum strategies to facilitate reproducible curriculum learning research.

## Features

- **Environment Wrappers**: Unified API for 3 PettingZoo environments (Pursuit, Cooperative Pong, Pistonball)
- **Complexity Metrics**: Graph-based and task-based metrics to measure environment difficulty
- **Curriculum Strategies**: Manual, performance-based, and complexity-based curriculum learning
- **Evaluation Framework**: Tools for comparing curriculum learning approaches
- **GPU Support**: Compatible with Stable-Baselines3 for efficient training

## Installation
```bash
pip install rl-curriculum-bench
```

For RL training capabilities:
```bash
pip install rl-curriculum-bench[rl]
```

## Quick Start
```python
from rl_curriculum_bench.environments import make_env
from rl_curriculum_bench.metrics import compute_complexity
from rl_curriculum_bench.curriculum import ComplexityBasedCurriculum

# Create an environment
env = make_env('pursuit', difficulty='medium')

# Compute complexity metrics
metrics = compute_complexity('pursuit', difficulty='medium')
print(metrics)

# Create a curriculum
env_complexities = {
    'cooperative_pong': 1.5,
    'pursuit': 6.5,
    'pistonball': 7.5
}
curriculum = ComplexityBasedCurriculum(env_complexities, ascending=True)

# Get next environment in curriculum
next_env = curriculum.get_next_env()
```

## Available Environments

- `pursuit`: Multi-agent pursuit-evasion task
- `cooperative_pong`: Two-player cooperative Pong
- `pistonball`: Cooperative ball manipulation with pistons

Each environment supports three difficulty levels: `easy`, `medium`, `hard`

## Curriculum Strategies

### Manual Curriculum
Fixed sequence of environments:
```python
from rl_curriculum_bench.curriculum import ManualCurriculum

curriculum = ManualCurriculum(['env1', 'env2', 'env3'])
```

### Performance-Based Curriculum
Progress when threshold is met:
```python
from rl_curriculum_bench.curriculum import PerformanceBasedCurriculum

curriculum = PerformanceBasedCurriculum(
    ['env1', 'env2', 'env3'],
    threshold=0.75
)
```

### Complexity-Based Curriculum
Automatically orders by complexity:
```python
from rl_curriculum_bench.curriculum import ComplexityBasedCurriculum

curriculum = ComplexityBasedCurriculum(env_complexities, ascending=True)
```

## Project Structure
```
rl_curriculum_bench/
├── environments/     # Environment wrappers
├── metrics/          # Complexity metrics
├── curriculum/       # Curriculum strategies
├── evaluation/       # Evaluation tools
└── utils/           # Utilities (config, seeds)
```

## Requirements

- Python ≥3.8
- NumPy ≥1.20.0
- PettingZoo ≥1.24.0
- Gymnasium ≥0.26.0
- NetworkX ≥2.6.0
- PyYAML ≥5.4.0

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
