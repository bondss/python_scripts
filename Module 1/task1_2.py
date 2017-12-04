import sys
import math 

x = float(sys.argv[1])
mu = float(sys.argv[2])
sigma = float(sys.argv[3])

result = (1/(sigma*math.sqrt(2*math.pi)))*math.exp(-((math.pow((x-mu), 2)/2*sigma**2)))

print(result)

