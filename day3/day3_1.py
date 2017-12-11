actual=[0,0]
positions ={}
position=1
moves=[]
for i in range(1,1000):
    moves.extend([i,i])
x = iter(moves)
for circle in range(1,300):

    for right in range(next(x)):
        actual[0]+=1
        position+=1
        positions[str(position)]=actual[:]
        print("actual for ", position ," is ", actual)
    for up in range(next(x)):
        actual[1]+=1
        position+=1
        positions[str(position)]=actual[:]
        print("actual for ", position ," is ", actual)
    for left in range(next(x)):
        actual[0]-=1
        position+=1
        positions[str(position)]=actual[:]
        print("actual for ", position ," is ", actual)
    for down in range(next(x)):
        actual[1]-=1
        position+=1
        positions[str(position)]=actual[:]
        print("actual for ", position ," is ", actual)
        
print(positions["277678"])
print("distance is ", abs(positions["277678"][0])+abs(positions["277678"][1]))