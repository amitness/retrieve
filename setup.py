from setuptools import setup, find_packages

setup(
    name='retrieve',
    version='0.0.5',
    license='MIT',
    description='Retrieve pre-trained models and cache it locally',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    author='Amit Chaudhary',
    author_email='meamitkc@gmail.com',
    url='https://github.com/amitness/retrieve',
    install_requires=['requests', 'tqdm'],
    packages=find_packages(),
)
