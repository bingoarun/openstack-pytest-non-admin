def write2file(key,value):
    with open("results.txt", "a") as myfile:
        temp = key + "\t:\t" + value + "\n"
        myfile.write(temp)