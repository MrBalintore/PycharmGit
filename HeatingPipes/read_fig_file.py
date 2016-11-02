import numpy as np
def text_to_numpy(text):
                numbers = map ( float,  text.split() )
                n_points = len(numbers) / 2
                list_2d = [ [ numbers[0 + 2 * i] ,  numbers[1 + 2 * i] ] for i in range(n_points)]
                array = np.array(list_2d)
                return array
def read_fig_file(file_name):
    #print "tring to open file"
    name_terms = []
    object_dict = {}
    cumulated_lines = []
    object_name    = ""
    all_lines = open(file_name).readlines()
    index = 0
    for line in all_lines:
        if line.startswith("#") and ( not line.startswith("#FIG") ):
            if ( cumulated_lines != [] ) and ( object_name != "" ):
                #print "cumulated_lines = ",cumulated_lines
                text = "".join(cumulated_lines[1:])
                #numbers = map ( float,  text.split() )
                #n_points = len(numbers) / 2
                #list_2d = [ [ numbers[0 + 2 * i] ,  numbers[1 + 2 * i] ] for i in range(n_points)]
                #array = np.array(list_2d)
                object_dict[object_name] = text_to_numpy(text)
                #print "numbers = ", numbers, array

            name_terms = (line.split())[1:]
            object_name = " ".join(name_terms)
            #print "NAME = ", object_name
            cumulated_lines = []
        else:
            cumulated_lines.append(line)
        if ".jpg" in line:
            fields = line.split()
            file_name = "".join(fields[1:])
            #print "file_name = ",file_name
            text   = all_lines[index + 1]
            object_dict[file_name] = text_to_numpy(text)

        index = index + 1
        #print line
        #print "--------------------"
    return object_dict
"""
   goal for today
   draw kitchen wing on screen with image
"""
def main():
    name = "kitchen_wing_pipes_windows_0.fig"
    object_dict = read_fig_file(name)
    print object_dict

main()
