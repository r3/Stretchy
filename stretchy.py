from math import pi, cos, sin, sqrt

import numpy
from matplotlib import pyplot

# Given (TEMP)
GRAV = 9.81  # [m/s^2]
R_NAUGHT = 1  # [m]
MASS = 5.9  # [g]
SPRING = 0.072375  # [N/m]
INCREMENT = pi / 6  # Rads

# These two lists will keep the r and theta values for each point, therefore
# the first point will be (r_vals[0], theta_vals[0])
# Things are done this way because of the pyplot.polar signature
r_vals = []
theta_vals = []
for theta in numpy.arange(0, 2 * pi, INCREMENT):
    # The following 'quad_' prefixed vars are for use in the quadratic formula
    quad_a = SPRING / 2 * cos(theta)
    quad_b = (SPRING / 2 + MASS * GRAV / 2 * sin(theta) - R_NAUGHT
              * MASS * SPRING / 2 * cos(theta) + MASS * GRAV * cos(theta))
    quad_c = -SPRING * R_NAUGHT / 2 - 3 * MASS * GRAV * R_NAUGHT / 2

    # Uses the previous vars in the quadratic formula (positive part)
    # (-b + sqrt(b^2 - 4ac))/(2a)
    stretch_length = (
        -quad_b + sqrt(quad_b ** 2 - 4 * quad_a * quad_c)) / (2 * quad_a)

    #r_vals.append(stretch_length + R_NAUGHT)
    r_vals.append(stretch_length)
    theta_vals.append(theta)

print("(r, theta)")
for x, y in zip(r_vals, theta_vals):
    print("({}, {})".format(x, y))

# Plot the points
pyplot.polar(r_vals, theta_vals, 'bo-')
pyplot.show()
