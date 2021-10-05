def selec( itemsList ):
    n = len( itemsList )
    for i in range( n - 1 ):
        minVal = i

        for j in range( i + 1, n ):
            if itemsList[j] < itemsList[minVal] :
                minVal = j

        if minVal!= i :
            temp = itemsList[i]
            itemsList[i] = itemsList[minVal]
            itemsList[minVal] = temp

    return itemsList


l = [101,6,9,33,3,-78]

print(selec(l))
