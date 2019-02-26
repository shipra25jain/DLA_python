import imageio
from optparse import OptionParser
parser = OptionParser()
import sys
import numpy as np
usage = "usage: %prog [options] arg1 arg2"

parser.add_option("-f", "--filepath", type="str", help="Input image", dest="inputim", default="dlaoutput.png")
options, arguments = parser.parse_args()
imageMat = imageio.imread(options.inputim)

def convertBinary(imageMat):
	for i in range(len(imageMat)):
		for j in range(len(imageMat)):
			if(imageMat[i][j]==255):
				imageMat[i][j]=1
	return imageMat

def maxdistFromCentroid(imageMat): 
    dist = 0
    cx = 0
    cy = 0
    count = 0
    maxRad = 0
    limit = len(imageMat)
    for i in range(0,limit): 
        for j in range(0,limit):           
            if(imageMat[i][j]==1):
                count = count+1
                cx = cx + i
                cy = cy + j
    cx = int(cx/count)
    cy = int(cy/count)
    for i in range(0,limit):
        for j in range(0,limit):
            if(imageMat[i][j]==1):
                dist = dist + max(abs(cx-i),abs(cy-j))
    dist = (dist/count)**0.5
    return dist
imageMat = convertBinary(imageMat)
maxdist = maxdistFromCentroid(imageMat)
stickiness = 0.837*maxdist - 6.143
print("Estimated stickiness : ", stickiness)