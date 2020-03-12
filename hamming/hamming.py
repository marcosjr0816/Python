def distance(strand_a, strand_b, count=0):
    if len(strand_a) == len(strand_b):
        for i in range(0, len(strand_a)):
            if strand_a[i] != strand_b[i]:
                count += 1
        return count
    raise ValueError(".+")
