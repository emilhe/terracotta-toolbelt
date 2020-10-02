import pathlib
import os

from setuptools import setup


HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(
    name='terracotta-toolbelt',
    author="Emil Haldrup Eriksen",
    author_email="emil.h.eriksen@gmail.com",
    description="A small Terracotta tool collection",
    version=os.getenv("CI_COMMIT_TAG", "v0.0.5").strip("v"),
    url='https://github.com/thedirtyfew/terracotta-toolbelt',
    packages=["terracotta_toolbelt", "terracotta_toolbelt.extensions"],
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    python_requires='>=3.6',
    install_requires=['terracotta', 'flask', 'rasterio']
)

