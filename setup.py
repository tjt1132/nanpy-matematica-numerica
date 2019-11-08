import setuptools

with open("README", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nanpy-pkg-ttorres", # Replace with your own username
    version="0.0.1",
    author="Ticiano J. Torres Peralta",
    author_email="ttorres@herrera.unt.edu.ar",
    description="Simple implementations of numerical analysis algorithms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tjt1132/nanpy-matematica-numerica",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
