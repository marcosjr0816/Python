def is_pangram(sentence):
    if sentence == "":
        return False
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    text = sentence.lower().replace(" ", "")
    for letter in alphabet:
        if letter not in text:
            return False
    return True
