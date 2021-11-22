#-------------------------------------------------------------------------------
# Name:        path check test
# Purpose:
#
# Author:      siro
#
# Created:     22.11.2021
# Copyright:   (c) siro 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pathlib import Path

path = '.'

for path in Path(path).iterdir():

    print(path)