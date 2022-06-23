def Series(x):
    Sum = 0
    for i in range(x+1):
        Sum += i**2
    
    return Sum


x = int(input("Enter x :"))
print("The sum upto", x, "term is :", Series(x))

