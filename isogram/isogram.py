def is_isogram(string):
    new_str = string.lower().replace(" ", "").replace("-", "")
    for i in range(0, len(new_str)):
        for j in range(i + 1, len(new_str)):
            if new_str[i] == new_str[j]:
                return False
    return True
