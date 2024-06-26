def fuzzy_complement(set1):
    result = {}
    for key in set1:
        result[key] = 1 - set1[key]
    return result

set1 = {'a': 0.7, 'b': 0.4, 'c': 0.9}

complement_result = fuzzy_complement(set1)
print("Fuzzy Complement:", complement_result)
