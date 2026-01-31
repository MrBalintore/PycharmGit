from math import sqrt
def calculate_kitchen():
    all = 0
    far = 508
    left = 390
    right = 197 + 249
    diagonal = 90
    near = 222 + 369
    straight_far = far + diagonal / sqrt(2)
    left_far = left  + diagonal / sqrt(2)
    all = left + right + near + far
    return all

def calculate_bedroom():
    far = 420
    diagonal = 78
    right = 380
    straight_far = far + diagonal / sqrt(2.0)
    straight_right = right + diagonal / sqrt(2.0)
    near = 435
    left = 169 + 52 + 14 + 97 + 249
    straight_left = 169 + 14 + 249

    all = far + diagonal + right + near + left
    return all

def calculate_living_room():
    near_wall = (265 + 318)
    far_wall = 350 + 190
    # near wll 43cm longer due to small hallway
    left_wall = 434
    right_wall = 250 + 69 + 14 + 116 + 173
    straight_right_wall = 250 + 14 + 173
    # straight_right_wall 3 cm bigger than left wall
    all = near_wall + far_wall + left_wall + right_wall
    return all

def main():

    living = calculate_living_room()
    bedroom = calculate_bedroom()
    hampshire_coving_in_m = (living + bedroom) / 100.0
    gothic_coving_in_m = ( calculate_kitchen() ) / 100.0

    print(f"gothic_coving_in_m={gothic_coving_in_m}")
    print(f"hampshire_coving_in_m={hampshire_coving_in_m}")

    print(f"gothic_coving_sections={gothic_coving_in_m/3.0}")
    print(f"hampshire_coving_sections={hampshire_coving_in_m/3.0}")
if __name__ == "__main__":
    main()


