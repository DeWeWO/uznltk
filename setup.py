from setuptools import setup, find_packages

setup(
    name="uznltk",
    version="0.0.11",
    author="Ulugbek Salaev",
    author_email="ulugbek0302@gmail.com",
    description="The Uzbek Natural Language Toolkit (NLTK) is a Python package for natural language processing.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/UlugbekSalaev/uznltk",
    keywords=['nltk', 'morphology', 'uzbek-language', 'pos tagging', 'morphological tagging'],
    project_urls={
        "Bug Tracker": "https://github.com/UlugbekSalaev/uznltk/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests",
        "UzMorphAnalyser",
        "UzSyllable"
    ],
    include_package_data=True,
    license="MIT",
)
