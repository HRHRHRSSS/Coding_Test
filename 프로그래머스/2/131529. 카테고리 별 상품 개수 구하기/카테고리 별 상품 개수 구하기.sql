-- PRODUCT 테이블에서 상품 카테고리 코드(PRODUCT_CODE 앞 2자리) 별 상품 개수를 출력
-- 앞 2자리는 카테고리 코드를 의미
-- 결과는 상품 카테고리 코드를 기준으로 오름차순 정렬
SELECT SUBSTR(PRODUCT_CODE,1,2) AS CATEGORY
        ,COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY CATEGORY