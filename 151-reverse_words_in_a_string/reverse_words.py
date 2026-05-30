s = "a good   example"

def reverseWords(s):
    words_list = []
    char_list = []
    aux_list = list(s)

    word_start = False

    for k in range(len(aux_list)):
        if aux_list[k] != ' ':
            word_start = True
            char_list.append(aux_list[k])
        elif aux_list[k] == ' ' and word_start == True:
            word_start = False
            words_list.append("".join(char_list))
            char_list.clear()

    if len(char_list) > 0:
        words_list.append("".join(char_list))
        char_list.clear()

    words_list.reverse()

    return " ".join(words_list)

print(reverseWords(s))
