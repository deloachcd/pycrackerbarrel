import numpy as np

t = np.array([[1],
              [0,1],
              [1,0,1],
              [1,0,1,0],
              [0,1,0,0,1]])

str_t = []
for row in t:
    for val in row:
        str_t.append('T' if val == 1 else '.')

tri = \
"""      /^\\
     / {} \\
    / {} {} \\
   / {} {} {} \\
  / {} {} {} {} \\
 / {} {} {} {} {} \\
'-------------'""".format(*str_t)

print(tri)
