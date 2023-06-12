# Module is a python file with functions, classes and other components
# We use modules to break code down into reusable structures.

# creating a module 
import helpers
helpers.display('Not a warning', True)

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')


# A package is a published collection of packages.
# Pip is the command line installer that is used to install packages.