from collections import deque

n = int(input())
card = []
for i in range(n):
    card.append(i+1)
    
card = deque(card)

while len(card)>1:
    card.popleft()
    temp = card.popleft()
    card.append(temp)
    
print(card[0])