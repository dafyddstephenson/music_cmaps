# music_cmaps
Music-influenced colormaps in Python/plaintext RGB, from https://twitter.com/music_cmaps

## Install
Pull this repo to somewhere on your Python path, making sure the directory name matches the repo name `music_cmaps`. 

## Use
To use a colormap "as is", one can either `import music_cmaps` and then point to it (as in the below example) or import the individual colormap, e.g., `from music_cmaps import darksideofthemoon`. 

There is also a function `get_music_cmap` which acts similarly to `matplotlib.cm.get_cmap`, accepting the colormap name (as a string) along with an integer number of desired colors, e.g., `CMAP=music_cmaps.get_music_cmap('batoutofhell',64)`. If this exceeds the existing number of colors, linear interpolation is used.

## Example
```
import numpy as np
import music_cmaps
import matplotlib.pyplot as plt


X,Y=np.meshgrid(np.linspace(0,2*np.pi,100),np.linspace(0,2*np.pi,100))
fig,ax=plt.subplots()
p=ax.contourf(X,Y,np.sin(X)*np.sin(Y),32,cmap=music_cmaps.spiritualstate,vmin=-1,vmax=1)
ax.contour(X,Y,np.sin(X)*np.sin(Y),32,colors='k',linewidths=0.3)
fig.colorbar(p,ax=ax)
fig.show()
```

## Previews:
![Preview of available colormaps](https://github.com/2wheelsgood/music_cmaps/blob/master/preview1.png)?raw=true)
