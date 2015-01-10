__author__ = 'david'


def cube_points():
    points = []
    for i in range(0,8):
        point = [ i & 1, ( i & 2 ) / 2, (i & 4) / 4 ]
        points.append(point)
    return points


def cube_polygons():
    return [ [0,2,3,1],
    [1,3,7,5],
    [5,7,6,4],
    [4,6,2,0],
    [2,6,7,3],
    [4,0,1,5] ]


def cube():
    return ( cube_points(), cube_polygons())