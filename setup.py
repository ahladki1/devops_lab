from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = main.snapshot:main",
        ],
    },
    install_requires=[
        'psutil',
        'argparse',

    ],
    version="0.1",
    author="Aliaksei Hladki1",
    author_email="captain_jack@gmail.com",
    description="The snapshot is saved to the file(Homework3)",
)
