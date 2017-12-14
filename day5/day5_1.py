def solve(input):
    listOfMoves=[]
    step = 0
    actualIndex=0
    futureIndex=0
    right=0

    for line in input.splitlines():
       listOfMoves.append(int(line))
    right = len(listOfMoves)-1

    while(True):
        futureIndex=actualIndex+listOfMoves[actualIndex]
        if(futureIndex<0 or futureIndex>right):
            step+=1
            break
        else:
            listOfMoves[actualIndex]+=1
            actualIndex=futureIndex
            step+=1
    print(step)




def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()
