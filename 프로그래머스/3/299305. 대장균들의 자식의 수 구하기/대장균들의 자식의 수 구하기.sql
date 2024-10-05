-- 대장균 개체의 ID(ID)와 자식의 수(CHILD_COUNT)를 출력
-- 자식이 없다면 자식의 수는 0으로 출력
-- 결과는 개체의 ID 에 대해 오름차순 정렬
SELECT P.ID, COUNT(C.ID) AS CHILD_COUNT
FROM ECOLI_DATA P
LEFT JOIN ECOLI_DATA C ON C.PARENT_ID = P.ID
GROUP BY P.ID
ORDER BY P.ID ASC

-- 헷갈렸던것? group by로 p.id를 묶어놓고 왜 c.id count를 하지?
-- 부모끼리 묶어놓고 그거에 맞는 자식수를 세어야 하니까
-- 그리고 없으면 0을 반환하래서 isnull 을 쓰려고 했는데
-- 생각해보니 count 할게없으면 알아서 0을 반환한다