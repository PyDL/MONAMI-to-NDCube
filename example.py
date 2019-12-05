#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Name: example

@author: Jiajia Liu

Description: example script for monami2ndcube

"""
__author__ = 'Jiajia Liu'
__copyright__ = 'Copyright 2019, The Solar Physics and Space Plasma ' + \
                'Research Center (SP2RC)'
__license__ = 'GPLv3'
__version__ = '1.0'
__maintainor__ = 'Jiajia Liu'
__email__ = 'jj.liu@sheffield.ac.uk'

# There are two ways to convert a potential field extrapolation result to
# NDCube (see https://docs.sunpy.org/projects/ndcube/en/stable/ndcube.html)

# Magnetic field observation
# The example fits file contains the LOS magnetic field observations by
# SDO/HMI on 2011-02-11 00:00:26.90 UT
obs = 'example.fits.gz'

# There first way is to use the output of MONAMI
# (https://github.com/komabi/MONAMI-Mapping-Of-Non-potentiAl-Magnetic-fIeld)
pf = 'example.sav'

# import the library
from monami2ndcube import generate_ndcube

# Generate NDCubes
bxcube, bycube, bzcube = generate_ndcube(obs, pf)

# The second way is to do the magnetic field extrapolation using the Python
# code. Uncomment the following line to run the code
# bxcube, bycube, bzcube = generate_ndcube(obs, nz=11)

# Now let's use some common functions of NDCube

# print the dimension
print(bzcube.dimensions)

# print physical types
print(bzcube.world_axis_physical_types)

# print out the coordination information
print(bzcube.axis_world_coords)

# get the real world coordinates of the NDCube
from astropy import units as u
lon = bzcube.axis_world_coords('lon')
lat = bzcube.axis_world_coords('lat')
z = bzcube.axis_world_coords('HPRZ')

# slicing the cube using pixels
temp = bzcube[5, :, :]

# show the image
temp.plot()

# More examples of using NDCube can be found in the documentations for NDCube
# https://docs.sunpy.org/projects/ndcube/en/stable/ndcube.html