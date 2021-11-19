def data_reader(fname):
  file = open(fname, "r")
  outfile = open("data_report.txt", "w")

  data = []
  if file.readline() != "":
    for line in file:
      value = line.split(",")

      temp_array = []
      temp_array.append(value[0])
      temp_array.append(value[2])
      temp_array.append(value[3])
      temp_array.append(value[4])
      temp_array.append(value[6])
      temp_array.append(value[7])
      if (value[8] == ""):
        temp_array.append("=")
      else:
        temp_array.append(value[8])

      data.append(temp_array)

  for i in range(0, len(data), 1):
    outfile.write(str(data[i]) + "\n")
  
  file.close()
  outfile.close()

data_reader("CSV SMB 6 Chart.csv")
