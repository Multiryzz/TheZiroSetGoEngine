#-------------------------------------------------------------------------------
# Name:        Dir Condition
# Purpose:     nooby implementation of condition check, to check for the core
#              Components.
#
# Author:      Siro
#
# Created:     22.11.2021
# Copyright:   (c) Multiryzz 2020
# Licence:     GNU General Public License v3.0
#-------------------------------------------------------------------------------

from pathlib import Path
import sys

def dirset():

    sys.path.append('gpu_piplines/')
    sys.path.append('other/')
    sys.path.append('test_modules/')