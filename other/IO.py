#-------------------------------------------------------------------------------
# Name:        IO Module
# Purpose:     save, load, auto setup/generate custom config files.
#
# Author:      Siro
#
# Created:     22.11.2021
# Copyright:   (c) Multiryzz 2021
# Licence:     Good old GNU General Public License v3.0
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()


def CreateConfig(file_name, Dic):

    file = open("config.cfg", "wb")
    print ("Name of the file: ", file.name)
    print ("Closed or not : ", file.closed)
    print ("Opening mode : ", file.mode)
    file.close()


CreateConfig("ree", 2)