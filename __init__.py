import os
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

################################################################################

def get_music_cmap(cmapname,ncols):
    ''' 
    Return a colormap from the music_cmaps library
    Parameters:
    -----------
    cmapname (str): The name of the desired colormap
    ncols (int): The number of colors in the returned colormap, quantized from a
                 list of colors stored in a plaintext .rgb file
    Returns:
    -------
    cm (LinearSegmentedColormap): The requested colormap
    '''
    
    cmarray=np.loadtxt(os.path.dirname(os.path.realpath(__file__))+'/RGB/'+cmapname+'.rgb')
    cm=LinearSegmentedColormap.from_list(cmapname,cmarray,N=ncols)
    return cm

kida                      = get_music_cmap('kida',128)
manonthemoon              = get_music_cmap('manonthemoon',128)
punisher                  = get_music_cmap('punisher',128)
fullmoonfever             = get_music_cmap('fullmoonfever',128)
wastinglight              = get_music_cmap('wastinglight',128)
lemonade                  = get_music_cmap('lemonade',128)
spiritualstate            = get_music_cmap('spiritualstate',128)
somegirls                 = get_music_cmap('somegirls',7)
currents                  = get_music_cmap('currents',128)
nodream                   = get_music_cmap('nodream',128)
skadream                  = nodream
donda                     = get_music_cmap('donda',2)
incolour                  = get_music_cmap('incolour',25)
melodrama                 = get_music_cmap('melodrama',128)
godsfavoritecustomer      = get_music_cmap('godsfavoritecustomer',128)
aladdinsane               = get_music_cmap('aladdinsane',128)
dreamland                 = get_music_cmap('dreamland',128)
seeds                     = get_music_cmap('seeds',16)
wonderwhereweland         = get_music_cmap('wonderwhereweland',128)
flowerboy                 = get_music_cmap('flowerboy',128)
awake                     = get_music_cmap('awake',8)
nattydread                = get_music_cmap('nattydread',128)
lover                     = get_music_cmap('lover',128)
awakenmylove              = get_music_cmap('awakenmylove',128)
fragments                 = get_music_cmap('fragments',128)
smash                     = get_music_cmap('smash',128)
littlefictions            = get_music_cmap('littlefictions',128)
hiphopandtheworldwelivein = get_music_cmap('hiphopandtheworldwelivein',128)
elvis                     = get_music_cmap('elvis',128)
iridescence               = get_music_cmap('iridescence',128)
