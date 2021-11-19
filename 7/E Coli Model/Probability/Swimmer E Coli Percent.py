def Percentage(fileName):
    file = open(fileName, "r")
    outfile = open("6N, Marion.txt", "w")

    count = 0
    if file.readline() != "":
        for line in file:
            value = line.split(" ")
            strValue = ''.join(value)
            if (float(strValue) > 32):
                count += 1
    percent = (count/10000) * 100

    outfile.write("Swimmer highly credible GI symptoms greater than 32: " + str(count) + "\n")
    outfile.write("Percentage: " + str(percent) + "\n")
    outfile.close()

def main():
    Percentage("6N, Swimmer, Marion, E Coli.txt")

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()