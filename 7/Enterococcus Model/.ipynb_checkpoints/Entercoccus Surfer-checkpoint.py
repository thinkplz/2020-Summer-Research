import random
import scipy
import math
from scipy import stats
#This is a tester, and use `6.6.Day.Without.Rain.ENTEROCOCCUS.File` as the test file

list = []
n = 0
while (n < 10):
  # -------------------- Generate random percentile --------------------
  random_percentile_one = random.uniform(0, 1)
  random_percentile_two = random.uniform(0, 1)
  random_percentile_three = random.uniform(0, 1)
  random_percentile_four = random.uniform(0, 1)
  
  #------------------------------- D Oral ------------------------------
  #Calculate concentration
  concentration = (stats.lognorm.ppf(random_percentile_one, 1/0.9335309, loc=0, scale= math.exp(2.3192296)))/100
  
  #Calculate I_oral
  I_oral = stats.lognorm.ppf(random_percentile_two, 1/0.5877867, loc=0, scale= math.exp(1.264127))
  #s : shape parameters, 1/sdlog
  #scale : optional, scale parameter (default=1), exp(meanlog)

  #Calculate D_oral
  D_oral = I_oral * concentration
  list.append(D_oral)

  #------------------------ Dose Response Model ------------------------
  k = stats.triang.ppf(random_percentile_three, (1442 - 177)/(14427 - 177), loc=177, scale=(14427 - 177))
  psi = stats.triang.ppf(random_percentile_four, (0.2 - 0.1)/(0.3 - 0.1), loc=0.1, scale=(0.3 - 0.1))
  GI_prob = (1 - math.exp((D_oral * -1)/k)) * psi
  
  n += 1