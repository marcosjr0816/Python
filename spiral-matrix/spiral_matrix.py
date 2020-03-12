from typing import List

def spiral_matrix(size: int) -> List[List[int]]:
    result = [[0] * size for i in range(size)]
    vectors_x, vectors_y = [0, 1, 0, -1], [1, 0, -1, 0]
    curr_x, curr_y, curr_value = 0, -1, 1
    for i in range(size + size - 1):
        for _ in range((size + size - i) // 2):
            curr_x += vectors_x[i % 4]
            curr_y += vectors_y[i % 4]
            result[curr_x][curr_y] = curr_value
            curr_value += 1
    return result
