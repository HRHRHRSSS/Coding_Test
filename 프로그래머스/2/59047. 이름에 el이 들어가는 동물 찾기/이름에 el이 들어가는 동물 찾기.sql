-- 이름에 "EL"이 들어가는 개의 아이디와 이름을 조회하는 SQL문
-- 결과는 이름 순으로 조회해주세요. 단, 이름의 대소문자는 구분하지 않습니다.
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE "%el%"
    AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME ASC