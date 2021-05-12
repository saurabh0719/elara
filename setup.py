from distutils.core import setup

with open('README.rst') as f:
    long_description = f.read()
    
setup(
  name = 'elara',         
  packages = ['elara'],   
  version = '0.2.0',      
  license='three-clause BSD',        
  description = 'Elara DB is an easy to use, key-value database written for python that can also be used as a fast in-memory cache. Includes various methods to manipulate data structures in-memory, secure database files and export data.',   
  long_description = long_description,
  author = 'Saurabh Pujari',                   
  author_email = 'saurabhpuj99@gmail.com',      
  url = 'https://github.com/saurabh0719/elara',  
  keywords = [
    'database',
    'key-value',
    'storage',
    'file storage',
    'json storage',
    'json database'
    'key-value database'  
    ],   # Keywords that define your package best
  install_requires=[
    'cryptography'
    ],
  classifiers=[
    'Development Status :: Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Database',
    'License :: OSI Approved :: BSD License',   
    'Programming Language :: Python'
  ],
)