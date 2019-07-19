import os
import linecache

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

def phaseCheck(path):
    num_lines = sum(1 for line in open(path))
    lastLine = linecache.getline(path, num_lines)
    if not lastLine:
        return 0
    phase = lastLine[0]
    linecache.clearcache()
    return phase


if __name__ == "__main__":
    f = fileName("log", "txt")
    with open(f, "a") as f:
        pass