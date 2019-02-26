#!/usr/bin/python
import dlaSimulator
from matplotlib import colors
import matplotlib.pyplot as plt
cmap = colors.ListedColormap(['black','white'])
from optparse import OptionParser
parser = OptionParser()
import sys
usage = "usage: %prog [options] arg1 arg2"

parser.add_option("-d", "--dimension", type="int", help="Image dimensions", dest="dimension", default=201)
parser.add_option("-s", "--stickiness", type="float", help="Stickiness factor", dest="stickiness", default=1.0)
parser.add_option("-n", "--nparticles", type="int", help="Number of particles", dest="nparticles", default=5000)
options, arguments = parser.parse_args()
stickiness = options.stickiness
imageSize = options.dimension
nparticles = options.nparticles

if(stickiness<0 or stickiness>1):
	print("invalid value for stickiness!")
	sys.exit()
if(imageSize<1):
	print("invalid value for image dimension!")
	sys.exit()
if(nparticles>(imageSize*imageSize)):
	print("invalid value for number of particles")
	sys.exit()
dls = dlaSimulator.dlaSimulator(imageSize,nparticles,stickiness)
imageMat = dls.simulate()

# plt.title("DLA Cluster", fontsize=20)
# plt.matshow(imageMat, interpolation='nearest',cmap=cmap)
# plt.xlabel("direction, $x$", fontsize=15)
# plt.ylabel("direction, $y$", fontsize=15)
# plt.savefig("dlaoutputimage.png", dpi = 200)
# plt.close()   
from scipy.misc import toimage
im = toimage(imageMat)
im.save("dlaoutput.png")