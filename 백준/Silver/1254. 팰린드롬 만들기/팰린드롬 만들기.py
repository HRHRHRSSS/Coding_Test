S = input().strip()
n = len(S)

forlen = 0
for i in range(n):
    if S[i:] == S[i:][::-1]:
        forlen = n-i
        break
        
add_char = S[:n-forlen][::-1]
result = S+add_char
print(len(result))