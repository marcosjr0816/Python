def slices(series, length):
    total = len(series)
    if length > total or length <= 0:
        raise ValueError('longitud inválida')
    return [series[i:i + length] for i in range(total - length + 1)]
