-- 대장균 개체의 크기를 내림차순으로 정렬했을 때
-- 상위 0% ~ 25% 를 'CRITICAL', 
-- 26% ~ 50% 를 'HIGH'
-- 51% ~ 75% 를 'MEDIUM', 76% ~ 100% 를 'LOW'
SELECT P.ID,
    CASE
        WHEN P.PER <= 0.25 THEN 'CRITICAL'
        WHEN P.PER <= 0.5 THEN 'HIGH'
        WHEN P.PER <= 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM
    (SELECT ID,
            PERCENT_RANK() OVER(ORDER BY SIZE_OF_COLONY DESC) AS PER
    FROM ECOLI_DATA) AS P
ORDER BY P.ID