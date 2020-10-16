def init_dict(s: str, map: dict) -> None:
    for i in range(1, len(s)):
        if s[i-1]+s[i] not in map:
            map[s[i-1]+s[i]] = 1
        else:
            map[s[i-1]+s[i]] += 1


def count_similarity(s: str, map: dict) -> int:
    ans = 0
    for i in range(1, len(s)):
        ans += map[s[i-1]+s[i]] if s[i-1]+s[i] in map else 0

    return ans


def solve() -> None:
    a = input().strip()
    b = input().strip()

    if len(a) == 1 or len(b) == 1:
        print(0)

    ans = 0
    pairs1 = dict()
    pairs2 = dict()

    init_dict(a, pairs1)
    init_dict(b, pairs2)

    ans = max(count_similarity(a, pairs2), count_similarity(b, pairs1))

    print(ans)


solve()
