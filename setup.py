import os

from setuptools import setup

# What packages are required for this module to be executed?
requires = [
    'click',
]

# Import the README and use it as the long-description.
cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name='fixed-vhd-writer',
        version='0.0.1',
        url='https://github.com/fujiawei-dev/fixed-vhd-writer',
        packages=['fixed_vhd_writer'],
        description='Fixed VHD writer.',
        long_description=long_description,
        long_description_content_type='text/markdown',
        license='MIT',
        author='Rustle Karl',
        author_email='fu.jiawei@outlook.com',
        install_requires=requires,

        entry_points={
            'console_scripts': [
                'vhdwriter=fixed_vhd_writer:fixed_vhd_writer',
            ],
        },

        classifiers=[
            'Intended Audience :: Developers',
            'Environment :: Console',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
)
