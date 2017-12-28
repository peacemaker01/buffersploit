#!/usr/bin/env python

import socket
from pyfiglet import Figlet
import os
import re
import shutil
import subprocess
import sys
from core import *
from color import colors
try:
    input = raw_input
except NameError:
    pass

f = Figlet(font='slant')
print f.renderText("BUFFERSPLOIT")



print colors.OKGREEN
print "                               Version 0.1 ALPHA                            "
print "---------------------------------------------------------------------------\n"
print colors.ENDC

print("what kind of test is taking place????? ;)")

print colors.OKBLUE
print("\nOption [1] single variable attack")

print("\nOption [2] double variable attack")

print("\nOption [3] triple threat ;p ")

print("\nOption [4] Quadluciuos :) ")

print colors.ENDC
def module_reload(module):
    if sys.version_info >= (3, 0):
        import importlib
        importlib.reload(module)
    else:
        reload(module)


print colors.UNDERLINE  
option=raw_input("Enter option []: ")
print colors.ENDC
if option == 'exit':
           sys.exit()
if option == 'about':
           print("\n\033[91mThis scritp was written by pE@{EM@KEr")
           pause = input("press any key to return")

if option == '1':
           try:
            module_reload(core.single)
           except:
            import core.single
if option == '2':
          try:
           module_reload(core.double)
          except:
           import core.double
if option == '3':
           try:
            module_reload(core.triple)
           except:
            import core.triple
if option == '4':
           print("not ready")

