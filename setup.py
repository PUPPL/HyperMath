from setuptools import setup, find_packages

setup(name='Hypermath', 
version='0.0.2',
description='Math',
author='7kcrafter7',
author_email='mathcodin7@gmail.com',
url='https://cafe.naver.com/mersenne',
license='MIT', 
py_modules=['Prime', 'BigNumber', 'Factorize','pyecm'],
python_requires='>=3',
install_requires=['gmpy2', 'numpy', 'Crypto', 'iteration_utilities'], 
packages=['Prime']
)
