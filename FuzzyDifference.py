def fuzzy_difference(set1, set2):
    result = {}
    for key in set1:
        if key in set2:
            result[key] = max(set1[key] - set2[key], 0)
        else:
            result[key] = set1[key]
    return result

set1 = {'a': 0.7, 'b': 0.4, 'c': 0.9}
set2 = {'b': 0.6, 'c': 0.8, 'd': 0.5}

difference_result = fuzzy_difference(set1, set2)
print("Fuzzy Difference:", difference_result)
