import setuptools
from pathlib import Path

readme_path = Path(__file__).with_name("README.md")
with open(readme_path, encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="algorithm-visualizer",
    version="0.1.0",
    license="MIT",

    author="Example Author",
    author_email="author@example.com",

    description="A visualization library for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    keywords="algorithm data-structure visualization animation",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Visualization"
    ],

    url="https://algorithm-visualizer.org",
    project_urls={
        "Documentation": "https://github.com/algorithm-visualizer/algorithm-visualizer/wiki",
        "Issue Tracker": "https://github.com/algorithm-visualizer/tracers.py/issues",
        "Source": "https://github.com/algorithm-visualizer/tracers.py"
    },

    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    extras_require={
        "requests": ["requests >= 2.22.0"]
    }
)
