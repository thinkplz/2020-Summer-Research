import random
import scipy
import math
from scipy import stats

outfile = open("5N, Swimmer, Conc, Enterococcus.txt", "w")
n = 0
greater_than_count = 0
temp_list = []

while (n < 10000):
  # -------------------- Generate random percentile --------------------
  random_percentile_one = random.uniform(0, 1)

  #Calculate concentration
  concentration = (stats.lognorm.ppf(random_percentile_one, 1.255004, loc=0, scale= math.exp(2.611828)))/100
  #compare this concentration to 1.04 to see if it is greater than 1.04
  if (concentration > 1.04):
    greater_than_count += 1
  
  temp_list.append(str(concentration))

  n += 1

outfile.write(str(greater_than_count) + " concentration(s) is/are greater than 1.04" + "\n")
outfile.write("----------------------------------------"+"\n")
for i in range(0, len(temp_list), 1):
  outfile.write(temp_list[i] + "\n")

outfile.close()
