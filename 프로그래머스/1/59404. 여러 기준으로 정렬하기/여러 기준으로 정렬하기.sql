-- 동물의 아이디, 이름, 보호시작일
-- 이름순, 보호 나중에 시작한 순으로 정렬
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC