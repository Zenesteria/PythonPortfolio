numbers = [10, 15, 3, 7]
k = 25


for i in numbers:
    parentNumber = i

    values = [10,15,3,7]
    sumArray = []

    values.remove(parentNumber)

    for x in values:
        sumNumber = parentNumber + x
        if sumNumber == k:

            hasK = "Yes, the number's there with a value of [%s]"%sumNumber
            break
        else:
            pass
print(hasK)


    
        

    
    
    

     

