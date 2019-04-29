import math

'''
Program to find a 3-digit number such that
it is equal to the sum of the factorials
of its digits

e.g. ABC = A! + B! + C!, where ABC is
a concatenation of A, B and C
'''
def findFac():
    for j in range(111, 1000):
        if (j == splitToFacSums(j)):
            print(j)

'''
Splits the number into a sum of factorials of its digits

e.g. 364 -> 3! + 6! + 4!
'''
def splitToFacSums(num):
    splitNum = list(str(num))
    sum = 0
    for i in range(0, len(splitNum)):
        sum += math.factorial(int(splitNum[i]))
    return sum

findFac()
