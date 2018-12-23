
newLine = list()
with open('output.txt', 'r') as f:
    for line in f.readlines():
        # newLine.append(line.replace('m',' '))
        print(line.replace('m',' ').replace('\n',''))