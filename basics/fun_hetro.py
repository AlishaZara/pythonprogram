def sumlist(arr):
    sum=0
    for i in arr:
        if type(i)==int:
            sum+=i
    print(sum)
sumlist([1,'a','b',4,5,])
sumlist([5,9,'s'])