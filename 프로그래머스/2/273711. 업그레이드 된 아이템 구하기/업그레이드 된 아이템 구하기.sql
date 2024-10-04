-- 희귀도가 'RARE'인 아이템들의
-- 모든 다음 업그레이드 아이템의 아이템ID, 아이템 명, 희귀도 출력
-- 아이템 ID 내림차순 정렬
SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
FROM ITEM_INFO A
JOIN ITEM_TREE B ON A.ITEM_ID = B.ITEM_ID
WHERE B.PARENT_ITEM_ID IN (SELECT ITEM_ID
                           FROM ITEM_INFO
                           WHERE RARITY='RARE')
ORDER BY A.ITEM_ID DESC