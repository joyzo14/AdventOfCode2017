def solve(input):
    blocks = input.split()
    blocks = list(map(int, blocks))  #map list of strings to integeres
    listofBanks=[] #lists of blocks after each iteration
    bufferOfBlocks = 0 #number of block to distribute
    index = 0 #current index
    indexOfMax = 0 #indexes of max number in current list
    redistributionCycles = 0 #number of cycles before infinite loop
    listofBanks.append(blocks[:]) #append first list of block into bank

    while (True):
        m = max(blocks) #value of max block in list
        indexOfMax = [i for i, j in enumerate(blocks) if j == m] #indexes of max number of blocks in list
        bufferOfBlocks = blocks[indexOfMax[0]] #insert number first max value of blocks
        blocks[indexOfMax[0]] = 0 #deleted all blocks in position of first max value of blocks
        index = indexOfMax[0] #index of first max value of current blocks
        for i in range(bufferOfBlocks): #iterate so many time as number of blocks in buffer
            index+=1
            if(index==(len(blocks))): #if index is out of range of blocks, change it to the first index
                index-=len(blocks)
            blocks[index]+=1
        redistributionCycles +=1
        print(blocks)
        listofBanks.append(blocks[:]) # append current set of block into bank
        if listofBanks.count(blocks) > 1: # if two equal blocks are in list, break the cycle
            break
    print(redistributionCycles)

def main():
    with open('textfile.txt', 'r') as f:
        fileinput = f.read()
        solve(fileinput)


if __name__ == '__main__':
    main()
