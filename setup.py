from setuptools import setup, find_packages

setup(
    name="data_pipeline",
    version="1.0.0",
    description="Databricks Asset Bundle - Medallion Architecture Data Pipeline",
    author="Your Organization",
    author_email="your.email@company.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "delta-spark>=2.4.0",
        "pandas>=2.0.0",
        "numpy>=1.24.0",
    ],
    entry_points={
        "console_scripts": [
            "bronze=bronze:main",
            "silver=silver:main",
            "gold=gold:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
