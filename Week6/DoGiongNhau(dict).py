def solve() -> None:
    a = input().strip()
    b = input().strip()

    if len(a) == 1 or len(b) == 1:
        print(0)

    ans = 0
    pairs = set()
    for i in range(1, len(a)):
        pairs.add(a[i-1]+a[i])

    for i in range(1, len(b)):
        ans += 1 if b[i-1]+b[i] in pairs else 0

    print(ans)


solve()
