-- 형질 : GENOTYPE
-- 2번 형질이 보유하지 않으면서 1번 3번 형질을 보유하고
-- 있는 대장균 개체의 수 
SELECT COUNT(ID) COUNT
FROM ECOLI_DATA 
WHERE
    -- CONV 활용 (10진수 -> 2진수 변환)
    -- 2번 형질을 보유하지 않으면서
    CONV(GENOTYPE, 10, 2) NOT LIKE '%1_' AND
    -- 1번, 3번 형질 보유
    (CONV(GENOTYPE, 10, 2) LIKE '%1' OR
    CONV(GENOTYPE, 10, 2) LIKE '%1__')