from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip()
                    and not line.startswith("#")]

setup(
    name="rl-curriculum-bench",
    version="0.1.0",
    author="Frankie",
    author_email="therealbatook@gmail.com",
    description="A benchmark suite for curriculum learning in multi-agent reinforcement learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Frankie0411/rl-curriculum-bench",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest", "black", "flake8"],
        "rl": ["stable-baselines3>=2.0.0", "torch"],
    },
)
