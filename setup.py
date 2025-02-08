from setuptools import setup, find_packages

setup(
    name="iforest",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "pandas",
        "numpy",
        "scikit-learn",
        "uvicorn",
        "python-dotenv"
    ]
)
