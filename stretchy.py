import argparse
from math import pi, cos, sin, sqrt

import numpy
from matplotlib import pyplot


def generate_points(increment, grav, r_naught, mass, spring):
    """Provides a generator of points in polar coordinates

    Based on the following equation (latex markup):

        $r^2\left(\frac{k}{2}\Cos(\theta)\right)+
         r\left(\frac{k+mg}{2}\sin(\theta)-
            \frac{r_0mk}{2}\Cos(\theta)+mg\Cos(\theta)\right)+
          \left(-\frac{kr_0-3mgr_0}{2}\right)$
    """
    for theta in numpy.arange(0, 2 * pi, increment):
        quad_a = spring / 2 * cos(theta)
        quad_b = (spring / 2 + mass * grav / 2 * sin(theta) - r_naught
                  * mass * spring / 2 * cos(theta) + mass * grav * cos(theta))
        quad_c = -spring * r_naught / 2 - 3 * mass * grav * r_naught / 2

        # Uses the previous vars in the quadratic formula (positive part)
        # (-b + sqrt(b^2 - 4ac))/(2a)
        stretch_length = (
            -quad_b + sqrt(quad_b ** 2 - 4 * quad_a * quad_c)) / (2 * quad_a)

        yield stretch_length + r_naught, theta


def print_points(points):
    """Display points numerically to standard output"""
    print("(r, theta)")
    for x, y in points:
        print("({}, {})".format(x, y))


def display_picture(points):
    """Graphs the points given on a polar coordinate grid"""
    r_vals = []
    theta_vals = []
    for r, theta in points:
        r_vals.append(r)
        theta_vals.append(theta)

    pyplot.polar(r_vals, theta_vals, linestyle='solid', marker='o')
    pyplot.show()


def display_video(points):
    """Produces an animated version of graph produced by 'display_picture'"""
    raise NotImplementedError("This feature is not yet implemented")


def main(args):
    dispatch = {'picture': display_picture, 'video': display_video,
                'data': print_points}
    points = generate_points(args.increment,
                             args.grav,
                             args.r_naught,
                             args.mass,
                             args.spring)

    for arg_name, func in dispatch.items():
        if getattr(args, arg_name):
            func(points)
            break
    else:
        dispatch.get('data')(points)


# Handle command line args
parser = argparse.ArgumentParser(description="""Tool for modeling the length
        of an elastic string with a mass attached to the end when swung in a
        cirle perpendicular to the ground.""", epilog="""Default behavior is
        to generate the data points and print them to standard output""")

parser.add_argument('--video', '-v', help="Generate video file of graph",
                    default=False, action='store_const',
                    const=True)
parser.add_argument('--picture', '-p', help="Generate picture file of graph",
                    default=False, action='store_const',
                    const=True)
parser.add_argument('--data', '-d', help="Generate data points (polar)",
                    default=False, action='store_const',
                    const=True)

parser.add_argument('--gravity', '-g', default=9.81, type=int, dest='grav',
                    help="Acceleration due to gravity (9.81 [m/s^2]")
parser.add_argument('--spring', '-s', default=0.072375, type=int,
                    help="Spring constant of elastic line (0.072375 [N/m])")
parser.add_argument('--length', '-r', default=1, type=int, dest='r_naught',
                    help="Initial length of string (1 [m])")
parser.add_argument('--mass', '-m', default=5.9, type=int,
                    help="Grams of mass hanging from string (5.9 [g])")

parser.add_argument('--increment', '-i', default=pi / 6, type=int,
                    help="""Increment used between thetas in calculating
                    length of string (pi/6).""")

args = parser.parse_args()
main(args)
