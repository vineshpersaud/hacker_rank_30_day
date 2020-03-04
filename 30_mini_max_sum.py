def miniMaxSum(arr):
    minNum = float("infinity")  
    maxNum = float("-infinity") 

    for num in arr :
        total = sum(arr)-num
        if total > maxNum:
            maxNum = total
        if total < minNum:
            minNum = total

    print(minNum,maxNum)