#-------------------------------------------------------------------------------
# Name:        Start
# Purpose:     Engine Start File
#
# dependencies:
#   gpu_piplines/
#   other/
#   test_modules/
# Info:
#   The Programm WILL try to run without them, but I will not guranty correct
#   functioning. So be careful what you are doing with the broken code!
# Author:      Siro
#
# Created:     22.11.2021
# Copyright:   (c) Multiryzz 2020-2021
# Licence:     GNU General Public License v3.0 uwu
#-------------------------------------------------------------------------------
import sys

from threading import Thread
from DIC import dirset
Debugging = True
dirset()
from OpenGLPiplineOne import startdisplay
from Debugging import text, activateDebug

def test(test):
    print(test)




activateDebug(Debugging)
text("yeet")


if __name__ == "__main__":


    thread = Thread(target = startdisplay, args = ())
    thread.start()
    print("everything is working omg omg uwuwuwuwuwuwuuw")

