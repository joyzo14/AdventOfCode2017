def solve(input):
    count = 0
    numberOfLines = 0


    for line in input.splitlines():
        numberOfLines += 1
        newline = line.split()
        sortedList = []
        for element in newline:
            sortedList.append(''.join(sorted(list(element))))
        for element in sortedList:
            if sortedList.count(element) > 1:
                count+=1
                break
    print (numberOfLines-count)



def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()
