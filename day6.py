import numpy as np
t = int("42686985")
d = int("284100511221341")
ans = []
curr = 0
for b in range(1, t+1):
        if (b)*(t-b) > d:
            curr += 1


print(curr)