from setuptools import setup

with open("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


setup (
    name="src",
    version="0.0.1",
    author="rahuls",
    description="Package for dvc ml demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rahul-Shedge/dvc_ml_demo",
    author_email="rahulshedge555@outlook.com",    
    packages=["src"],
    install_requires=[
        "dvc",
        "pandas",
        "scikit-learn"
    ],
    python_requires=">=3.9" )


