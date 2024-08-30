import numpy as np
import math

qwerty_dict = {
    '1': {'x': 0, 'y': -1}, '2': {'x': 1, 'y': -1}, '3': {'x': 2, 'y': -1},
    '4': {'x': 3, 'y': -1}, '5': {'x': 4, 'y': -1}, '6': {'x': 5, 'y': -1},
    '7': {'x': 6, 'y': -1}, '8': {'x': 7, 'y': -1}, '9': {'x': 8, 'y': -1},
    '0': {'x': 9, 'y': -1}, 'q': {'x': 0, 'y': 0}, 'w': {'x': 1, 'y': 0},
    'e': {'x': 2, 'y': 0}, 'r': {'x': 3, 'y': 0}, 't': {'x': 4, 'y': 0},
    'y': {'x': 5, 'y': 0}, 'u': {'x': 6, 'y': 0}, 'i': {'x': 7, 'y': 0},
    'o': {'x': 8, 'y': 0}, 'p': {'x': 9, 'y': 0}, 'a': {'x': 0, 'y': 1},
    's': {'x': 1, 'y': 1}, 'd': {'x': 2, 'y': 1}, 'f': {'x': 3, 'y': 1},
    'g': {'x': 4, 'y': 1}, 'h': {'x': 5, 'y': 1}, 'j': {'x': 6, 'y': 1},
    'k': {'x': 7, 'y': 1}, 'l': {'x': 8, 'y': 1}, 'z': {'x': 0, 'y': 2},
    'x': {'x': 1, 'y': 2}, 'c': {'x': 2, 'y': 2}, 'v': {'x': 3, 'y': 2},
    'b': {'x': 4, 'y': 2}, 'n': {'x': 5, 'y': 2}, 'm': {'x': 6, 'y': 2}
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

def levN (s, t, insertion_weight=1, deletion_weight=1, substitution_weight=2):
    try:
        distances = np.zeros((len(s) + 1, len(t) + 1))

        for i in range(len(s) + 1):
            distances[i][0] = i * deletion_weight

        for i in range(len(t) + 1):
            distances[0][i] = i * insertion_weight

        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    distances[i][j] = distances[i - 1][j - 1]
                else:
                    distances[i][j] = min(
                        distances[i - 1][j] + deletion_weight,
                        distances[i][j - 1] + insertion_weight,
                        distances[i - 1][j - 1] + substitution_weight
                    )

        lev_distance = distances[len(s)][len(t)]
        result = (len(s) + len(t) - lev_distance) / (len(s) + len(t))   
        
    except Exception as e:
        if (s == '' or t == ''):
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


def nearest_key_distance(char):
    min_distance = float('inf')
    for key in qwerty_dict:
        distance = qwertyDistance(char, key)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def qwertyN(token1, token2):
    if token1 is None or token2 is None:
        return 0
    
    token1 = token1.lower()
    token2 = token2.lower()

    for token in [token1, token2]:
        for char in token:
            if char not in qwerty_dict:
                raise ValueError(f"Character '{char}' not in qwerty_dict")
            
    total_distance = 0
    for char1, char2 in zip(token1, token2):
        total_distance += qwertyDistance(char1, char2)

    if len(token1) > len(token2):
        for char in token1[len(token2):]:
            total_distance += nearest_key_distance(char)
    elif len(token2) > len(token1):
        for char in token2[len(token1):]:
            total_distance += nearest_key_distance(char)
    
    max_distance = max(len(token1), len(token2)) * 6
    normalized_distance = 1 - (total_distance / max_distance)

    return normalized_distance

def QLev(token1, token2):
    token1 = token1.lower()
    token2 = token2.lower()
    normalized_distance = qwertyN(token1, token2)
    lev = levN(token1, token2)

    result = (normalized_distance + lev) / 2

    return result

def to_vector(word):
    word = word.lower()
    vector = np.zeros((len(word), 2))  
    for i, char in enumerate(word):
        if char in qwerty_dict:
            vector[i] = [qwerty_dict[char]['x'], qwerty_dict[char]['y']]
        else:
            raise ValueError(f"Character '{char}' not in qwerty_dict")
    return vector

def to_vector_flatten(word):
    word = word.lower()
    vector = np.zeros((len(word), 2))  
    for i, char in enumerate(word):
        if char in qwerty_dict:
            vector[i] = [qwerty_dict[char]['x'], qwerty_dict[char]['y']]
        else:
            raise ValueError(f"Character '{char}' not in qwerty_dict")
    return vector.flatten()

def pad_vectors(vector1, vector2):
    max_len = max(len(vector1), len(vector2))
    if vector1.shape[0] < max_len:
        padding = np.zeros((max_len - vector1.shape[0], 2))
        vector1 = np.vstack((vector1, padding))
    if vector2.shape[0] < max_len:
        padding = np.zeros((max_len - vector2.shape[0], 2))
        vector2 = np.vstack((vector2, padding))
    return vector1, vector2


def vectors_penalty(vector1, vector2):
    vector1 = to_vector(vector1)
    vector2 = to_vector(vector2)
    vector1, vector2 = pad_vectors(vector1, vector2)
    min_len = min(len(vector1), len(vector2))
    total_distance = np.linalg.norm(vector1[:min_len] - vector2[:min_len])

    size_difference = abs(len(vector1) - len(vector2))
    total_distance += size_difference

    return total_distance

def aggregate_vector(vector):
    return np.mean(vector.reshape(-1, 2), axis=0)  

def aggr_vectors(vector1, vector2):
    vector1 = to_vector(vector1)
    vector2 = to_vector(vector2)
    aggregated_vector1 = aggregate_vector(vector1)
    aggregated_vector2 = aggregate_vector(vector2)
    return np.linalg.norm(aggregated_vector1 - aggregated_vector2)