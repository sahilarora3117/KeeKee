import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KeeKee-sahilarora3117", # Replace with your own username
    packages=[
        "KeeKee"
        ],
    entry_points={
            "console_scripts": [
                "keekee = KeeKee.gui:initialize_gui"
            ]
        },
    version="0.0.1",
    author="Sahil Arora",
    author_email="sahil.arora3117@gmail.com",
    description="A GUI from PyKeePass",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sahilarora3117/keekee",
        install_requires=[
        "pykeepass"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
