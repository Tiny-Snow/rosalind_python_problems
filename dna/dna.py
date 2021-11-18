A, C, G, T = 0, 0, 0, 0

for s in input():
    if s == 'A':
        A += 1
    elif s == 'C':
        C += 1
    elif s == 'G':
        G += 1
    elif s == 'T':
        T += 1

print(A, C, G, T)