def saveLog(path, *data):
    with open(path, "a") as f:
        for i in range(len(data)):
            for j in range(len(data[i])):
                f.write(str(data[i][j]) + "\t")
                print(str(data[i][j]) + "\t", end="")
        f.write("\n")
        print()

def fileName(f):
	i = 0
	while(os.path.exists(f+str(i) + ".txt")):
		i = i + 1
	f = f + str(i) + ".txt"
	return f

if __name__ == "__main__":
    data1 = [1.0, 2.0, 3.0]
    data2 = [10, 20, 30]
    saveLog("log.txt", data1, data2)