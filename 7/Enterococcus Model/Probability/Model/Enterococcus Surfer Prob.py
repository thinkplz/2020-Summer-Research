import random
import scipy
import math
from scipy import stats

outfile = open("5N, Surfer, Prob, Enterococcus.txt", "w")
n = 0
while (n < 10000):
  # -------------------- Generate random percentile --------------------
  random_percentile_one = random.uniform(0, 1)
  random_percentile_two = random.uniform(0, 1)
  random_percentile_three = random.uniform(0, 1)
  random_percentile_four = random.uniform(0, 1)
  
  #------------------------------- D Oral ------------------------------
  #Calculate concentration
  concentration = (stats.lognorm.ppf(random_percentile_one, 1.255004, loc=0, scale= math.exp(2.611828)))/100

  #Calculate I_oral for Surfer
  I_oral = stats.lognorm.ppf(random_percentile_two, 1.80, loc=0, scale= math.exp(3.54))

  #Calculate D_oral
  D_oral = I_oral * concentration

  #------------------------ Dose Response Model ------------------------
  k = stats.triang.ppf(random_percentile_three, (1442 - 177)/(14427 - 177), loc=177, scale=(14427 - 177))
  psi = stats.triang.ppf(random_percentile_four, (0.2 - 0.1)/(0.3 - 0.1), loc=0.1, scale=(0.3 - 0.1))
  GI_prob = (1 - math.exp((D_oral * -1)/k)) * psi
  outfile.write(str(GI_prob) + "\n")
  
  n += 1

outfile.close()