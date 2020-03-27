import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newmode",
    version="0.1.6",
    author="New/Mode",
    author_email="info@newmode.net",
    description="New/Mode API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NewMode/python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

