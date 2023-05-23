s1 = "apple"
s2 = "pplea"

def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    f1 = {}
    f2 = {}
    for i in s1:
        if i in f1:
            f1[i] += 1
        else:
            f1[i] = 1

    for i in s2:
        if i in f2:
            f2[i] += 1
        else:
            f2[i] = 1
    if f1==f2:
        return True
    else:
        return False
    

print(anagram(s1, s2))

