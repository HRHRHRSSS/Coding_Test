-- 테스트케이스는 통과했는데 채점이 틀린 이유
-- concat()함수 쓰면 결과값은 String이므로 order by 의 값을 round(sum(~), ~)으로 바꿔야한다.
SELECT ROUTE,
        CONCAT(ROUND(SUM(D_BETWEEN_DIST),1),"km") AS "TOTAL_DISTANCE",
        CONCAT(ROUND(AVG(D_BETWEEN_DIST),2),"km") AS "AVERAGE_DISTANCE"
FROM SUBWAY_DISTANCE
GROUP BY ROUTE
ORDER BY ROUND(SUM(D_BETWEEN_DIST),1) DESC