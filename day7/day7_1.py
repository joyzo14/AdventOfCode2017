def solve(input):
    count = 0
    listOfRightValues = [] #list of values after arrow "->"
    listOfValues = [] #list of all values

    for line in input.splitlines():
        a = line.replace(',', '').split() #replace all commas with dot
        if len(a)> 2:
            listOfRightValues.extend(a[3:])
        listOfValues.append(a)

    for line in listOfValues:
        if(line[0] not in listOfRightValues):
            print(line[0])

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)

if __name__ == '__main__':
    main()