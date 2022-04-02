# music_cmaps
Music-influenced colormaps in Python/plaintext RGB, from https://twitter.com/music_cmaps

## Install:
Pull this repo to somewhere on your Python path, making sure the directory name matches the repo name `music_cmaps`. 
Use is then as simple as `import music_cmaps` with, e.g. `cmap=music_cmaps.darksideofthemoon`:

## Example:
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
