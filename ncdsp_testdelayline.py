#!/usr/bin/python

#
# ncdsp_testdelayline.py
#

import sys

from ncdsp import *

# create the delay line
createdelayline( 'yummy', 40 )

# set up the input
# always return 0, unless it's the first timestep
# introduce an impulse at the first timestep
determinefuncs['yummy_input'] = lambda state: 0
vals[('yummy_input',0)] = 1
vals[('yummy_input',7)] = 5

for time in range(50):
    for cellnum in range( 40 ):
        cellname = 'yummy_{0}'.format(cellnum)
        cellvalue = read((cellname,time))
        sys.stdout.write(repr(cellvalue))
    sys.stdout.write("\n")


# vim:sw=4:ts=4:ai:et