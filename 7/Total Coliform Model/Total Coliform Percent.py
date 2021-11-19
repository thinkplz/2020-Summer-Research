def Percentage(fileName):
    file = open(fileName, "r")
    outfile = open("6N.txt", "w")

    count = 0
    if file.readline() != "":
        for line in file:
            value = line.split(" ")
            strValue = ''.join(value)
            if (float(strValue) > 10000):
                count += 1
    percent = (count/10000) * 100

    outfile.write("Number of data greater than 10000: " + str(count) + "\n")
    outfile.write("Percentage: " + str(percent) + "\n")
    outfile.close()

def main():
    Percentage("6N, Total Coliform.txt")

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()