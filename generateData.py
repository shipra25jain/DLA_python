#!/usr/bin/python
import dlaSimulator
import numpy as np
import random
import pandas as pd
dsize = 40
image_size = 201
nparticles = np.random.randint(500,600,dsize)*10
stickiness = np.random.uniform(0,1,dsize)

# Returns max radius of cluster, L2 or root mean square distance of 
# all white pixels from the cluster centroid and max distance max(|x-c|,|y-c|)of white pixel from cluster centroid
def distRadFromCentroid(imageMat): 
    dist = [0,0,0]
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
                maxRad = max(((cx-i)**2 + (cy-j)**2)**0.5, maxRad)
                dist[0] = dist[0] + max(abs(cx-i),abs(cy-j))
                dist[1] = dist[1] + (cx-i)**2 + (cy-j)**2
    dist[0] = (dist[0]/count)**0.5
    dist[1] = (dist[1]/count)**0.5
    dist[2] = maxRad/count
    return dist

# Returns Sum of number of neighbours that every pixel in cluster has
def NumOfNeighbour(imageMat): 
	n = pixelsinCluster(imageMat)
	neighbour = 0
	dim = len(imageMat)
	for i in range(dim):
		for j in range(dim):
			if imageMat[i][j] == 1:
				neighbour += pixelsinNeighbour(imageMat, i, j)
	numneighbour = float(neighbour) / n
	return numneighbour
	
def pixelsinCluster(imageMat): # Returns number of pixels in cluster
	count = 0
	for i in range(len(imageMat)):
		for j in range(len(imageMat)):
			if(imageMat[i][j] == 1):
				count += 1
	return count

def pixelsinNeighbour(imageMat, x, y): # Returns number of white pixels around given pixel
	neighbour = 0
	dim = len(imageMat)
	sx = [-1, -1, 0, 1, 1, 1, 0, -1]
	sy = [0, 1, 1, 1, 0, -1, -1, -1]
	for xx, yy in zip(sx,sy):
		if 0 <= x+xx < dim and 0 <= y+yy < dim :
			if imageMat[x+xx][y+yy] == 1:
				neighbour += 1
	return neighbour


d = {'stickiness':np.zeros(dsize),'nparticles':np.zeros(dsize),'maxdistance':np.zeros(dsize), 'L2distance':np.zeros(dsize), 'maxradius':np.zeros(dsize), 'numneighbour':np.zeros(dsize)}
df = pd.DataFrame(data=d)
ds = 0
for npart, st in zip(nparticles, stickiness):
    count = 0
    dls = dlaSimulator.dlaSimulator(image_size,npart,st)
    imageMat = dls.simulate()	
    print("\nSimulation Over ; Analysis starts \n")
    numneigh = NumOfNeighbour(imageMat)
    distRad = distRadFromCentroid(imageMat)
    print("avgNeighbor ",numneigh)
    print("maxDist ", distRad[0])
    print("L2Dist ", distRad[1])
    print("maxRad ", distRad[2])
    df.loc[ds]["stickiness"]= st
    df.loc[ds]["nparticles"]= npart
    df.loc[ds]["maxdistance"]= distRad[0]
    df.loc[ds]["L2distance"]= distRad[1]
    df.loc[ds]["maxradius"]= distRad[2]
    df.loc[ds]["numneighbour"]=numneigh
    ds = ds +1
df.to_csv("dataforanalysis.csv")




