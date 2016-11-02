import matplotlib.pyplot as plt
import matplotlib
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import sys
import math
"""
verts = [
    (0., 0.), # left, bottom
    (0., 1.), # left, top
    (1., 1.), # right, top
    (1., 0.), # right, bottom
    (0., 0.), # ignored
    ]
http://matplotlib.org/api/path_api.html
http://matplotlib.org/users/path_tutorial.html
http://matplotlib.org/api/patches_api.html
http://stackoverflow.com/questions/36730261/matplotlib-path-contains-point
"""

def polygon_to_patch(name, verts, colour):
    if len(verts) < 2:
        path = Path([], [])
        patch = patches.PathPatch(path, fill=False, edgecolor=colour, lw=1)
        return
    n_internal_points = len(verts) - 2
    codes = [Path.MOVETO] +  [ Path.LINETO] * n_internal_points + [ Path.CLOSEPOLY ]
    debug = False
    if ( debug ):
         print "VERTS = ", verts
    path = Path(verts, codes)
    #patch = patches.PathPatch(path, facecolor='orange', lw=2)
    if "manifold" in name:
        ec = "blue"
    else:
        ec = "red"
    patch = patches.PathPatch(path, fill=False, edgecolor=ec, lw=1)
    return patch

def dict_to_patches(verts_dict):
    my_patches = []
    for key, verts in verts_dict.iteritems():
        if ( len(verts) >= 2 ):
            patch = polygon_to_patch(key,verts,"red")
            my_patches.append( patch )
    #my_patches = map( polygon_to_patch, verts_dict.values() )
    return my_patches

def dict_to_bounds(verts_dict):
    verts = verts_dict.values()
    #all_verts = reduce( lambda a, b : a + b, verts )
    #numpy_array = np.array(all_verts)
    numpy_array = np.concatenate( verts )
    #print "numpy_array = ", numpy_array

    y_column = numpy_array[:,1]
    y_min, y_max = np.amin(y_column), np.amax(y_column)
    x_column = numpy_array[:,0]
    x_min, x_max = np.amin(x_column), np.amax(x_column)
    return x_min, x_max, y_min, y_max


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#import Image
image = mpimg.imread("07-014-3_kitchen_wing_floor_plan_(proposed)_1st_june_2008_stamped.jpg")
plt.imshow(image)

def verts_to_image_dict(verts_dict):
    for key,value in verts_dict.iteritems():
        if ( ".jpg" in key  ):
            return { key:value }
    return {}

"""
for each room (not manifold and not .jpg )
find manifold inside room
lay_pipe_in_room

"""

def is_room(name):
    if ( ".jpg" in name ):
        return False
    if ( "manifold" in name ):
        return False
    return True

import matplotlib.path as mplPath
"""
path.contains_point((1,50))
"""

def geometry_to_centroid(inner):
    x_average = np.average(inner[:,0][:-1])
    y_average = np.average(inner[:,1][:-1])
    return (x_average,y_average)

def contour_inside(name, room, inner,outer):
    inner_path = mplPath.Path(inner)
    outer_path = mplPath.Path(outer)

    centroid = geometry_to_centroid(inner)
    b = outer_path.contains_point( centroid)
    #b = outer_path.contains_path(inner_path)
    return b


def named_manifold_in_named_room(name, room, verts_dict):
    return contour_inside(name, room, verts_dict[name], verts_dict[room]  )

def find_manifold_in_room(room, verts_dict):
    for name in verts_dict.keys():
        if ( "manifold" in name ):
            bool =  named_manifold_in_named_room(name, room, verts_dict)
            if ( bool):
                return name
    return ""

def dist(x1,y1, x2,y2, x3,y3): # x3,y3 is the point
    px = x2-x1
    py = y2-y1

    something = px*px + py*py

    u =  ((x3 - x1) * px + (y3 - y1) * py) / float(something)

    if u > 1:
        u = 1
    elif u < 0:
        u = 0

    x = x1 + u * px
    y = y1 + u * py

    dx = x - x3
    dy = y - y3

    # Note: If the actual distance does not matter,
    # if you only want to compare what this function
    # returns to other results of this function, you
    # can just return the squared distance instead
    # (i.e. remove the sqrt) to gain a little performance

    dist = math.sqrt(dx*dx + dy*dy)

    return dist

def perpendicular_point_on_edge(x1,y1,x2,y2,x3,y3):
        dx = (x2-x1)
        dy = (y2-y1)
        k = ((y2-y1) * (x3-x1) - (x2-x1) * (y3-y1)) / (dy * dy + dx * dx)
        x4 = x3 - k * dy
        y4 = y3 + k * dx
        return (x4, y4)

def get_edge_nearest_manifold( room_name, manifold_name, verts_dict ):
    room = verts_dict[room_name]
    n_points, n_dims = room.shape
    n_edges = n_points - 1
    print "n_edges = ", n_edges
    (x3,y3) = geometry_to_centroid(verts_dict[manifold_name])
    distances      = []
    points_on_edge  = []
    for i in range(n_edges):
        x1 = room[i][0]
        y1 = room[i][1]
        x2 = room[i+1][0]
        y2 = room[i+1][1]
        distances.append( dist(x1,y1, x2,y2, x3,y3) )
        p4 = perpendicular_point_on_edge(x1,y1,x2,y2,x3,y3)
        points_on_edge.append(  p4 )
    print "distances = ", distances
    index_min = min(xrange(len(distances)), key=distances.__getitem__)
    return index_min, points_on_edge[index_min],(x3, y3)

