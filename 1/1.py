def data_report(fname):
  fxqile = open(fname, "r")
  outfile = open("data_report.txt", "w")
  outfile.write("Data Report"+"\n")
  outfile.write("--------------------"+"\n")

  count_prcp = 0
  count_t = 0
  if file.readline() != "":
    for line in file:
      values = line.split(",")

      if values[7] != '"0.00"':
        corresponding_date = values[6];
        outfile.write(corresponding_date+"\n")
        count_prcp += 1
      
      if values[8] == '"T':
        corresponding_date = values[6];
        outfile.write(corresponding_date+"\n")
        count_t += 1

  outfile.write("--------------------"+"\n")
  outfile.write("Number of days with precipitation greater than 0: " + str(count_prcp) + "\n")
  outfile.write("Number of days with T attribution: " + str(count_t) + "\n")

  file.close()
  outfile.close()

data_report("Los Angeles International Airport 20090101-20101231.csv")
