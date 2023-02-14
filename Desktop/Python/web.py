import math

y=[0.11,0.24,0.27,0.52,1.13,1.54,1.71,1.84,1.92,2.01]
init=0.25
tol=0.000001
err=100000000000000000000000000000
epsilon=0.00001
def weird(x):
    top = 0
    for i in y:
        top += i ** x * math.log(i, math.exp(1))
    bot = 0
    for i in y:
        bot += i ** x
    center = 1 / x
    right = 0
    for i in y:
        right += math.log(i, math.exp(1))
    sum = top / bot - center - right / len(y)
    return sum
def weirdPrime(x):
    prime=(weird(x+epsilon)-weird(x))/epsilon
    return prime
p=0
while tol<err:
    p=init
    init=init-weird(init)/weirdPrime(init)
    err=init-p
    print(init)
print("La réponse à la question a est : " + str(init))
def weirdPrime2(x):
    return ((-weird(x+2*epsilon))+8*weird(x+epsilon)-8*weird(x-epsilon)+weird(x-2*epsilon))/(12*epsilon)

init=0.25
p=0
err=100000000000000000000000000000

while tol<err:
    p=init
    init=init-weird(init)/weirdPrime2(init)
    err=init-p
    print(init)
print("La réponse à la question b est : " + str(init))