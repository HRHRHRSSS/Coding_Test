import sys
from collections import Counter

trees = []
while True:
    tree = str(sys.stdin.readline().rstrip())
    # 입력받은 나무가 없다면 반복문을 멈춘다.
    if not tree:
        break
    trees.append(tree)

tree_map = Counter(trees)
total_trees = sum(tree_map.values())
sorted_tree = sorted(tree_map.keys())

for t in sorted_tree:
    rate = (tree_map[t] / total_trees) * 100
    # f-string으로 소수점 4자리까지 출력
    print(f'{t} {rate:.4f}')