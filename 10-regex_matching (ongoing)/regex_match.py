
s = 'aab'
p = 'c*a*b'

# '.' matches any single character
# '*' matches zero or more preceding element

def isMatch(s, p):

    strcomp = list(s)
    pattern = list(p)

    if pattern[0] == '.' and pattern[1] == '*':
        return True
    
    if s == p:
        return True

        
    else:
        counter = 0
        state = False
        prev_element = ''
        star_mark = False

        for k in range(len(strcomp)):

            if counter == len(pattern): #wrong
                if len(strcomp) > len(pattern):
                    if strcomp[counter] == pattern[counter - 1]:
                        state = False
                #state = True
                break

            if pattern[counter] == '*':
                star_mark = True
                prev_element = pattern[counter - 1]


            if not star_mark:
                if strcomp[k] == pattern[counter] or pattern[counter] == '.':
                    state = True
                    counter = counter + 1
                else:
                    counter = 0
            else:
                if strcomp[k] != prev_element:
                    counter = 0
                    star_mark = False


    return state

print(isMatch(s, p))