-- 2트
-- 상반기 판매된 아이스크림의 맛
-- 총주문량 내림차순, 출하번호 오름차순
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC