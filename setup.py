from setuptools import setup, find_packages

CLASSIFIERS = [
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
]
 
setup(name='flames',
      version='1.0',
      url='https://github.com/VaasuDevanS/flames',
      license='GNU-GPL',
      author='Vaasu Devan S',
      author_email='vaasuceg.96@gmail.com',
      description='Compute the FLAMES value with amazing results using the flames module in python',
      packages=find_packages(),
      long_description=open('README.rst').read(),
      zip_safe=False,
      classifiers=CLASSIFIERS,
 )
