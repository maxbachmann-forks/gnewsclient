from setuptools import setup


def readme():
    with open('README.md') as f:
        descr = f.read()
    return descr


setup(name='gnewsclient',
      version='1.12',
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
      ],
      keywords='google news feed python client feed',
      description='Python client for Google News Feed.',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='http://github.com/nikhilkumarsingh/gnewsclient',
      author='Nikhil Kumar Singh',
      author_email='nikhilksingh97@gmail.com',
      license='MIT',
      packages=['gnewsclient'],
      install_requires=['requests', 'rapidfuzz', 'feedparser'],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'gnewsclient = gnewsclient.gnewsclient:main'
          ],
      }
      )
