-- 서울에 위치한 식당들의
-- 식당 ID, 식당 이름, 음식 종류, 즐찾 수, 주소, 리뷰 평균 점수 조회
-- 리뷰 평균점수 : 소수점 세 번째 자리에서 반올림
-- 평균점수 기준 내림차순, 즐겨찾기수 기준 내림차순
SELECT A.REST_ID, A.REST_NAME, A.FOOD_TYPE, A.FAVORITES,
A.ADDRESS, ROUND(AVG(B.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO A 
JOIN REST_REVIEW B ON A.REST_ID = B.REST_ID
GROUP BY REST_ID
HAVING A.ADDRESS LIKE '서울%'
ORDER BY AVG(B.REVIEW_SCORE) DESC, FAVORITES DESC

-- !!! 처음에는 GROUP BY를 쓸 생각을 못했다
-- 그런데, 리뷰 평균점수는 식당별로 내야하는 거니까
-- group by로 묶어주고, 서울 위치 식당은 having으로 넘어가야한다