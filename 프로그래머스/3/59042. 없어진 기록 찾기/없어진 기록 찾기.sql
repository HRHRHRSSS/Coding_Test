-- 입양을 간 기록은 있는데, 보호소에 들어온 기록이 없는
-- 동물의 ID와 이름
-- ID순으로 정렬
SELECT B.ANIMAL_ID, B.NAME
FROM ANIMAL_INS A
RIGHT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE SEX_UPON_INTAKE IS NULL
ORDER BY B.ANIMAL_ID