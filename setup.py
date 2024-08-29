from setuptools import setup

from src.constants import PrePyAbout

setup(
    name=PrePyAbout.NAME,
    version=PrePyAbout.VERSION,
    description=PrePyAbout.DESCRIPTION,
    author=PrePyAbout.AUTHOR,
    author_email=PrePyAbout.AUTHOR_EMAIL,
    package_dir={"src": "src"},
    include_package_data=True,
    install_requires=[
        'PyYAML >= 6.0.2',
    ],
    entry_points={
        'console_scripts': [
            'pre-py = src.entrypoints:prepy'
        ]
    }
)
