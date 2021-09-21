import random
def gcd(a:int,b:int):
    """ General Common Divider """
    assert a>0 and b>0, "Параметры GCD должны быть больше нуля"
    if a==b:
        return a
    elif a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)


def gcd2(a:int,b:int):
    """ Improved General Common Divider """
    #assert a>0 and b>0, "Параметры GCD должны быть больше нуля"
    if b==0:
        return a
    else:
        return gcd2(b,a%b)


for i in range(10):
    a=random.randint(1,1000)
    b=random.randint(1,1000)
    print("a={}\tb={}\tGCD={} | GCD2={}".format(a,b,gcd(a,b),gcd(a,b)))
