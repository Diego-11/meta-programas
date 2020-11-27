def split_values(value):
    dct = {}
    value = value.split('-')
    a = value[0]
    b = value[1]
    dct = {'d': a, 'i': b}
    return dct
