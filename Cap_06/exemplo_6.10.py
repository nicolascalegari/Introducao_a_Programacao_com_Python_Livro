L = list(range(100, 1100, 50))

print(L)

L = [5, 9, 13]

for x, e in enumerate(L):
    print(f"[{x}] {e}")

for z in enumerate(L):
    x, e = z
    print(f"[{x}] {e}")
    print(z)