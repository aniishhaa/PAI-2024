def fuzzy_union(set1, set2):
    result = {}
    for key in set1:
        if key in set2:
            result[key] = max(set1[key], set2[key])
        else:
            result[key] = set1[key]
    for key in set2:
        if key not in set1:
            result[key] = set2[key]
    return result

set1 = {'a': 0.7, 'b': 0.4, 'c': 0.9}
set2 = {'b': 0.6, 'c': 0.8, 'd': 0.5}

union_result = fuzzy_union(set1, set2)
print("Fuzzy Union:", union_result)
