**8. `setup.py`:**

```python
from setuptools import setup, find_packages

setup(
    name='kyoo_log',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[], # Kosong jika tidak ada dependensi
    python_requires='>=3.6',
    description='A simple logging library for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Kyoo-log', # Ganti dengan nama Anda
    author_email='movahmi@gmail.com', # Ganti dengan email Anda
    url='https://github.com/username/kyoo-log', # Ganti dengan username dan repo Anda
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)