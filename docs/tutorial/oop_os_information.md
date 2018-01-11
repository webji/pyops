Tutorial 4: OOP OS Information
==============================

>In this tutorial, we will introduce how to represent the physical world object into digital model. Thus the project could be more suiltable for engineering.

Prerequistites
--------------
- [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) 
  - Before we start this section, you'd better under stand what is OOP. OOP is not only a skill for programming, but a different way you understand the world. It is not only an engineering but a philosophical thinking way, and it re-shape the software industry thoroughly. For more details, please refer to this topic [Object Oriented Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)

- [click](http://click.pocoo.org)
  - Besides the OOP, we introduced a new package of python called [click](http://click.pocoo.org) which is a fantastic tool for cli command options.

Objects
-------

In this sample, we defines an object called OS_CI, which is a naming from CMDB style.

This OS_CI have 5 public properties and 1 public methods

Python is not a strict type language, so it does not have 'public/protected/private' keyword as other OOP languages. Anyhow, it is the Python style, simple but works and straight forward.

We organize the code in modules.

``` bash
~$ mkdir libs
~$ touch libs/__init__.py
~$ code libs/os_info.py
```
The code is as follows:

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:59:10

import os
from collections import defaultdict
import datetime

import commands


class OS_CI(object):
    version = 'UNKOWN'
    dist_name = 'UNKOWN'
    dist_release = 'UNKOWN'
    dist_codename = 'UNKOWN'
    kernel = 'UNKOWN'

    def __init__(self):
        super(OS_CI, self).__init__()
        if os.name == 'posix':
            self._get_posix_dist_info()
            self._get_posix_kernel()

        
    def _get_posix_dist_info(self):
        """get the os distribution information
        """

        results = os.popen('lsb_release -a')
        lsb_dict = defaultdict()

        for result in results:
            (d_type, d_value) = result.split(':\t')
            lsb_dict[d_type.strip()] = d_value.strip()

        self.version = lsb_dict.get('Description', 'UNKOWN')
        self.dist_codename = lsb_dict.get('Codename', 'UNKOWN')
        self.dist_name = lsb_dict.get('Distributor ID', 'UNKOWN')
        self.dist_release = lsb_dict.get('Release', 'UNKOWN')


    def _get_posix_kernel(self):
        """get the os kernel information
        """

        command = os.popen('uname -r')
        results = command.readlines()
        if len(results):
            self.kernel = results[0].strip()


    def date(self):
        """get the os date value
        """

        command = os.popen('date')
        results = command.readlines()
        if len(results):
            return results[0].strip()

```

Now we can use the object:

``` bash
~$ code oop_os_info.py
```

and code is:

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 20:02:10

from libs.os_info import OS_CI

os_info = OS_CI()
print 'Kernel: {}'.format(os_info.kernel)
print 'Dist Name: {}'.format(os_info.dist_name)
print 'Dist Releast: {}'.format(os_info.dist_release)
print 'Dist Codename: {}'.format(os_info.dist_codename)
print 'Dist Versoin: {}'.format(os_info.version)
print 'OS Date: {}'.format(os_info.date())

```

The object now represents the OS_CI in the system. When you want some information, you don't care about the exact command and kernal type. You can focus on target now.

Cli Option
----------

As a tool, we want some control of the output. And the solution is add some command option. Click is one of the best choice.

The cli command we exptected is:
``` bash
 ~$ python oop_os_info.py --help
Usage: oop_os_info.py [OPTIONS] COMMAND [ARGS]...

Options:
  --fs       display fs information  [default: False]
  --disk     display disk information  [default: False]
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  dist
```

When '--fs' is specified, we show fs information, while '--disk' shows the disk information.

We have a subcommand called dist:

``` bash
~$ python oop_os_info.py dist --help
Usage: oop_os_info.py dist [OPTIONS]

Options:
  --kernel         display kernel info  [default: False]
  --dist_name      display dist name  [default: False]
  --dist_release   display release number  [default: False]
  --dist_codename  display codename  [default: False]
  --version        display dist version  [default: False]
  --help           Show this message and exit.
```

This subcommand customized what is displayed of a OS information

And code is:

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 20:02:10

import click

from libs.os_info import OS_CI

@click.group(invoke_without_command=True)
@click.option('--fs', default=False, is_flag=True, help='display fs information', show_default=True)
@click.option('--disk', default=False, is_flag=True, help='display disk information', show_default=True)
@click.version_option(version='0.0.1.0', prog_name='oop_os_info')
@click.pass_context
def cli(ctx, **kwargs):
    
    if kwargs['fs']:
        print 'fs information'

    if kwargs['disk']:
        print 'disk informati0n'

    return ctx



@cli.command()
@click.option('--kernel', default=False, is_flag=True, help='display kernel info', show_default=True)
@click.option('--dist_name', default=False, is_flag=True, help='display dist name', show_default=True)
@click.option('--dist_release', default=False, is_flag=True, help='display release number', show_default=True)
@click.option('--dist_codename', default=False, is_flag=True, help='display codename', show_default=True)
@click.option('--version', default=False, is_flag=True, help='display dist version', show_default=True)
@click.pass_context
def dist(ctx, kernel, dist_name, dist_release, dist_codename, version):
    g = ctx.obj
    os_info = OS_CI()
    if kernel:
        print 'Kernel: {}'.format(os_info.kernel)

    if dist_name:
        print 'Dist Name: {}'.format(os_info.dist_name)

    if dist_release:
        print 'Dist Releast: {}'.format(os_info.dist_release)

    if dist_codename:
        print 'Dist Codename: {}'.format(os_info.dist_codename)

    if version:
        print 'Dist Versoin: {}'.format(os_info.version)


if __name__ == '__main__':
    cli()

```

Test
----

Test of command:

``` bash
~$ python oop_os_info.py --fs
fs information
~$ python oop_os_info.py --disk
disk information
~$ python oop_os_info.py --disk --fs
fs information
disk information
```

Test of sub command

``` bash
~$ python oop_os_info.py dist
~$ python oop_os_info.py dist --kernel
Kernel: 4.4.0-43-Microsoft
~$ python oop_os_info.py dist --dist_name
Dist Name: Ubuntu
~$ python oop_os_info.py dist --dist_release
Dist Releast: 16.04
~$ python oop_os_info.py dist --dist_codename
Dist Codename: xenial
~$ python oop_os_info.py dist --version
Dist Versoin: Ubuntu 16.04.3 LTS
~$ python oop_os_info.py dist --version --kernel --dist_release
Kernel: 4.4.0-43-Microsoft
Dist Releast: 16.04
Dist Versoin: Ubuntu 16.04.3 LTS
~$ python oop_os_info.py --fs dist --version --kernel --dist_release
fs information
Kernel: 4.4.0-43-Microsoft
Dist Releast: 16.04
Dist Versoin: Ubuntu 16.04.3 LTS
```

Homework
--------
- []Complete the option '--fs' display for real systems
- []Complete the option '--disk' display for real systems

Epilog
------

Hope all above helps and wish you a good luck.

