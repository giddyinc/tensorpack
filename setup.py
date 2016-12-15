from setuptools import setup

dependencies = [
    "numpy",
    "six",
    "termcolor",
    "tqdm>4.6.1",
    "msgpack-python",
    "msgpack-numpy",
    "pyzmq",
    "subprocess32",
    "gym>=0.2.3",
]

setup(
    name="tensorpack",
    version="0.1",
    install_requires=dependencies,
)
