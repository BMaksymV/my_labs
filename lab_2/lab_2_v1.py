def merge_sort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr

def max_hamsters(S, C, hamsters):

    def can_feed(k):
        if k == 0:
            return True
        
        costs = [h + g * (k - 1) for h, g in hamsters]
        
        merge_sort(costs)

        return sum(costs[:k]) <= S

    low, max = 0, C
    while low < max:
        mid = (low + max + 1) // 2
        if can_feed(mid):
            low = mid
        else:
            max = mid - 1

    return low
