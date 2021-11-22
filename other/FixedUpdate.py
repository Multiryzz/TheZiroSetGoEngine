#-------------------------------------------------------------------------------
# Name:        Fixed Update
# Purpose:
#
# Author:      Siro
#
# Created:     18.11.2021
# Copyright:   (c) Multiryzz 2021
# Licence:     All rights reserved
#-------------------------------------------------------------------------------
from cube import RunTime, a, b, c, d


def stableLoop(runTime, precision, FtE, run):
    while True:
        global a
        global b
        global c
        global d
        if run == True:
            try:
                if int(precision) == 3:
                    if((runTime - b) > 1):
                        print("1 Second Passed...")
                        FtE
                        b = runTime
                        num = a/1
                        fps = "fps: " + str(num)+ "\n"
                        sys.stdout.write(fps)

                elif int(precision) == 2:
                    if (((runTime - c) > 0.02) ):
                            c = runTime
                        # DEBUG ONLY it makes the program super slow because of print
                            #print(format((runTime - b), ".2f"))
                elif int(precision) == 1:
                    #10x per second
                    if((runTime - d) > 0.1):
                        d = runTime
                        #every second

                    print("bb")
                else:
                    print("please use an Int, that is smaller then 4...")
                    exit()
            except ValueError:
                try:
                    int(precision)
                except ValueError:
                    print("you need to use an int for precision")
                    exit()
            if precision > 54444444:
                exit()
            #50x per second

#TODO bugfixing
"""
cant use those functions right, they need to run in an stable loop
and they should be easyly callable,
they need to get the runtime somehow without making an imposible import loop
also the user should just be able to call it with
SlowFixedUpdate(TestFunction, True)
True is here to pause the function with another function
so that you have more controll what is executed at any time.

good luck future siro!
"""




#gets called every second
def SlowFixedUpdate(function, run):
    global runtime
    runTime = runtime
    stableLoop(runTime, 3, function, run)
#gets called 10x per second
def FixedUpdate(function, run):
    global RunTime
    runTime = RunTime
    stableLoop(runTime, 2, function, run)
#Best for fast realtime Interactions gets called 50x per second
def FastFixedUpdate(function, run):
    global RunTime
    runTime = RunTime
    stableLoop(runTime, 1, function, run)

def test():
    print("hiii")

def TestModule():
    SlowFixedUpdate(test(), True)

if __name__ == '__main__':
    TestModule()
