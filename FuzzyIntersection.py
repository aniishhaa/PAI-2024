def fuzzy_intersection(set1, set2):
    result = {}
    for key in set1:
        if key in set2:
            result[key] = min(set1[key], set2[key])
    return result

set1 = {'a': 0.7, 'b': 0.4, 'c': 0.9}
set2 = {'b': 0.6, 'c': 0.8, 'd': 0.5}

intersection_result = fuzzy_intersection(set1, set2)
print("Fuzzy Intersection:", intersection_result)
