for row in range(4) :

    for column in range(4):

        hourGlass = (arr[row][column] + arr[row][column+1] + arr[row][column+2]+
        arr[row+1][column+1]+
        arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2])

        if hourGlass > maxGlass :
            maxGlass = hourGlass

print (maxGlass)
