import setuptools

import branched

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=branched.name,
    version=branched.version,
    author="Koen Woortman",
    author_email="koensw@outlook.com",
    url='https://github.com/koenwoortman/branched',
    description="Terminal selector for git branches",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        'simple_term_menu',
    ],
    entry_points={
        'console_scripts': [
            'branched = branched:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Environment :: Console',
    ],
)
