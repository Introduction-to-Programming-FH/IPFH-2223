def no_vowels(string):
    vowels =   ["a","e","i","o", "u", "A", "E", "I", "O", "U"]
    for vowel in vowels:
        string = string.replace(vowel,"")
    return string

import re
def no_vowels_regex(string):
    string = re.sub(r"[aeiouAEIOU]", "", string)
    return string

print(no_vowels("Hello"))
print(no_vowels_regex("HOla"))