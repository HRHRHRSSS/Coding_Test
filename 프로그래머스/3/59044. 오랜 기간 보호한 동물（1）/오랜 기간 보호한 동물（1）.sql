-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리
-- 이름과 보호 시작일을 조회
-- 결과는 보호 시작일 순으로 조회
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE B.SEX_UPON_OUTCOME IS NULL -- 입양을 못 감
ORDER BY A.DATETIME -- 가장 오래 있었다 : 보호 시작일이 적은 ASC
LIMIT 3