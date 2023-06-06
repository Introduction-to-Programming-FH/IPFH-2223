import re
def ordered_words(string):
    word_list = re.split(r"\W+", string)
    if "" in word_list:
        word_list.remove("")
    word_set = set(word_list)
    word_list = list(word_set)
    word_list.sort()
    return word_list

print(ordered_words("who lives in munich?"))
