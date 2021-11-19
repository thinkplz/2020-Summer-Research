def data_reader(fname, location):
  file = open(fname, "r")

  data = []
  if file.readline() != "":
    for line in file:
      value = line.split(",")

      if (value[2] == location):
        temp_array = []
        temp_array.append(value[0])
        temp_array.append(value[2])
        temp_array.append(value[3])
        temp_array.append(value[4])
        temp_array.append(value[6])
        temp_array.append(value[7])
        data.append(temp_array)
  
  file.close()
  return data

def day_with_prcp(fname):
  file = open(fname, "r")
  
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
  rain_day = []
  for i in range (0, len(date_and_prcp) - 3, 1):
    if(date_and_prcp[i][1] != '"0.00"' or date_and_prcp[i][2] == '"T'):
      for j in range (0, 4, 1):
        rain_day.append(date_and_prcp[i+j][0])

  #Get rid of redundancy
  result = []
  for i in range(0, len(rain_day), 1):
    if (rain_day[i] not in result):
      result.append(rain_day[i])

  file.close()
  return result;

def dry_and_storm(data, rain_day):
  outfile_with_rain = open("Day With Rain.txt", "w")
  outfile_without_rain = open("Day Without Rain.txt", "w")

  rain_day_modified = []
  for i in range(0, len(rain_day), 1):
    some_date = ""
    some_date += rain_day[i][6:8]
    some_date += "/"
    some_date += rain_day[i][9:11]
    some_date += "/"
    some_date += rain_day[i][1:5]
    rain_day_modified.append(some_date)

  outfile_with_rain.write("Day With Rain"+"\n")
  outfile_without_rain.write("Day Without Rain"+"\n")

  for i in range(0, len(data), 1):
    if data[i][0] in rain_day_modified:
      outfile_with_rain.write(str(data[i]) + "\n")
    else:
      outfile_without_rain.write(str(data[i]) + "\n")

  outfile_with_rain.close()
  outfile_without_rain.close()

def main():
  data_65 = data_reader("CSV SMB 6 Chart.csv", "SMB-6-05")
  data_66 = data_reader("CSV SMB 6 Chart.csv", "SMB-6-06")
  rain_day = day_with_prcp("Los Angeles International Airport 20090101-20101231.csv")
  dry_and_storm(data_65, rain_day)


if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()
