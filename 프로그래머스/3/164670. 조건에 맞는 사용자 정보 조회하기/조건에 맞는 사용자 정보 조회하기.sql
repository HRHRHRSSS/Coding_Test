-- 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회
-- 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력
-- 결과는 회원 ID를 기준으로 내림차순 정렬
SELECT DISTINCT B.USER_ID, B.NICKNAME,
    CONCAT(CITY,' ',STREET_ADDRESS1,' ',STREET_ADDRESS2) AS 전체주소, 
    CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4)) AS 전화번호
FROM USED_GOODS_BOARD A
JOIN USED_GOODS_USER B ON A.WRITER_ID = B.USER_ID
WHERE A.WRITER_ID IN (SELECT WRITER_ID
                     FROM USED_GOODS_BOARD
                     GROUP BY WRITER_ID
                     HAVING COUNT(WRITER_ID)>=3)
ORDER BY B.USER_ID DESC
