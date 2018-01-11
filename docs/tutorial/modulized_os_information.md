Tutorial 3: Modulized OS Information
====================================

>In this tutorial, we will introduce a way to organize more complex code. Code will be organzied in modules.

Terms
-----

Before we goes deep into the code, let's clearify some concepts of terms.

- Package
  - A collection of libs that organized for a kind of purpose
  - Package is distributed and can be installed
- Lib
  - A collection of modules that are organized under a folder
- Module
  - A collection of classes, functions, variables defined in a file
  - Every file is a module
  - Module can be imported, reloaded and the variable and function can be used

OS Info Module
--------------

Let's create a simple lib called os_info, which contains a module called info.py.

In the %{ROOT} dir, create a folder called 'modulized_os_information'

``` bash
~$ mkdir os_info
~$ cd os_info
~$ touch info.py
```

Now we have created the lib and a module. Put the code what we previous generaged in the last tutorial[Tutorial 1: Environment Setup](environment_setup).

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

We can test the python code in the sub folder and see the result:

``` bash
~$ python info.py
Release          --      : 16.04
Codename         --      : xenial
Distributor ID   --      : Ubuntu
Description      --      : Ubuntu 16.04.3 LTS
```

Use the module
--------------

After the module created, we can used it now.

``` bash
~$ code test_info.py
```

and the code should looks like:

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-11 11:18:12

import info

values = info.get_os_info()
info.display_os_info(values)
```

and run the code:

``` bash
~$ python test_info.py
Release          --      : 16.04
Codename         --      : xenial
Distributor ID   --      : Ubuntu
Description      --      : Ubuntu 16.04.3 LTS
```

Import will run the code from the module, the first time imported.

``` bash
~$ code test_test_info.py
```

with the code:

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-11 11:18:12

import test_info

import test_info
```

``` bash
$ python test_test_info.py
Release          --      : 16.04
Codename         --      : xenial
Distributor ID   --      : Ubuntu
Description      --      : Ubuntu 16.04.3 LTS
```

The test_info.py is excuted the first time imported.

Every thing goes well, we got what we expected.

But it is too simple, maybe too naive?

Organize modules
----------------

In most cases the modules are organized in a lib folder, and called from outside of the folder.

Let's try:

``` bash
~$ cd ..
~$ code modulized_os_info.py
```

and the code is:

``` python
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Author: Will<willji@outlook.com>
# Created on 2018-01-10 19:49:12

from os_info import info

values = info.get_os_info()
info.display_os_info(values)

```

Let's have a test:

``` bash
$ python modulized_os_info.py
Traceback (most recent call last):
  File "modulized_os_info.py", line 7, in <module>
    from os_info import info
ImportError: No module named os_info
```

The module is not existed.

The fix is quite simple:

``` bash
~$ touch os_info/__init__.py
```

Now try again:

``` bash
$ python modulized_os_info.py
Release          --      : 16.04
Codename         --      : xenial
Distributor ID   --      : Ubuntu
Description      --      : Ubuntu 16.04.3 LTS
```

OK, the modules works now.

Tips
----

- \_\_name\_\_ in a module have different values with different referenced type
  - when imported, the value is the module name, as 'os_info'
  - when excuted by python directly, the value is '__main__'
  - That's why we have "if \_\_name\_\_ == \'\_\_main\_\_\'" code in modules


Source code refers to [modulized_os_information](https://github.com/webji/pyops/tree/master/pyops/tutorial/modulized_os_information).
