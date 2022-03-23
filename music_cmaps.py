import os
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

################################################################################

def rgb2cmap(cmapname,ncols):
    cmarray=np.loadtxt(os.path.dirname(os.path.realpath(__file__))+'/RGB/'+cmapname+'.rgb')
    cm=LinearSegmentedColormap.from_list(cmapname,cmarray,N=ncols)
    return cm

kida         = rgb2cmap('kida',128)
manonthemoon = rgb2cmap('manonthemoon',128)
