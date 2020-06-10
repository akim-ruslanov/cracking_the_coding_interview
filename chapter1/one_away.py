'''
Ask:
1) Uppercase vs lowercase  
2) '''


def one_away(str1, str2):
    if (max(str1, str2) - min(str1, str2) > 1):
        return False
    big_str = max(str1, str2)
    small_str = min(str1, str2)
    letter_dict = build_letter_dict(big_str)
    for x in