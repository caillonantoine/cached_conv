import setuptools

with open("README.md", "r") as readme:
    readme = readme.read()

with open("requirements.txt", "r") as requirements:
    requirements = requirements.read()

setuptools.setup(
    name="cached_conv",
    version="1.1-b2",
    author="Antoine CAILLON",
    author_email="caillon@ircam.fr",
    description="Tools allowing to use neural network inside realtime apps.",
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements.split("\n"),
    python_requires='>=3.7',
)
