s1 = "abca"
s2 = ""
s3 = " "
s4 = "pwwkew"
s5 = "aab"

#soluçao1
def lengthOfLongestSubstring(s: str) -> int:
    list_aux = list(s)
    current = []
    max_size = 0
    current_size = 0
    index_aux = 0
    index_aux_ultimo = 0
    update = True
    while True:
        if index_aux > len(list_aux) - 1:
            break
        if not list_aux[index_aux] in current:
            if update:
                index_aux_ultimo = index_aux
                update = False
            current.append(list_aux[index_aux])
            current_size = len(current)
            if current_size > max_size:
                max_size = current_size
        else:
            if current_size > max_size:
                max_size = current_size
            index_aux = index_aux_ultimo
            current.clear()
            update = True
        index_aux = index_aux + 1
    return max_size

#soluçao2 (bem mais eficiente)
def lengthOfLongestSubstring2(s: str) -> int:
    last_seen = {}
    start = 0
    max_len = 0

    for end in range(len(s)):
        char = s[end]
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = end
        max_len = max(max_len, end - start + 1)

    return max_len

print(lengthOfLongestSubstring2(s4))