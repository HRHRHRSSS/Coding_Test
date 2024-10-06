-- 서브쿼리 두 번 사용하기?
SELECT ID
FROM ECOLI_DATA
WHERE PARENT_ID IN
                (SELECT ID
                FROM ECOLI_DATA
                WHERE PARENT_ID IN
                                (SELECT ID
                                FROM ECOLI_DATA
                                WHERE PARENT_ID IS NULL))
ORDER BY ID ASC