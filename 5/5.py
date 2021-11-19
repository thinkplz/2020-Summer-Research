def data_reader(fname):
  file = open(fname, "r")
  print(fname[:-4])
  TC_file = open(fname[:-4] + " TOTAL COLIFORM File.txt", "w")
  ECOLI_file = open(fname[:-4] + " E COLI File.txt", "w")
  ENTER_file = open(fname[:-4] + " ENTEROCOCCUS File.txt", "w")

  if file.readline() != "":
    for line in file:
      value = line.split(",")
      if value[2] == " 'TOTAL COLIFORM (CS)'":
        TC_file.write(line)
      elif value[2] == " 'E COLI (CS)'":
        ECOLI_file.write(line)
      elif value[2] == " 'ENTEROCOCCUS (CS)'":
        ENTER_file.write(line)
  
  file.close()
  TC_file.close()
  ECOLI_file.close()
  ENTER_file.close()

data_reader("6-6 Day With Rain.txt")
