import operator
from numpy import amax
from visual import false
from visual_common.create_display import color
from visual_common.primitives import sphere, convex, cylinder
#from Main import extents

__author__ = 'david'


def extents(o):
    (points,polygons) = o
    min = list(points[0])
    max = list(points[0])

    for p in points[1:]:
        for i in range(0,3):
            if p[i] > max[i]:
                max[i] = p[i]
            if p[i] < min[i]:
                min[i] = p[i]
    return (min,max)

def draw_object( o ):
    fill_poly = false
    (points,polygons) = o
    (min_coords,max_coords) = extents(o)
    difference =  map(operator.sub, max_coords , min_coords )
    print("difference =", difference)
    big_dim = max( difference )
    radius = big_dim / 40.0
    c = 0
    pi = 0
    #polygons=polygons[3:4]
    for point in points:
        sphere(pos = point, color = color.blue, radius = radius )
    for polygon in polygons:
        point_list = []
        for index in polygon:
            point_list.append( points[index] )
        pi += 1
        #pi = polygon_index
        col = ( pi & 1,  (pi & 2) / 2 , (pi & 4) / 4 )
        #col = color.cyan
        print("point list = ", point_list)
        if ( fill_poly ):
           convex(pos = point_list, color = col)
        #point_list.reverse()
        #convex(pos = point_list, color = col)

        npoints = len(point_list)
        for i in range(0,npoints):
            p1 = point_list[i]
            p2 = point_list[ ( i + 1 ) % npoints]
            axis = map(operator.sub,p2,p1)
            cylinder( pos = p1, axis= axis , radius= radius / 2)
        if ( fill_poly ):
          point_list.reverse()
          convex(pos = point_list, color = col)