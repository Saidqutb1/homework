#1
# Domla, Outputni vato beribti
def birinchisi(a, b):
    a1 = set(a)
    b1 = set(b)
    a1.symmetric_difference_update(b1)
    if a1:
         return sum(a1) / len(a1)
    else:
        return 0

# a = [1, 1, 3, 4, 4, 5, 6, 7]
# b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# print(birinchisi(a, b))

#2
def ikkinchisi(a, b):
    return [b + str(i) for i in a]

# a = [1, 4, 3, 9]
# b = 'RM'
# print(ikkinchisi(a, b))

#3
def uchinchisi(a):
    return max(a)

# a = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(uchinchisi(a))

#4
def tortinchisi(a):
    s = 0
    for i in a:
        if isinstance(i, (int, float)):
            s += 1
    return s

# a = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# print(tortinchisi(a))

#5
def beshinchi_vazifa(a):
    s = max(set(a), key = a.count)
    count = a.count(s)
    return f"{s} --> {count} marta"

# a = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
# print(beshinchi_vazifa(a))

#6
def oltinchi_vazifa(a):
    n = len(a)
    for i in range(n - 1, -1, -1):
        if a[i] < 9:
            a[i] += 1
            return a
        else:
            a[i] = 0
    return [1] + a

# a = [1, 2, 3]
# a = [9]
# a = [9, 9, 9, 9]
# print(oltinchi_vazifa(a))



#7
# s = []
# a = int(input('Son kiriting: '))
# while a > 0:
#     s.append(int(input("List uchun son kiriting: ")) ** 2)
#     a -= 1
# print(s)

#8
def sakizinchi_vazifa(a, b):
    s = []
    for i in range(min(len(a), len(b))):
        s.append(str(b[i]) + str(a[i]))
    return s

# a = [1, 4, 3, 9]
# b = ['chelsea', 'real', 'barca', 'MU']
# print(sakizinchi_vazifa(a, b))

#9
def toqizinchi_vazifa(a, b):
    a1 = set(a)
    b1 = set(b)
    s = a1.intersection(b1)
    return max(s)

# a = [1, 1, 3, 4, 4, 5, 6, 7]
# b = [0, 1, 2, 3, 4, 4, 5, 7, 8]
# print(toqizinchi_vazifa(a, b))

#10
#Fibonacci sonlarni xisoblaydigan funksiya
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = int(input('-->'))
# print(fibonacci(n))

def sas_fibonacci(a):
    s = [1, 2]
    while len(s) < a:
        d = s[-1] + s[-2]
        s.append(d)
    return s[:-1]

# a = int(input("--->"))
# print(sas_fibonacci(a))






