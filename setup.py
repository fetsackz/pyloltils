from setuptools import setup

setup(
    name='pyloltils',
    version='0.0.1',    
    description='create plot functions for torch applications to minimize boilerplate, and rewritin g of code',
    url='https://github.com/fetsackz/pyloltils',
    author='fetsackz',
    author_email='-',
    license='MIT License',
    packages=['pyloltils'],
    install_requires=['matplotlib',                     
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: Microsoft :: Windows :: Windows 11',        
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
