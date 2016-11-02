from read_fig_file import read_fig_file
from complete_plot import complete_plot, dict_to_bounds
"""

work out how to place image

2 5 0 1 0 -1 50 -1 -1 0.000 0 0 -1 0 0 5
	0 07-014-3_kitchen_wing_floor_plan_(proposed)_1st_june_2008_stamped.jpg
	 90 90 13050 90 13050 9135 90 9135 90 9

"""

def flip_y_coords_object(bounds, o ):
    _,_,ymin,ymax = bounds
    #print "o = ", o, type(o), o[:,1], (ymax - ymin) - o[:,1]
    o[:,1] = (ymax - ymin) - o[:,1]
    return o
"""
    offset = ( y - ymin )
    new_y = ymax - offset
          = ymax -  ( y - ymin )
          = ( ymax - ymin) - y
"""


def flip_y_coords_dict(bounds,object_dict):
    f = flip_y_coords_object
    my_dictionary = {k: f(bounds, v) for k, v in object_dict.iteritems()}
    return my_dictionary
def plot_fig():

    name = "kitchen_wing_pipes_windows.fig"
    object_dict = read_fig_file(name)
    bounds      = dict_to_bounds(object_dict)
    object_dict = flip_y_coords_dict(bounds,object_dict )
    complete_plot( object_dict )

if __name__ == "__main__":
    plot_fig()


