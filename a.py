from os import read


w = "dir.txt"
with open(w, "r") as file:
    while(True):
        line = file.readline()
        if(line == ""):
            break
        print(line.strip())
