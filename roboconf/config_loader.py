from pathlib import Path
import yaml


def load_nearest_conf(path, verbose=False):
    print(Path(path))
    print(Path(path).resolve())
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

        current_path = current_path.parent

    if conf_path is None:
        raise Exception('No conf file found.')

    if verbose:
        print(conf_path)

    with open(conf_path, mode='rb') as f:
        return yaml.safe_load(f)
