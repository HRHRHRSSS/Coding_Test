# 히든케이스 -> 공백문자가 연속해서 나올 수 있다?

def solution(s):
    newstring = []
    arr = s.split(' ')
    for i in arr:
        if i and i[0].isalpha():
            first = i[0].upper()
            back = i[1:].lower()
            temp = first+back
        else:
            temp = i.lower()
        newstring.append(temp)
    return ' '.join(newstring)