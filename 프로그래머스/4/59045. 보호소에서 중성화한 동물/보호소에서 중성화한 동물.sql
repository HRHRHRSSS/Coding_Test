-- 보호소에서 중성화 수술을 거친 동물 정보
-- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물
-- 아이디와 생물 종, 이름을 조회
-- 아이디 순으로 정렬
SELECT A.ANIMAL_ID, A.ANIMAL_TYPE, A.NAME
FROM ANIMAL_INS A
JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.SEX_UPON_INTAKE LIKE 'Intact%'
    AND (B.SEX_UPON_OUTCOME LIKE 'Spayed%'
    OR B.SEX_UPON_OUTCOME LIKE 'Neutered%')
ORDER BY A.ANIMAL_ID