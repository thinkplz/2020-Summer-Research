import random
import scipy
import math
from scipy import stats
#This is a tester, and use `6.6.Day.Without.Rain.ENTEROCOCCUS.File` as the test file

n = 0
while (n < 10):
  # -------------------- Generate random percentile --------------------
  random_percentile_one = random.uniform(0, 1)
  random_percentile_two = random.uniform(0, 1)
  random_percentile_three = random.uniform(0, 1)
  random_percentile_four = random.uniform(0, 1)
  random_percentile_five = random.uniform(0, 1)

  #Calculate concentration
  concentration = (stats.lognorm.ppf(random_percentile_one, 1/0.9335309, loc=0, scale= math.exp(2.3192296)))/100
  
  #------------------------------- I Oral ------------------------------
  #Calculate T_exposure
  T_exposure = stats.rayleigh.ppf(random_percentile_two, loc=0, scale=58.3081/60)
  print(T_exposure)

  #Calculate R_ingestion
  #Use beta distribution instead 
  R_ingestion = stats.triang.ppf(random_percentile_three, (35 - 20)/(50 - 20), loc=20, scale=(50 - 20))
  print(R_ingestion)

  I_oral = T_exposure * R_ingestion

  #------------------------------- D Oral ------------------------------
  D_oral = I_oral * concentration

  #------------------------ Dose Response Model ------------------------
  k = stats.triang.ppf(random_percentile_four, (1442 - 177)/(14427 - 177), loc=177, scale=(14427 - 177))
  psi = stats.triang.ppf(random_percentile_five, (0.2 - 0.1)/(0.3 - 0.1), loc=0.1, scale=(0.3 - 0.1))
  GI_prob = (1 - math.exp((D_oral * -1)/k)) * psi

  n += 1