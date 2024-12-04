"""
1
"""

d = {"Alan": 7, "Bob": 3, "Ben": 5, "Joe": 2, "Zoe": 8}
print(d)

"""
2
"""
for key in d:
    print(key, d[key]**2)

"""
3
"""
def somme(d):
    s = 0
    for key in d:
        s += d[key]
    return s

print(somme(d))

"""
4
"""

def moy(d):
    s = somme(d)
    return s/len(d)

print(moy(d))

"""
5
"""

def argmin(d):
    min = float('inf')
    for i in d:
        if d[i] < min:
            min = d[i]
            toReturn = i
    return toReturn

print(argmin(d))

"""
6
"""

def carres(d):
    e = {}
    for i in d:
        e.update({i: d[i]**2})
    return e

print(carres(d))

"""
7
"""

def dicocon(d, o):
    e = {}
    for i in d:
        e.update({i: o})
    return e

print(dicocon(d, 0))

"""
8
"""

e = {'Alan': 5, 'Malo': 4, 'Joe': 8, 'Nina': 6}
print(e)

"""
9
"""
def ajout(d, e):
    temp = {}
    n = 0
    for i in d:
        if i in e:
            print(i, e[i])
            temp.update({i: e[i]})
        else:
            temp.update({i: d[i]})
    for j in e:
        if j in d:
            None
        else:
            print('uwu')
            temp.update({j: e[j]})

    return temp
print(ajout(d, e))

