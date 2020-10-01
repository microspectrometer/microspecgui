"""Project setup for `microspecgui`.

Normal Use
----------
Chromation runs this script to generate a distribution for
publishing on PyPI so that end users install the project:

pip install microspecgui

Developer Use
-------------
Clone the repository from the project homepage on GitHub.
Create a virtual environment using Python3.7 or higher.
Enter the local repository root folder.
Install this project in editable mode:

pip install -e .
"""
import setuptools

# Show PyPI.md as PyPI "Project description"
# encoding="utf-8" is for tree symbols: └─, ├─, etc.
with open("doc/PyPI.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="microspecgui", # do not use dashes or underscores in names!
    version="0.0.1a7", # must increment this to re-upload
    author="Chromation",
    author_email="mike@chromationspec.com",
    description="Chromation spectrometer dev-kit GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/microspectrometer/microspecgui",
    project_urls={
        'Chromation': 'https://www.chromation.com/',
    },
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "microspec-gui=microspecgui.__main__:main",
            ],
        },
    # Include `sdist` data files in the `bdist`.
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires='>=3.7',
    install_requires=[
        "pygstuff",
        "microspec"
        ],
    license='MIT', # field in *.egg-info/PKG-INFO
    platforms=['Windows', 'Mac', 'Linux'], # legacy field in *.egg-info/PKG-INFO
)

