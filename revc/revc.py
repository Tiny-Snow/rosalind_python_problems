s = ''
for c in input()[::-1]:
    if c == 'A':
        s += 'T'
    elif c == 'T':
        s += 'A'
    elif c == 'C':
        s += 'G'
    elif c == 'G':
        s += 'C'
print(s)