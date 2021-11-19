import random
import scipy
import math
from scipy import stats

outfile = open("5, Swimmer, Without Rain, Enterococcus.txt", "w")
n = 0
while (n < 10000):
  # -------------------- Generate random percentile --------------------
  random_percentile_one = random.uniform(0, 1)
  random_percentile_two = random.uniform(0, 1)
  random_percentile_three = random.uniform(0, 1)
  random_percentile_four = random.uniform(0, 1)
  random_percentile_five = random.uniform(0, 1)

  #Calculate concentration
  concentration = (stats.lognorm.ppf(random_percentile_one, 1.255004, loc=0, scale= math.exp(2.611828)))/100
  #compare this concentration to 1.04 to see if it is greater than 1.04
  #------------------------------- I Oral ------------------------------
  
  T_exposure = stats.rayleigh.ppf(random_percentile_two, loc=0, scale=58.3081/60)
  R_ingestion = (stats.beta.ppf(random_percentile_three, 0.188527, 0.0554375, loc = 0, scale = 1)) * 50
  #Calculate I_oral for Swimmer
  I_oral = T_exposure * R_ingestion

  #------------------------------- D Oral ------------------------------
  D_oral = I_oral * concentration

  #------------------------ Dose Response Model ------------------------
  k = stats.triang.ppf(random_percentile_four, (1442 - 177)/(14427 - 177), loc=177, scale=(14427 - 177))
  psi = stats.triang.ppf(random_percentile_five, (0.2 - 0.1)/(0.3 - 0.1), loc=0.1, scale=(0.3 - 0.1))
  GI_prob = (1 - math.exp((D_oral * -1)/k)) * psi
  outfile.write(str(GI_prob) + "\n")

  #32 per 1000 (0.032)

  n += 1

outfile.close()