from setuptools import setup, find_packages

setup(
    name="circuit_prediction",
    version="1.0.0",
    author="Your Name",
    author_email="your@email.com",
    description="A Python project for circuit prediction",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.0.0",
        "keras>=2.0.0",
        "matplotlib>=3.0.0",
        "tqdm>=4.0.0",
        "torchvision>=0.0.0",
        "torch>=0.0.0",
    ],
    entry_points={
        "console_scripts": [
            # You can define command-line scripts here if needed
        ],
    },
)
