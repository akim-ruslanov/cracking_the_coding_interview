''' Optimizations:
1) Return false when str len is > alphabet size

No data structure:
1) Compare every  character to other character O(n^2)
2) Sort the string and do linear search'''

# O(1) amortized
def isUnique(str):
    letters_dict = {}
    for x in str:
        if x in letters_dict:
            return False
        else:
            letters_dict[x] = 1
    return True


print(isUnique('hello'))