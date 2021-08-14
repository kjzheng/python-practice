import math
import argparse

parser = argparse.ArgumentParser(description="Calculate the volume of cylinder")  # A container to hold our argument
parser.add_argument("radius", type=int, help="Radius of cylinder")  # add argument of radius with integer type. This is a positional argument. Type '2' in parameters to enter 2 as radius, the first 2 is always taken as radius
parser.add_argument("height", type=int, help="Height of cylinder")  # add argument of height with integer type. This is a positional argument. Type '2' in parameters to enter 2 as height, the second 2 is always taken as height

# parser.add_argument("-R", "--radius", type=int, help="Radius of cylinder")  # add argument of radius with integer type. This is a optional argument. Type '-R 2' in parameters to enter 2 as radius, position doesnt matter
# parser.add_argument("-H", "--height", type=int, help="Height of cylinder")  # add argument of radius with integer type. This is a optional argument. Type '-H 2' in parameters to enter 2 as height

args = parser.parse_args() # Parse these arguments

def cylinder_volume(radius, height):  # define func volume with 2 arguments
    volume = (math.pi)*(radius**2)*(height)  # cylinder vol (pi)*r^2*h
    return volume

if __name__ == "__main__":
    print(cylinder_volume(args.radius, args.height))




# type "python 'script path' -h" in terminal for the help list
# comment and uncomment the arguments to switch between optional and positional arguments