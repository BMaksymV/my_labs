def compute_tf(needle):
    m = len(needle)
    alphabet = set(needle)
    tf = [{char: 0 for char in alphabet} for _ in range(m + 1)]
    
    for state in range(m + 1):
        for char in alphabet:
            if state < m and char == needle[state]:
                tf[state][char] = state + 1
            else:
                current_str = needle[:state] + char
                for i in range(min(state + 1, m), 0, -1):
                    if current_str.endswith(needle[:i]):
                        tf[state][char] = i
                        break
    return tf

def search_automaton(haystack, needle):
    n = len(haystack)
    m = len(needle)
    result_indices = []

    if m == 0 or n == 0 or m > n:
        return result_indices

    tf = compute_tf(needle)
    state = 0

    for i in range(n):
        char = haystack[i]
        
        if char in tf[state]:
            state = tf[state][char]
        else:
            state = 0
            if char in tf[0]:
                state = tf[0][char]

        if state == m:
            result_indices.append(i - m + 1)

    return result_indices