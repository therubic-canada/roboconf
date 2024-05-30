"""Utility for loading nearest config file."""

from pathlib import Path

import yaml


def load_nearest_conf(path: str, *, verbose: bool = False) -> dict:
    """Finds and reads the nearest config file.

    Args:
        path (str): Path from which to start searching. Usually "__file__".
        verbose (bool, optional): Whether to print the path to the found
            config file.

    Returns:
        dict: Dictionary loaded from the found config file.

    Raises:
        FileNotFoundError: If no config file is found.
    """
    conf_path = _find_nearest_conf(path)

    if verbose:
        print(conf_path)

    with conf_path.open('rb') as f:
        return yaml.safe_load(f)


def _find_nearest_conf(path: str) -> Path:
    current_path = Path(path).resolve(strict=True)
    if current_path.is_file():
        current_path = current_path.parent

    conf_path = None
    while current_path != current_path.parent:
        if (current_path / 'config').exists():
            for file in (current_path / 'config').iterdir():
                if file.suffixes == ['.roboconf', '.yml']:
                    conf_path = file
                    break

        for file in current_path.iterdir():
            if file.suffixes == ['.roboconf', '.yml']:
                conf_path = file
                break

        for file in current_path.glob('src/*/config/*.roboconf.yml'):
            conf_path = file
            break

        current_path = current_path.parent

    if conf_path is None:
        raise FileNotFoundError('No conf file found.')

    return conf_path
