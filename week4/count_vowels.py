def count_vowels(s):
    vowels = ["a","e","i","o","u"]
    counter = 0
    for character in s:
        if character in vowels:
            counter +=1
    return counter