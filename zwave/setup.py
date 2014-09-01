import sys
from distutils.core import setup

if sys.version_info[:2] < (2, 5) or sys.version_info[0] > 2:
    msg = ("brewery requires Python 2.5 or later but does not work on "
           "any version of Python 3.  You are using version %s.  Please "
           "install using a supported version." % sys.version)
    sys.stderr.write(msg)
    sys.exit(1)

CLASSIFIERS = [
    'Development Status :: 3 - Development',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.5',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Software Development',
    'Topic :: Software Development :: Embedded Systems',
    'Topic :: System :: Hardware'
    ]

setup(name='brewery',
      version='2014-08-21',
      description='The python brewery.',
      license='MIT X11',
      url='https://github.com/Malt-a-bars/brewery',
      author='Sam Grimee',
      author_email='',
      maintainer='Sam Grimee',
      maintainer_email='',
      classifiers=CLASSIFIERS,
      package_dir = {'brewery': 'src'},
      packages=['brewery']
      )
