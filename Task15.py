N, K = map(int, input().split())

x = ["I"] * N

for _ in range(K):
    li, ri = map(int, input().split())
    x[li - 1:ri] = ["."] * (ri - li + 1)

res = "".join(x)
print(res)