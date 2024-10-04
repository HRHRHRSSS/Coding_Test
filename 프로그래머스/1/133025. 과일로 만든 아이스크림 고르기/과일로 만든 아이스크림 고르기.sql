-- 2트
-- 상반기 아이스크림 총주문량 > 3000
-- 이고, 아이스크림 주 성분인 과일인
-- 아이스크림 맛을 총주문량이 큰 순서대로 정렬해 출력
SELECT A.FLAVOR
FROM FIRST_HALF A JOIN ICECREAM_INFO B
ON A.FLAVOR = B.FLAVOR
WHERE A.TOTAL_ORDER > 3000
AND B.INGREDIENT_TYPE = 'fruit_based'
ORDER BY TOTAL_ORDER DESC