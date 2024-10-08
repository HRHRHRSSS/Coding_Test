WITH RECURSIVE GenerationCTE AS (
    -- 1세대 : PARENT_ID가 NULL인 대장균
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    -- 재귀적으로 세대를 계산
    SELECT e.ID, e.PARENT_ID, g.GENERATION+1 AS GENERATION
    FROM ECOLI_DATA e
    JOIN GenerationCTE g ON e.PARENT_ID = g.ID
)
-- 세대별로 자식이 없는 대장균 개수 세기
SELECT COUNT(g.ID) AS COUNT, g.GENERATION
FROM GenerationCTE g
LEFT JOIN ECOLI_DATA e ON g.ID = e.PARENT_ID
WHERE e.ID IS NULL -- 자식이 없는 개체들만 선택
GROUP BY g.GENERATION
ORDER BY g.GENERATION