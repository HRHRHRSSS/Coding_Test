def solution(n):
    c = bin(n)[2:]
    cnt = c.count('1')
    next_num = n+1
    
    while True:
        nextc = bin(next_num)[2:]
        nextcnt = nextc.count('1')
        if cnt == nextcnt:
            break;
        else:
            next_num += 1
    return(next_num)