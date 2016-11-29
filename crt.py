# n = 3,5,7, A = 2,3,2
# GCD of N values: 1
# Result (x) is: 23

# x mod 3=2
# x mod 5=3
# x mod 7=2


nval = [3,5,7]
aval = [2,3,2]

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1

    while a > 1:
    try:
            q = a / b
            a, b = b, a%b
            x0, x1 = x1 - q * x0, x0
    except:
        print "Bad N values (check no common factors in N vals)"
        return 0
    if x1 < 0: x1 += b0
    return x1

def gcd(L):
    return reduce(fractions.gcd, L)

n = nval
a = aval
g = gcd(nval)
print "GCD of N values: "+ str(g)
if (g>1):
    print "Cannot compute - check your N values for a common factor"
else:
    print "Result (x) is: "+str(chinese_remainder(n, a))+"\n"
    count=0
    for str1 in nval:
        print "x mod "+str(str1)+"="+str(aval[count])
        count=count+1
