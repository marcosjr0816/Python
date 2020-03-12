def is_valid(isbn):
    try:
        digits = [int(num) for num in list(isbn[:-1].replace('-', ''))]
        check = 10 if isbn[-1] == 'X' else int(isbn[-1])
        digits.append(check)
    except:
        return False
    total = 0
    for pos, digit in enumerate(digits):
        total += digit * (10 - pos)
    return True if len(digits) == 10 and total % 11 == 0 else False
