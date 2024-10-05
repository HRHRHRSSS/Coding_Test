-- 가장 큰 물고기 10마리의 ID와 길이 출력 (LIMIT사용?)
-- 길이 기준 내림차순, ID기준 오름차순
-- 가장 큰 물고기 10마리 중 NULL인 경우는 x
SELECT ID, LENGTH
FROM FISH_INFO
ORDER BY LENGTH DESC, ID ASC
LIMIT 10

