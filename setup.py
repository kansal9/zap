# -*- coding: utf-8 -*-

import os
import subprocess
from setuptools import setup, find_packages

# Read version.py
__version__ = None
__description__ = None
with open('zap2/version.py') as f:
    exec(f.read())

# If the version is not stable, we can add a git hash to the __version__
if '.dev' in __version__:
    # Find hash for __githash__ and dev number for __version__ (can't use hash
    # as per PEP440)
    command_hash = 'git rev-list --max-count=1 --abbrev-commit HEAD'
    command_number = 'git rev-list --count HEAD'

    try:
        commit_hash = subprocess.check_output(command_hash, shell=True)\
            .decode('ascii').strip()
        commit_number = subprocess.check_output(command_number, shell=True)\
            .decode('ascii').strip()
    except Exception:
        pass
    else:
        # We write the git hash and value so that they gets frozen if installed
        with open(os.path.join('zap2', '_githash.py'), 'w') as f:
            f.write("__githash__ = \"{}\"\n".format(commit_hash))
            f.write("__dev_value__ = \"{}\"\n".format(commit_number))

        # We modify __version__ here too for commands such as egg_info
        __version__ += commit_number


setup(
    name='zap2',
    version=__version__,
    description=__description__,
    author='Simon Conseil',
    author_email='simon.conseil@univ-lyon1.fr',
    url='https://git-cral.univ-lyon1.fr/MUSE/zap2',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['numpy', 'scipy', 'astropy', 'scikit-learn'],
    extras_require={'plot': ['matplotlib']},
    entry_points={
        'console_scripts': ['zap2 = zap2.__main__:main']
    },
)
