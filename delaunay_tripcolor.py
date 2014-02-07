import matplotlib.delaunay as triang
import matplotlib.tri as tri
import matplotlib.pyplot as plt

import pylab
import numpy as np
from random import choice
from math import pi

ignore_list = ["LUTSIZE","ScalarMappable","cbook","cmap_d","cmapname","colors","datad","get_cmap","ma","mpl","np","os","register_cmap","revcmap","spec","spec_reversed",]
color_lists = [i for i in dir(plt.cm) if i[0] != '_' and i not in ignore_list]

fi = open("sample.txt",'r')
x = []
y = []
for line in fi.readlines():
    i,j = eval(line)
    x.append(i)
    y.append(j * -1) # -1 Flips the Image Right-side up
x = np.array(x)
y = np.array(y)
t = tri.Triangulation(x, y)
cens,edg,tri,neig = triang.delaunay(x,y)

# Need to determine some real numbers for angles and radii
temp = []
for i in range(1, len(x)/2):
    if len(x) % i == 0: temp.append(i)

n_angles = temp[-1]
n_radii = len(x) / n_angles
min_radius = 0.25
radii = np.linspace(min_radius, 0.95, n_radii)

angles = np.linspace(0, 2*pi, n_angles, endpoint=False)
angles = np.repeat(angles[...,np.newaxis], n_radii, axis=1)
angles[:,1::2] += pi/n_angles
z = (np.cos(radii)*np.cos(angles*3.0)).flatten()

for color in color_lists:
    try:
        print color
        color="rainbow"
        plt.figure()
        plt.gca().set_aspect('equal')
        plt.tripcolor(t, z, shading='flat', cmap=color)
        plt.axis('off')
        plt.savefig("colors/%s.png" % color, bbox_inches='tight', transparent=True)
        plt.show()
        break
    except:
        print "\tError"
