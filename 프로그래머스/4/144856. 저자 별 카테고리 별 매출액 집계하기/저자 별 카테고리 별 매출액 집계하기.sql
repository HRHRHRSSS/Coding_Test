-- 2022년 1월의 도서 판매 데이터를 기준
-- 저자 별, 카테고리 별 매출액(TOTAL_SALES = 판매량 * 판매가) 출력
-- 저자 ID(AUTHOR_ID), 저자명(AUTHOR_NAME), 카테고리(CATEGORY), 매출액(SALES) 리스트를 출력
-- 저자 ID를 오름차순으로, 저자 ID가 같다면 카테고리를 내림차순 정렬
SELECT A.AUTHOR_ID, B.AUTHOR_NAME, A.CATEGORY, SUM(A.PRICE * C.SALES) AS TOTAL_SALES
FROM BOOK A
JOIN AUTHOR B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN BOOK_SALES C ON A.BOOK_ID = C.BOOK_ID
WHERE C.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
GROUP BY A.AUTHOR_ID, A.CATEGORY
ORDER BY A.AUTHOR_ID, A.CATEGORY DESC
