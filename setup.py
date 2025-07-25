from setuptools import setup

with open("README.md","r",encoding="utf-8") as f:
    long_description= f.read()
    
REPO_NAME = "DVC-NLP"
AUTHOR_USER_NAME = "Utkarsh Shelke"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    description="A NLP DEMO",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/ushel/NLP_dvc.git",
    author_email="utkarsh03@icloud.com",
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.6",
    install_requirements= LIST_OF_REQUIREMENTS
)