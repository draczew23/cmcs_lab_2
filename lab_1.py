import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
print("hey")

zero = np.matrix([
0,1,1,1,0,
1,0,0,0,1,
1,0,0,0,1,
1,0,0,0,1,
1,0,0,0,1,
0,1,1,1,0
])

one=np.matrix([
0,1,1,0,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0,
0,0,1,0,0
])

two=np.matrix([
1,1,1,0,0,
0,0,0,1,0,
0,0,0,1,0,
0,1,1,0,0,
1,0,0,0,0,
1,1,1,1,1,
])


test_ar = np.random.randint(2, size=(5, 6))
print(test_ar)