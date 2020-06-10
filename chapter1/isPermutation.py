'''
Ask what kind of strings (ASCII vs Unicode). Are two strings always the same size? Are spaces allowed? upper case vs lower case? '''

def isPermutation(str1, str2):
    letter_dict = {}
    if (len(str1) != len(str2)):
        return False
    for x in str1:
        if x in letter_dict:
            letter_dict[x]+=1
        else:
            letter_dict[x]=1
    for x in str2:
        if x in letter_dict:
            letter_dict[x] -= 1
            if letter_dict[x] == 0:
                letter_dict.pop(x)
        else:
            return False
    return True

print(isPermutation('aabbcc', 'abcdea'))
print(isPermutation('aaaopee', 'eeopaaa'))