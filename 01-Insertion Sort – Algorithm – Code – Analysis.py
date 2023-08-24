myList = [9,5,10,8,4]

def insertionsort(x):
    for i in range(1, len(x)):
        key = x[i]
        j = i-1
        
        while j >= 0 and key < x[j]:
            x[j+1] = x[j]
            j -=1 
        x[j+1] = key
    return x
        
print (insertionsort(myList))

#the output is: [4, 5, 8, 9, 10] 
