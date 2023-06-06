import re
def number_of_sentences(string):
    sentence_separator_list = re.findall(r"[.!?]+", string)
    return len(sentence_separator_list)

print(number_of_sentences("My name is Bruno. I am a computer scientist!!! What is your name?"))

def number_of_sentences2(string):
    string = string.replace("!",".")
    string = string.replace("?", ".")
    string = re.sub(r"[.]+", ".", string)
    sentences = string.split(".")
    sentences.remove("")
    return len(sentences)

print(number_of_sentences2("My name is Bruno. I am a computer scientist!!! What is your name?"))

