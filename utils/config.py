# File: utils/config.py

import yaml
import json
from pathlib import Path
from typing import Dict, Any, Union


class ConfigManager:
    """Manage experiment configurations."""

    @staticmethod
    def load_config(config_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Load configuration from YAML or JSON file.

        Args:
            config_path: Path to config file

        Returns:
            Configuration dictionary
        """
        config_path = Path(config_path)

        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")

        with open(config_path, 'r') as f:
            if config_path.suffix in ['.yaml', '.yml']:
                config = yaml.safe_load(f)
            elif config_path.suffix == '.json':
                config = json.load(f)
            else:
                raise ValueError(
                    f"Unsupported config format: {config_path.suffix}")

        return config

    @staticmethod
    def save_config(config: Dict[str, Any], output_path: Union[str, Path]):
        """
        Save configuration to file.

        Args:
            config: Configuration dictionary
            output_path: Path to save config
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w') as f:
            if output_path.suffix in ['.yaml', '.yml']:
                yaml.dump(config, f, default_flow_style=False)
            elif output_path.suffix == '.json':
                json.dump(config, f, indent=2)
            else:
                raise ValueError(
                    f"Unsupported config format: {output_path.suffix}")
