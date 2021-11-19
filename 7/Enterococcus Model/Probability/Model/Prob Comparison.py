def Comparison(fileSurfer, fileSwimmer):
    outfile = open("Site 6, With Rain.txt", "w")
    surfer_count = helper(fileSurfer)
    swimmer_count = helper(fileSwimmer)
    
    surfer_percent = (surfer_count/10000) * 100
    swimmer_percent = (swimmer_count/10000) * 100

    outfile.write(fileSurfer + " comparing to " + fileSwimmer + "\n")
    outfile.write("-----------------------------------------" + "\n")
    outfile.write("Surfer GI_PROB greater than 0.032: " + str(surfer_count) + "\n")
    outfile.write("Percentage: " + str(surfer_percent) + "\n")
    outfile.write("Swimmer GI_PROB greater than 0.032: " + str(swimmer_count) + "\n")
    outfile.write("Percentage: " + str(swimmer_percent) + "\n")

    outfile.close()

def helper(fileName):
    count = 0
    file = open(fileName, "r")

    if file.readline() != "":
        for line in file:
            value = line.split(" ")
            strValue = ''.join(value)
            if (float(strValue) > 0.032):
                count += 1
    
    file.close()
    return count

def main():
    Comparison("6Y, Surfer, Prob, Enterococcus.txt", "6Y, Swimmer, Prob, Enterococcus.txt")

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  main()