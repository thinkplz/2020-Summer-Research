import random
import scipy
import math
from scipy import stats

outfile = open("5N, Swimmer, Marion, E Coli.txt", "w")
n = 0
while (n < 10000):
  #Generate random percentile
  random_percentile_one = random.uniform(0, 1)

  #Calculate concentration
  concentration = (stats.lognorm.ppf(random_percentile_one, 0.6040282, loc=0, scale= math.exp(3.6920300)))
  #print(concentration)
  X = math.log10(concentration)
  Y = -0.059 + (10.36 * X)
  outfile.write(str(Y) + "\n")

  n += 1

outfile.close()