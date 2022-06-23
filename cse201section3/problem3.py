def f1(x):
    return x**2

def f2(x):
    return x - x**2


x = int(input("Enter x :"))
print("(f1+f1)(",x,") =", f1(x) + f2(x))
print("(f1f1)(",x,") =", f1(x) * f2(x))