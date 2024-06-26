def complement(set1, universal_set):
    return universal_set - set1

universal_set = {1, 2, 3, 4, 5}
set1 = {2, 4}

complement_set = complement(set1, universal_set)
print("Complement of set1:", complement_set)
