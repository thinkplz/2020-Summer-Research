def affected_date(fname):
  file = open(fname, "r")
  outfile = open("Affected Date.txt", "w")
  
  #Construct a 2D array of dates and corresponding precipitations
  date_and_prcp = []
  if file.readline() != "":
    for line in file:
      value = line.split(",")

      temp_array = []
      temp_array.append(value[6])
      temp_array.append(value[7])
      temp_array.append(value[8])

      date_and_prcp.append(temp_array)
      
  #Identify and record affected dates
  affected_date = []
  for i in range (0, len(date_and_prcp) - 3, 1):
    if(date_and_prcp[i][1] != '"0.00"' or date_and_prcp[i][2] == '"T'):
      for j in range (0, 4, 1):
        affected_date.append(date_and_prcp[i+j][0])

  #Get rid of redundancy
  result = []
  for i in range(0, len(affected_date), 1):
    if (affected_date[i] not in result):
      result.append(affected_date[i])
  
  #Record dates in file
  outfile.write("Affected Date Report"+"\n")
  outfile.write("--------------------"+"\n")

  affected_date_count = 0
  for i in range(0, len(result), 1):
    outfile.write(result[i] + "\n")
    affected_date_count += 1

  outfile.write("--------------------"+"\n")
  outfile.write("Number of days affected: " + str(affected_date_count) + "\n")
  
  file.close()
  outfile.close()

affected_date("Los Angeles International Airport 20090101-20101231.csv")
