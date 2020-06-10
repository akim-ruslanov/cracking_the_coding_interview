''' 
Ask ASCII vs Unicode? Double spaces? Spaces at the end?

Notes:
1) To do in O(1) space, need to copy over the elements. Hurts time complexity'''

# Assuming no double spaces
def urlify(str, len):
    url = ""
    for x in range(len):
        if str[x] == ' ':
            url += '%20'
        else:
            url += str[x]
    return url

print(urlify('Mr John Smith      ', 13))