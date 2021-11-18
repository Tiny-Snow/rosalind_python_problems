from scipy.special import comb

k, m, n = map(int, input().split())
p = 1 - (comb(n, 2) + m * n / 2 + comb(m, 2) / 4) / comb(k + m + n, 2)
print(p)