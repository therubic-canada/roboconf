# Roboconf
[![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This is a configuration file loading utility.

This package will allow loading the nearest config file based on a specific pattern, either `<name>.roboconf.yml` or `config/<name>.roboconf.yml`. The loader will look through the parents of the current file until it either matches the pattern and loads the file or reaches the root directory and raises an exception.

## Installation
```
pip install git+https://github.com/therubic-canada/roboconf.git
```

## Usage
```python
import roboconf

conf = roboconf.load_nearest_conf(__file__)
```
