import math
N = int(raw_input())
print math.factorial(N)
import itertools
arr = []
for i in range(1,N+1):
	arr.append(i)
ans = list(itertools.permutations(arr))
for x in ans:
	for i in range(0,N):
		print x[i],
	print ""