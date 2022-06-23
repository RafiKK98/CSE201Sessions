def union(A, B):
    C = A.copy()
    for item in B:
        if item not in A:
            C.append(item)
    return C

def intersection(A, B):
    C = []
    for item in A:
        if item in B:
            C.append(item)
    return C

def difference(A, B):
    C = A.copy()
    for item in A:
        if item in B:
            C.remove(item)
    return C

def symmetric_difference(A, B):
    return difference(union(A, B), intersection(A, B))

X = [1, 2, 3, 4]
Y = [3, 4, 5, 6]
print(union(X, Y))
print(intersection(X, Y))
print(difference(X, Y))
print(symmetric_difference(X, Y))
