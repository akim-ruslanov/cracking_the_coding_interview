'''
Ask:
1) Do we care about spaces?
2) Upper case vs lower case?
3) Can I use built-in lower functions? '''

'''Notes:
1) Make your code more modular
2) One loop per function if possible'''

# Assuming spaces do not matter, and I can use lower function
def palindrome_perm(str):
    letter_dict = {}
    odd_count = 0
    str = remove_spaces(str)
    str = str.lower()
    for x in str:
        if x in letter_dict:
            letter_dict[x] += 1
            if letter_dict[x] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        else:
            letter_dict[x] = 1
            odd_count += 1
    return odd_count<=1

def remove_spaces(str):
    ret = ''
    for x in str:
        if x != ' ':
            ret += x
    return ret
print(palindrome_perm('Tact coa'))