import pathlib
import setuptools

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setuptools.setup(
    name="blenderUtils",
    version="0.0.1",
    description="Working with geospatial data to generate 3D visualisations",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vizzTools/blenderUtils",
    author="OSenar",
    author_email="oscar.esbri@vizzuality.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    packages=['blenderUtils'],
    install_requires=['requests>=2.2.0', 'folium==0.8.3'],
    entry_points={
        "console_scripts": [
            "vizzpython=blenderUtils.__main__:main",
        ]
    },
)
