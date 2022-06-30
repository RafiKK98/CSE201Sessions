U = list(range(1, 101))
A = [1,2,3,4]
B = [3,4,5,6]

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

def compliment(A):
    return difference(U, A)


def theorem():
    return difference(A, B) == intersection(A, compliment(B))

print("A - B = A ∩ B' ", theorem())