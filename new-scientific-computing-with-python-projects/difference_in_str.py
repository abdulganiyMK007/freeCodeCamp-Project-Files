str1 = "hello world"
str2 = "hallo worlt"


def difference_in_string(str1, str2):
    set_diff1 = set(str1) - set(str2)
    set_diff2 = set(str2) - set(str1)

    print(f"Characters in str1 but not in str2: {set_diff1}")
    print(f"Characters in str2 but not in str1: {set_diff2}")


def difference_char_by_char(str1, str2):
    for i, (char1, char2) in enumerate(zip(str1, str2)):
        if char1 != char2:
            print(f"Difference at position {i}: '{char1}' vs '{char2}'")


from difflib import ndiff


def difference_diff(str1, str2):
    diff = ndiff(str1, str2)
    print("\n".join(diff))

print('DIFFERENCE: by set')
difference_in_string(str1, str2)

print('DIFFERENCE: character by character')
difference_char_by_char(str1, str2)


difference_diff(str1, str2)



