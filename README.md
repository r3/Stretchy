Stretchy
========

Author: Ryan Roler (ryan.roler@gmail.com)
License: GPL 3
Requires: matplotlib

Description:
Physics tool for showing one implementation of the conservation of energy.

System is a ball with mass 'm' connected to an elastic string with spring
constant 'k'. This ball is moved in a vertical (perpindicular to the floor)
circle about a central point. This tool uses the conservation of mechanical
energy to predict the length of the elastic string given some angle theta.

The formula is viewable in the 'equation.gif' image file and a resultant graph
is viewable in 'r_vs_theta-polar.png'.

If run without options, the program will print out a table of calculated
values. For other options, invoke the program with '-h' or '--help' options
for the following instructions:

    ----------------------------------------------------------------
    
usage: stretchy.py [-h] [--video] [--picture] [--data] [--gravity GRAV]
                   [--spring SPRING] [--length R_NAUGHT] [--mass MASS]
                   [--increment INCREMENT]

Tool for modeling the length of an elastic string with a mass attached to the
end when swung in a cirle perpendicular to the ground.

optional arguments:
  -h, --help            show this help message and exit
  --video, -v           Generate video file of graph (Not implemented)
  --picture, -p         Generate picture file of graph (polar)
  --data, -d            Generate data points
  --gravity GRAV, -g GRAV
                        Acceleration due to gravity (9.81 [m/s^2]
  --spring SPRING, -s SPRING
                        Spring constant of elastic line (0.072375 [N/m])
  --length R_NAUGHT, -r R_NAUGHT
                        Initial length of string (1 [m])
  --mass MASS, -m MASS  Grams of mass hanging from string (5.9 [g])
  --increment INCREMENT, -i INCREMENT
                        Increment used between thetas in calculating length of
                        string (pi/6).

Default behavior is to generate the data points and print them to standard
output

    ----------------------------------------------------------------
