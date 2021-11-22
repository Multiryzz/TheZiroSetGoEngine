#-------------------------------------------------------------------------------
# Name:        Debug
# Purpose:
#
# Author:      Siro
#
# Created:     22.11.2021
# Copyright:   (c) Multiryzz 2021
# Licence:     GPL V3
#-------------------------------------------------------------------------------

def activateDebug(Activate):

    if Activate == True:
        global debug
        debug = True
def text(text):
    print(text)