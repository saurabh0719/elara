from distutils.core import setup

with open("README.rst") as f:
    long_description = f.read()

setup(
    name="elara",
    packages=["elara"],
    version="0.4.0",
    license="three-clause BSD",
    description="Elara DB is an easy to use, lightweight NoSQL database written for python that can also be used as a fast in-memory cache for JSON-serializable data. Includes various methods and features to manipulate data structures in-memory, protect database files and export data.",
    long_description=long_description,
    author="Saurabh Pujari",
    author_email="saurabhpuj99@gmail.com",
    url="https://github.com/saurabh0719/elara",
    keywords=[
        "database",
        "key-value",
        "storage",
        "file storage",
        "key-value database",
        "nosql",
        "nosql database",
        "cache",
        "file cache",
    ],
    project_urls={
        "Documentation": "https://github.com/saurabh0719/elara#readme",
        "Source": "https://github.com/saurabh0719/elara",
    },
    install_requires=["cryptography", "msgpack"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
    ],
)
