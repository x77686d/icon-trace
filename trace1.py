import icon_trace

icon_trace.start()

def main():
    print(fact(int(sys.argv[1])))


def fact(n):
    return 1 if n == 1 else n * fact(n-1)

def count_nickels(cup):
    x = 5
    if cup == []:
        return 0
    elif cup[0] == 5:
        return 1 + count_nickels(cup[1:])
    else:
        return count_nickels(cup[1:])

        
def sum_rec(L):
    if L == []:
        return 0
    else:
        return L[0] + sum_rec(L[1:])

def f(c,a,b):
    pass

class X:
    def __init__(self,value):
        self._value = value

    def __str__(self):
        return "X({})".format(value)


#f([1,2,3],10,20)
#sum_rec([5])
#sum_rec([5,3,1,2])
print(fact(2))

print(count_nickels([5,1,9,2,7,3,5]))

x1 = X(30)

f(x1,10,20)
