import numpy as np
import math

me = {2, 3, 4, 5, 6, 7}
print(me)
me = np.array(list(me))
print(me)
print(me.mean())
print(math.ceil(me.mean()))
print(math.floor(me.mean()))