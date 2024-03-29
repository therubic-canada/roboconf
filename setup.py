from setuptools import find_packages, setup

package_name = 'roboconf'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools', 'pyyaml'],
    zip_safe=True,
    maintainer='Auguste Lalande',
    maintainer_email='alal@therubic.com',
    description='Config loading utility',
    license='TODO: License declaration',
)
