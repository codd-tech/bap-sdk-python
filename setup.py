from setuptools import setup

setup(
    name='bapsdk',
    packages=['bap'],
    version='0.1.0',
    description='Bot Advertising Platform SDK',
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    extras_require={
        'aiogram2': [
            'aiogram>=2.0.0,<3.0.0',
        ],
    },
)
