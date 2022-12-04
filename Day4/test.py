import numpy as np
import re
with open("input.py") as fp:
    s1, e1, s2, e2= np.array([re.search(r"(\d+)-(\d+),(\d+)-(\d+)", l).groups() for l in fp.readlines()],dtype=int).T
print("part 1:", np.sum((s1 - s2) * (e1 - e2) <= 0))
#print("part 2:", np.sum((e2 - s1) * (s2 - e1) <= 0))