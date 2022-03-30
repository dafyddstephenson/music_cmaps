import os
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

################################################################################

def rgb2cmap(cmapname,ncols):
    cmarray=np.loadtxt(os.path.dirname(os.path.realpath(__file__))+'/RGB/'+cmapname+'.rgb')
    cm=LinearSegmentedColormap.from_list(cmapname,cmarray,N=ncols)
    return cm

kida          = rgb2cmap('kida',128)
manonthemoon  = rgb2cmap('manonthemoon',128)
punisher      = rgb2cmap('punisher',128)
fullmoonfever = rgb2cmap('fullmoonfever',128)
wastinglight  = rgb2cmap('wastinglight',128)
lemonade      = rgb2cmap('lemonade',128)
spiritualstate= rgb2cmap('spiritualstate',128)
somegirls     = rgb2cmap('somegirls',7)
currents      = rgb2cmap('currents',128)
