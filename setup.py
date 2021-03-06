
from setuptools import setup, find_packages
setup(name='spl',
      version='1.0',
      url='https://github.com/CCI-MOC/moc-public',
      packages=find_packages(),
      scripts=['spl_init.py', 'spl_restful.py', 'spl_shell.py'],
      install_requires=[
          'flask',
          'libvirt-python',
          'sqlalchemy',
          'Flask-HTTPAuth',
      ],
      )
