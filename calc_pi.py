pi = 0

n: int = 20_000_000
n = round(20e6)
x:int = 1
for i in range(n):
	if i%2 == 0:
		pi += 4/x
	else:
		pi -= 4/x

	x += 2

print(pi)
import math
print(math.pi)

# takes about 40 seconds and is accurate for 7 digits with n = 20E6

