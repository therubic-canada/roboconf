# Roboconf
This is a configuration file loading utility.

This package will allow loading the nearest config file based a specific pattern, either `<name>.roboconf.yml` or `config/<name>.roboconf.yml`. The loader will look through the parents of the current file until it either matches the pattern and loads the file or reaches the root directory and raises an exception.

## Installation
1. `git clone git@github.com:therubic-canada/roboconf.git`
2. `pip install roboconf`

## Usage
```
import roboconf

conf = roboconf.load_nearest_conf(__path__)
```
