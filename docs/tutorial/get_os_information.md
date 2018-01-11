Tutorial 2: Get OS Information
==============================

>In this tutorial, we will introduce a simple single file script as an example of operation.

Once we try to solve some maintenance issues, we have to diagnostic the root cause first, and some interaction between the machine and human happens. There are different ways to lead to the answer. Some one would use bash command to talk, another combines with shell scripts and some others would use scripts as python, as the internal directives in Ansible does.

Imaging that we want to get the OS general information of a system. Lets use 'lsb_release' as an example:

``` bash
~$ lsb_release -a
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.3 LTS
Release:        16.04
Codename:       xenial
```

How to get the codename or release number? Here we introduce the python script to do the job.

Try with IPython
----------------

- Enter ipython env

``` bash
~$ ipython
Python 2.7.12 (default, Nov 20 2017, 18:23:56)
Type "copyright", "credits" or "license" for more information.

IPython 5.5.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

In [1]:
``` 

Excute the bash command
-----------------------

``` bash
In [1]: lsb_release -a
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-1-e88c09c26ddd> in <module>()
----> 1 lsb_release -a

NameError: name 'lsb_release' is not defined

In [2]: ~$ ipython
  File "<ipython-input-2-eeeae6e09cf7>", line 1
    ~$ ipython
         ^
SyntaxError: invalid syntax

```

See what? Python is not compatible with bash. We have to leverage some libs as os to do that.

``` bash
In [3]: import os

In [4]: command = os.popen('lsb_release -a')

In [5]: type(command)
Out[5]: file

In [6]: print command
<open file 'lsb_release -a', mode 'r' at 0x7ff66ae399c0>
```

Here we use pip line to simulate the bash execution, and result is redirect to the stream type as file. 

Retrieve the results
--------------------

As the output is a file, so we can read lines of the file to get the result.

``` bash
In [8]: results = command.readlines()

In [9]: type(results)
Out[9]: list

In [10]: print results
['Distributor ID:\tUbuntu\n', 'Description:\tUbuntu 16.04.3 LTS\n', 'Release:\t16.04\n', 'Codename:\txenial\n']
```

Iter the results
----------------

The result is embraced in a list, we have to iterate to the target and erase the noise.

``` bash
In [13]: dist_name_line = results[0]

In [15]: type(dist_name_line)
Out[15]: <type 'str'>

In [16]: print dist_name_line
Distributor ID: Ubuntu

In [18]: dist_release_line = results[2]

In [19]: print dist_release_line
Release:        16.04
```

Digest the value
----------------

Now we got the target line as a string 'Release:        16.04', but the '16.04' is what we really wanted. 

As people always says that every roads lead to Roma, there are many way to achive the goal, and here we will show 2 of them.

- One way to get information from string is to use regex to match the target.

``` bash
In [21]: import re

In [22]: pattern = r'(.*):\t(.*)'

In [23]: regex = re.compile(pattern)

In [25]: value = regex.findall(dist_release_line)

In [26]: print value
[('Release', '16.04')]
```

Now the value is a list of tuples, we just pick the right item:

``` bash
In [27]: (dist_release_type, dist_release_value) = value[0]

In [28]: print dist_release_value
16.04

In [29]: type(dist_release_value)
Out[29]: <type 'str'>
```
- Another one is split the string into a list the get the target index.

``` bash
In [30]: (dist_release_type, dist_release_value) = dist_release_line.split()

In [31]: print dist_release_value
16.04

In [32]: type(dist_release_value)
Out[32]: <type 'str'>
```

Convert the type
----------------

What we got now is a string, but we want some number values.

``` bash
In [33]: release_number = float(dist_release_value)

In [34]: print release_number
16.04

In [35]: type(release_number)
Out[35]: <type 'float'>
```

Get all the value
-----------------

Not only the release number, but all the values are useful, and we want to keep them and will be used in the future.

``` bash
In [40]: for result in results:
    ...:     (d_type, d_value) = result.split(':\t')
    ...:     print '{} - {}'.format(d_type, d_value)
    ...:
    ...:
Distributor ID - Ubuntu

Description - Ubuntu 16.04.3 LTS

Release - 16.04

Codename - xenial
```

