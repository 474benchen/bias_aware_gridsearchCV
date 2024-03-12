from setuptools import setup, find_packages

# Read content from the requirements.txt file
with open('requirements_pip.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='YourPackageName',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=requirements,  # List of dependencies from your requirements.txt
    description='Modified version of gridsearchCV to support bias mitigation',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/474benchen/bias_aware_gridsearchCV',
    classifiers=[
        'Programming Language :: Python :: 3.12'
    ],
    python_requires='>=3.12',
)
