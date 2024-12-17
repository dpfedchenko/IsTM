import numpy as np
from assign import hx, hy # type: ignore

arx = np.arange(-1 + hx / 2, 1, hx)
ary = np.arange(.4, 2.4, hy)

midx = arx[0] + (arx[-1] - arx[0])/2
midy = ary[0] + (ary[-1] - ary[0])/2

xv, yv = np.meshgrid(arx, ary)
pairs = np.stack((xv.ravel(), yv.ravel()), axis=-1)