import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DEEPCON",
    version="0.0.1",
    author="Badri Adhikari",
    author_email="adhikarib@umsl.edu",
    description="Protein Contact Prediction using Dilated Convolutional Neural Networks with Dropout",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/badriadhikari",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
		'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
    ],
)