-- 중성화된 동물은 SEX_UPON_INTAKE 컬럼에 'Neutered' 또는 'Spayed'
-- 동물의 아이디와 이름, 중성화 여부를 아이디 순으로 조회
-- 중성화가 되어있다면 'O', 아니라면 'X'라고 표시
SELECT ANIMAL_ID, NAME,
    CASE 
        WHEN SEX_UPON_INTAKE LIKE 'Intact%' THEN 'X'
        ELSE 'O'
    END AS "중성화"
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