def point_to_marker( point ):
    points = []
    step = 10
    for dx in range(-step, 3 * step, 2 * step ):
        for dy in  range(-step, 3 * step, 2 * step ):
            points.append( point )
            star_point = (point[0] + dx, point[1] + dy)
            points.append(star_point )
            points.append( point )
    a = np.array(points )
    return a

def point_to_patch( point ):
    a = point_to_marker( point )
    patch = polygon_to_patch("anything",a)
    return patch

def point_to_wedge(point, color):
    return matplotlib.patches.Wedge( point, 10, 0, 360, color=color )


"""
"""

def move_edge_inwards(room, edge_index, n, gap):
    p1 = room[edge_index] + 2 * gap * n
    p2 = room[edge_index + 1] + 2 * gap * n
    a = np.vstack((p1,p2,p1)) #np.concatenate( (p1,p2,p1), axis=1 )
    patch = polygon_to_patch("anything",a,"yellow")
    return p1, p2, patch

def perpendicular_point_on_edge_3(p1,p2,p3):
    return perpendicular_point_on_edge(p1[0],p1[1],p2[0],p2[1],p3[0],p3[1])

def perform_room_layout(room_name, manifold_name, verts_dict):
    centroid = geometry_to_centroid(verts_dict[manifold_name])
    # find edge nearest to centroid
    # put two points in from edge perpendicular to side
    edge_index , edge_point, manifold_centroid = get_edge_nearest_manifold(room_name, manifold_name, verts_dict)
    print "edge_point = ", edge_point
    a =  point_to_marker( edge_point )
    b =  point_to_marker( manifold_centroid )
    vector_into_room = np.array(manifold_centroid) - np.array(edge_point)
    n = vector_into_room / np.linalg.norm(vector_into_room)
    gap  = 80
    red  = edge_point + 0.5 * gap * n
    blue = edge_point + 1.5 * gap * n
    points  = [ edge_point, red, blue ]
    colours = ["green", "red", "blue" ]
    pairs = zip(points,colours)
    l =  map(lambda (a,b) : point_to_wedge(a,b) , pairs )
    room = verts_dict[room_name]
    A, B, new_edge       = move_edge_inwards(room, edge_index, n, gap)
    p1 = room[edge_index]
    p2 = room[edge_index + 1]
    pp = perpendicular_point_on_edge_3(p1,p2,B)
    vec = B - pp
    n = vec / np.linalg.norm(vec)
    print "second egde in = ", n
    A_2, B_2, new_edge_2 = move_edge_inwards(room, edge_index + 1, n, gap)
    l.append(new_edge)
    l.append(new_edge_2)
    print "l = ", l
    print "vector_into_room = ", vector_into_room
    return np.concatenate((a,b) ), l


def lay_pipes_in_room( room_name, verts_dict):
    manifold_name = find_manifold_in_room(room_name, verts_dict)
    print "room = ", room_name, "manifold_name = ", manifold_name
    if ( manifold_name != "" ):
        verts_dict_out, patch_list = perform_room_layout( room_name, manifold_name, verts_dict)
    else:
        verts_dict_out = np.array([])
        patch_list = []
    return verts_dict_out, patch_list

def lay_pipes(verts_dict):
    output_verts   = {}
    output_patches = {}
    for room_candidate in verts_dict.keys():
        if is_room(room_candidate):
            output_verts[room_candidate], patch_list = lay_pipes_in_room( room_candidate, verts_dict)
            output_patches[room_candidate] = patch_list
    return output_verts, output_patches


def complete_plot(verts_dict ):
    """
    look for image
    """

    fig = plt.figure()
    ax = fig.add_subplot(111)
    I= mpimg.imread("07-014-3_kitchen_wing_floor_plan_(proposed)_1st_june_2008_stamped.jpg")
    #RI = ax.imref2d(size(I));
    #RI.XWorldLimits = [0, 3];
    #RI.YWorldLimits = [2, 5];

    patches    =  dict_to_patches(verts_dict)
    image_dict =  verts_to_image_dict(verts_dict)
    image_bounds =  dict_to_bounds(image_dict)
    ax.imshow(I, extent = image_bounds) # ax.imshow(I, extent = [0, 10000, 0, 10000])
    add_input_patchs = False
    if add_input_patchs:
        for patch in patches:
            ax.add_patch(patch)

    output_verts_dict, output_patches_dict = lay_pipes(verts_dict)
    output_patches    =  dict_to_patches(output_verts_dict)
    for name, output_patch_list in output_patches_dict.iteritems():
        for output_patch in output_patch_list:
            ax.add_patch(output_patch)
    #for patch in output_patches:
    #    ax.add_patch(patch)

    bounds = dict_to_bounds(verts_dict)
    #print "bounds = ", bounds
    x_min, x_max, y_min, y_max = bounds
    ax.set_xlim(x_min ,x_max) # ax.set_xlim(-2,2)
    ax.set_ylim(y_min, y_max) # ax.set_xlim(-2,2)
    plt.show()

def main():
    verts = [
        (0., 0.), # left, bottom
        (0., 1.), # left, top
        (1., 1.), # right, top
        (1., 0.), # right, bottom
        (0., 0.), # ignored
        ]
    verts_dict = { "test": verts }
    complete_plot( verts_dict )
if __name__ == "__main__":
    main()




