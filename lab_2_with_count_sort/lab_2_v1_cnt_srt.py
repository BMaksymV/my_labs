def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)
    
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
        
    return arr

def max_hamsters(S, C, hamsters):

    def can_feed(k):
        if k == 0:
            return True
        
        costs = [h + g * (k - 1) for h, g in hamsters]
        
        counting_sort(costs)

        return sum(costs[:k]) <= S

    low, max = 0, C
    while low < max:
        mid = (low + max + 1) // 2
        if can_feed(mid):
            low = mid
        else:
            max = mid - 1

    return low
