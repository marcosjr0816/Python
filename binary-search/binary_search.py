from typing import List

def find(numbers: List[int], number: int) -> int:
    if numbers:
        start, end = 0, len(numbers) - 1
        while start <= end:
            mid = (start + end) // 2
            val = numbers[mid]
            if val > number:
                end = mid - 1
            elif val < number:
                start = mid + 1
            else:
                return mid
    raise ValueError("No result found!")
