-- FIRST_HALF: 상반기 주문 정보
-- ICECREAM_INFO : 아이스크림 성분
SELECT A.FLAVOR
FROM FIRST_HALF A JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR 
-- 상반기 아이스크림 총주문량이 3,000보다 높으
-- + 아이스크림의 주 성분이 과일인 아이스크림의 맛
WHERE A.TOTAL_ORDER > 3000 AND B.INGREDIENT_TYPE = 'fruit_based'
-- 총주문량이 큰 순서
ORDER BY A.TOTAL_ORDER DESC;