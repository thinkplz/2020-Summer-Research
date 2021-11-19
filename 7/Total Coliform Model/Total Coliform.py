import random
import scipy
import math
from scipy import stats

outfile = open("6Y, Total Coliform.txt", "w")
n = 0
while (n < 10000):
  #Generate random percentile
  random_percentile_one = random.uniform(0, 1)

  #Calculate concentration
  concentration = (stats.gamma.ppf(random_percentile_one, 0.833984405, loc=0, scale= math.exp(0.002794455)))
  #print(concentration)
  outfile.write(str(concentration) + "\n")

  n += 1

outfile.close()