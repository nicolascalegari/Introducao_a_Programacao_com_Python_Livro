# MDC
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

# MMC
def mmc(a, b):
    return abs(a * b) / mdc(a, b)

print(f"MMC 10 e 5: {mmc(10, 5)}")
print(f"MMC 32 e 24: {mmc(15, 3)}")
print(f"MMC 5 e 3: {mmc(20, 2)}")