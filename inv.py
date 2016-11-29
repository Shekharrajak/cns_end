# The inverse of 53 mod 120 is 77

# Working out (we are searching for a value of 1)
# Val (val * n) mod m
# 1   53
# 2   106
# 3   39
# 4   92
# 5   25
# 6   78
# 7   11
# 8   64
# 9   117
# 10  50
# 11  103
# 12  36
# 13  89
# 14  22
# 15  75
# 16  8
# 17  61
# 18  114
# 19  47
# 20  100
# 21  33
# 22  86
# 23  19
# 24  72
# 25  5
# 26  58
# 27  111
# 28  44
# 29  97
# 30  30
# 31  83
# 32  16
# 33  69
# 34  2
# 35  55
# 36  108
# 37  41
# 38  94
# 39  27
# 40  80
# 41  13
# 42  66
# 43  119
# 44  52
# 45  105
# 46  38
# 47  91
# 48  24
# 49  77
# 50  10
# 51  63
# 52  116
# 53  49
# 54  102
# 55  35
# 56  88
# 57  21
# 58  74
# 59  7
# 60  60
# 61  113
# 62  46
# 63  99
# 64  32
# 65  85
# 66  18
# 67  71
# 68  4
# 69  57
# 70  110
# 71  43
# 72  96
# 73  29
# 74  82
# 75  15
# 76  68
# 77  1
# Found it at 77


n=53
m=120

def inv(n,m,working):
    max=0
    val=0
    if (working==True):
        print "Val\t(val * n) mod m"
    while True:
        val = val + 1
        result = (val * n) % m
        if (working==True):
            print str(val)+"\t"+str(result)
        if (result==1):
                break
        if (max>1500):
            return(0)
    return val

if (m<n):
    print "m need to be larger than n"
else:
    print "The inverse of "+str(n)+" mod "+str(m)+ " is " + str(inv(n,m,False))
    print "\nWorking out"
    print "Found it at "+str(inv(n,m,True))
