def series(n):
    Sum = 0
    i = 1
    while i < n + 1:
        Sum += pow(i,i)
        i += 1
    return Sum

print(series(int(input("Enter n(must be greater than 0):"))))