Step 1: Environment Setup
=========================

>In this tutorial, we will setup the python 2.7 environment. 

Before Start
------------

You should have python 2.7 installed. Generally, if you are using CentOS 7.2, Ubuntu LTS, python 2.7 is installed by default.

Using the following command to check the installation:

``` bash
~$ python --version
Python 2.7.12

~$ pip --version
pip 9.0.1 from /home/cesbd/.local/lib/python2.7/site-packages (python 2.7)

~$ ipython --version
5.5.0
```

IPython Playground
------------------
[IPython](http://ipython.org/) is a good start to play with python expressions and directives:

``` bash
~$ ipython
Python 2.7.12 (default, Nov 20 2017, 18:23:56)
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In []: import os
In []: print os.name
posix
In []: print os.defpath
:/bin:/usr/bin

```

VSCode
------
Many fantastic editors and IDEs for python
  - [PyCharm](https://www.jetbrains.com/pycharm/) - JetBrains product - Commercial
  - [Sublim Text 3](https://www.sublimetext.com/3) - Open Source
  - [Atom](https://atom.io/) - js based
  - [VSCode](https://code.visualstudio.com) - Microsoft product - Open Source
  - UltraEdit
  - Notepad++
 
 And we use [VSCode](https://code.visualstudio.com) from Microsoft, which fits  sprint-boot, angular framework and java, typescript, javascript, html, scss, shell and python languages.


Packages
--------
[Pypi](https://pypi.python.org) is where you can find all the packages for almost all your work, including libs from it maintenance to data science and deep learning for ai.

The suggested ones are:
  - re : for regex
  - sys : for python info
  - os : for OS operations
  - datetime : to deal with datetime
  - time : to generate time
  - click: for commandline options
  - unittest2: for unittest
  - logging: for log either on screen or files
  - numpy: for metrics calculation
  - pandas: for table formulas
  - matplotlib: for data visualization

