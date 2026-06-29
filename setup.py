from setuptools import setup, find_packages

setup(
    name="vulnterm",
    version="2.0.0",
    author="Syed Rehan",
    author_email="rehuonly@aol.com",
    description="Terminal HackBar - Advanced Security Testing Toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/rehuux/vulnterm",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.28.0",
        "colorama>=0.4.6",
    ],
    entry_points={
        "console_scripts": [
            "hackbar=hackbar.__main__:main",
        ],
    },
)
