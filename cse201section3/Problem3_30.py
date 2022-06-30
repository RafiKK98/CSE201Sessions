A = [1,2,3,4]
B = ['a', 'b', 'c', 'd']

mydict = {
    1 : 'd',
    2 : 'b',
    3 : 'c',
    4 : 'a'
}

def f(i):
    return mydict[i]

def oneToOne():
    outputs = []
    
    for i in A:
        outputs.append(f(i))
    
    return len(set(A)) == len(set(outputs))

def onTo():
    outputs = []
    
    for i in A:
        outputs.append(f(i))
    
    return set(outputs) == set(B)

def oneToOneCorrespondence():
    return oneToOne() and onTo()

print(oneToOne())
print(onTo())
print(oneToOneCorrespondence())
