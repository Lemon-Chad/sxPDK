import setuptools
from distutils.core import setup
setup(
  name = 'sxPDK',         # How you named your package folder (MyLib)
  packages = ['sxPDK'],   # Chose the same as "name"
  version = '1.5.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'The Plugin Development Kit for ShieldX Manager.',   # Give a short description about your library
  author = 'LemonChad',                   # Type in your name
  author_email = 'jakitmationstudios@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Lemon-Chad/sxPDK',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Lemon-Chad/sxPDK/archive/v_1.5.4.zip',    # I explain this later on
  keywords = ['discord.py', 'shieldx', 'shieldxplugins'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'discord',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)