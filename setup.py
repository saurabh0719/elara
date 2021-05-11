
from distutils.core import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
setup(
  name = 'elara',         
  packages = ['elara'],   
  version = '0.1.2',      
  license='three-clause BSD',        
  description = 'Elara DB is an easy to use key-value storage for your python projects!',   
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = 'Saurabh Pujari',                   #
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
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'Topic :: Database',
    'License :: OSI Approved :: BSD License',   
    'Programming Language :: Python'
  ],
)