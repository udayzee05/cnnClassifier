import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cnn_classifier",
    version="0.0.1",
    author="Uday Zope",
    author_email="udayzee05@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/udayzee05/cnnClassifier",
    packages=setuptools.find_packages(),
    
)