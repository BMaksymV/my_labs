def max_hamsters(S, C, hamsters) -> int:

    def can_feed(k: int) -> bool:
        if k == 0:
            return True
        costs = [h + g * (k - 1) for h, g in hamsters]
        costs.sort()
        return sum(costs[:k]) <= S

    low, max = 0, C
    while low < max:
        mid = (low + max + 1) // 2
        if can_feed(mid):
            low = mid
        else:
            max = mid - 1

    return low
