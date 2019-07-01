from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DEEPCON",
    version="0.0.3",
    author="Badri Adhikari",
    author_email="adhikarib@umsl.edu",
    description="Protein Contact Prediction using Dilated Convolutional Neural Networks with Dropout",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/badriadhikari/DEEPCON",
    packages=find_packages(),    
	package_data={
        'DEEPCON.covariance': [
            'DEEPCON/deepcon-covariance/weights-rdd-covariance.hdf5'
        ]
    },
    include_package_data=True,
	install_requires=open('requirements.txt').read().splitlines(),
	setup_requires=['numpy', 'pyyaml'],
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
		'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
    ],
)
