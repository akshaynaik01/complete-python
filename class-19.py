   # Modules And Package
 
 # Modules: A file containing python code(function,var,classes).  It allows code reuse snd organization.
 
 # Package: A package is a directory of modules with an __init__.py file,enabling hierarchy.
 

import math_utils

from math_utils import add,sub
print(add(20,10))
print(sub(20,10))
#  or

print(math_utils.add(20,10))


# Package
# syntax
from folder_name import file_name1,file_name2

from folder_name.file_name1 import add
from folder_name.file_name2 import to_upper
