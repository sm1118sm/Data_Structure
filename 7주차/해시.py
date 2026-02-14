def hashFn(key):
    sum = 0
    for c in key:
        sum = sum + ord(c)
    return sum % M