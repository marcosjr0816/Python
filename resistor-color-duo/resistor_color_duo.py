def value(colors, code=""):
    list_colors = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9}
    for color in colors:
        code += str(list_colors[color])
    return int(code)
