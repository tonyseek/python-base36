from setuptools import setup


with open('README.rst') as readme:
    next(readme)
    long_description = ''.join(readme).strip()


setup(
    name='base36',
    version='0.1.0',
    author='Jiangge Zhang',
    author_email='tonyseek@gmail.com',
    description='Yet another implementation for the positional numeral system '
                'using 36 as the radix.',
    long_description=long_description,
    url='https://github.com/tonyseek/python-base36',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    py_modules=['base36'],
    platforms=['Any'],
)
