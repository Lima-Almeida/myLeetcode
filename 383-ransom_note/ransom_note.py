ransomNote = "aa"
magazine = "aab"

def canConstruct(ransomNote, magazine):
    ransomNote = list(ransomNote)
    magazine = list(magazine)

    for k in ransomNote:
        try:
            magazine.remove(k)
        except ValueError:
            return False

    return True

print(canConstruct(ransomNote, magazine))