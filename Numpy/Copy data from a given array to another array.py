import numpy as np
x = np.array([24, 27, 30, 29, 18, 14])
print("Original array:")
print(x)
y = np.empty_like (x)
y[:] = x
print("\nCopy of the said array:")
print(y)
