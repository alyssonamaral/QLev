import numpy as np
import math

qwerty_dict = {
    'q': {'x': 0, 'y': 0}, 'w': {'x': 1, 'y': 0}, 'e': {'x': 2, 'y': 0},
    'r': {'x': 3, 'y': 0}, 't': {'x': 4, 'y': 0}, 'y': {'x': 5, 'y': 0},
    'u': {'x': 6, 'y': 0}, 'i': {'x': 7, 'y': 0}, 'o': {'x': 8, 'y': 0},
    'p': {'x': 9, 'y': 0}, 'a': {'x': 0, 'y': 1}, 's': {'x': 1, 'y': 1},
    'd': {'x': 2, 'y': 1}, 'f': {'x': 3, 'y': 1}, 'g': {'x': 4, 'y': 1},
    'h': {'x': 5, 'y': 1}, 'j': {'x': 6, 'y': 1}, 'k': {'x': 7, 'y': 1},
    'l': {'x': 8, 'y': 1}, 'z': {'x': 0, 'y': 2}, 'x': {'x': 1, 'y': 2},
    'c': {'x': 2, 'y': 2}, 'v': {'x': 3, 'y': 2}, 'b': {'x': 4, 'y': 2},
    'n': {'x': 5, 'y': 2}, 'm': {'x': 6, 'y': 2}
    }

def levenshteinDistance(token1, token2):
    distances = np.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2

    a = 0
    b = 0
    c = 0

    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1 - 1] == token2[t2 - 1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]

                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)] 

def levN (token1, token2):
    try:
        distance = levenshteinDistance(token1, token2)
        sumLen = len(token1) + len(token2)   
        result = distance / sumLen
        
    except Exception as e:
        if (token1 == '' or token2 == ''):
            print('One of the string should not be empty')
        else:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

    return result 

def qwertyDistance (token1, token2):
    token1 = token1.lower()
    token2 = token2.lower()
    try:
        X = (qwerty_dict[token1]['x'] - qwerty_dict[token2]['x']) ** 2
        Y = (qwerty_dict[token1]['y'] - qwerty_dict[token2]['y']) ** 2
        return math.sqrt(X+Y)

    except Exception as e:
        if (len(token1) != 1 or len(token2) != 1):
            print('quertyDistance accepts only the distance between chars')
        else:
            if hasattr(e, 'message'):
                print(e.message)
            else:
                print(e)

def QLev (token1, token2):
    token1List = [*token1]
    token2List = [*token2]
    i = 0
    
    if len(token1List) == len(token2List):
        charX = []
        while i < len(token1List):
            dist = qwertyDistance(token1List[i], token2List[i])
            charX.append(dist)
            i += 1
        sumMin = sum(charX)
    else:
        return 'The string should have the same lengh'
    
    lev = levN(token1, token2)     
    mean = (sumMin + lev) / 2
    sumLen = len(token1) + len(token2)   
    result = mean / sumLen

    if result > 1:
        result = 1

    return result