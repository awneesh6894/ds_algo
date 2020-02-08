s =input()

def uniq_char(s):
    count = {}
    for i in s:
        if i not in count:
            count[i] = 1
        else:
            return False
    return True



def uniq_char2(s):
    return len(set(s)) == len(s)

print(uniq_char2(s))