

__author__ = 'david'
"""
need numpy and 32-bit VPython
"""

#from Polygon import *
from visual import *
from cube import *
import datetime
from draw_object import *
"""
get to stage where we are intersecting two
polygons to find a points - display these

shift and translate to form the second cube
"""
import sys

print ("hello")
d = datetime.datetime.now()
print(str(d))
print(sys.version)

sphere(pos = vector(-1,0,0), radius = 0.5 , color = color.green )
print "hello"
c = cube()
draw_object(c)
print("cube points = ", c )

