class Matrix:
    def __init__(self, matrix_string: str):
        self.matrix = [[int(elem) for elem in row.split(" ")] for row in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return list(map(lambda row: row[index - 1], self.matrix))