As the result is a kind of (key, value) group, we can store them in a dictionary(Map in some other languages).

``` bash
In [43]: from collections import defaultdict

In [44]: lsb_dict = defaultdict()

In [45]: print lsb_dict
defaultdict(None, {})

In [47]: type(lsb_dict)
Out[47]: <type 'collections.defaultdict'>
```

Lets re-write the iter process:

``` bash
In [48]: for result in results:
    ...:     (d_type, d_value) = result.split(':\t')
    ...:     lsb_dict[d_type.strip()] = d_value.strip()
    ...:

In [49]: print lsb_dict
defaultdict(None, {'Release': '16.04', 'Codename': 'xenial', 'Distributor ID': 'Ubuntu', 'Description': 'Ubuntu 16.04.3 LTS'})

In [50]: lsb_dict['Description']
Out[50]: 'Ubuntu 16.04.3 LTS'

In [51]: print lsb_dict['Description']
Ubuntu 16.04.3 LTS
```


Summary the process
-------------------

The interactive way is useful for developers but we can't use it for programing. Luckily that, ipython provids a good direct to list all the history, '%hist' or '%history'

``` bash
In [36]: %hist
lsb_release -a
import os
command = os.popen('lsb_release -a')
type(command)
print command
results = command.readlines()
type(results)
print results
dist_name_line = results[0]
type(dist_name_line)
print dist_name_line
dist_release_line = results[2]
print dist_release_line
import re
pattern = r'(.*):\t(.*)'
regex = re.compile(pattern)
(d_type, d_value) = regex.match(pattern, dist_release_line)
value = regex.findall(dist_release_line)
print value
(dist_release_type, dist_release_value) = value[0]
print dist_release_value
type(dist_release_value)
(dist_release_type, dist_release_value) = dist_release_line.split()
print dist_release_value
type(dist_release_value)
release_number = float(dist_release_value)
print release_number
type(release_number)
for result in results:
    (d_type, d_value) = result.split(':\t')
    print '{} - {}'.format(d_type, d_value)
print d_type
print d_value
from collections import defaultdict
lsb_dict = defaultdict()
print lsb_dict
type(lsb_dict)
for result in results:
    (d_type, d_value) = result.split(':\t')
    lsb_dict[d_type.strip()] = d_value.strip()
print lsb_dict
lsb_dict['Description']
print lsb_dict['Description']
%hist
```

Generate the python code
------------------------

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:33:12

import os
from collections import defaultdict

command = os.popen('lsb_release -a')
results = command.readlines()

lsb_dict = defaultdict()

for result in results:
    (d_type, d_value) = result.split(':\t')
    lsb_dict[d_type.strip()] = d_value.strip()

# print lsb_dict
for key in lsb_dict:
    print '{} \t -- \t : {}'.format(key, lsb_dict[key])

```

Source code refers to [get_os_information.py](https://github.com/webji/pyops/blob/master/pyops/tutorial/get_os_information/get_os_infomation.py).

Organize in functions
----------------------

As you see the code is quite easy and simple. But is just goes from top to bottom without any stop and logic paths. We need organize.

The process is seperated into two phases:
- Execute the command and got the result map
- Print the result map

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:49:12

import os
from collections import defaultdict

def get_os_info():

    command = os.popen('lsb_release -a')
    results = command.readlines()

    lsb_dict = defaultdict()

    for result in results:
        (d_type, d_value) = result.split(':\t')
        lsb_dict[d_type.strip()] = d_value.strip()

    return lsb_dict


def display_os_info(lsb_dict):
    # print lsb_dict
    for key in lsb_dict:
        print '{} \t -- \t : {}'.format(key, lsb_dict[key])

if __name__ == '__main__':
    values = get_os_info()
    display_os_info(values)

```

Source code refers to [function_os_information.py](https://github.com/webji/pyops/blob/master/pyops/tutorial/get_os_information/function_os_information.py) as the source code.
