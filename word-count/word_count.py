def count_words(sentence):
    counts = dict()
    words = sentence.lower().replace('\n', ' ').replace(',', ' ').replace('_', ' ').replace("!!&@$%^&", "")\
        .replace(':', '').replace('.', '').replace('"', '').split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
