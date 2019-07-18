import os

def saveLog(path, *data):
    with open(path, "a") as f:
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][j]) + "\t")
                #print(str(data[i][j]) + "\t", end="")
        f.write("\n")
        #print()

def fileName(f, ext):
	i = 0
	while(os.path.exists(f+str(i) + "." + ext)):
		i = i + 1
	f = f + str(i) + "." + ext
	return f

if __name__ == "__main__":
    f = fileName("log", "txt")
    with open(f, "a") as f:
        pass