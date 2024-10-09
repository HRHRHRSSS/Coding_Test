-- HR_DEPARTMENT, HR_EMPLOYEES, HR_GRADE 테이블에서 2022년도 한해 평가 점수가 가장 높은 사원 정보를 조회
-- 2022년도 평가 점수가 가장 높은 사원들의 점수, 사번, 성명, 직책, 이메일을 조회
-- 2022년도의 평가 점수는 상,하반기 점수의 합을 의미
-- 평가 점수를 나타내는 컬럼의 이름은 SCORE
SELECT SUM(C.SCORE) AS SCORE, C.EMP_NO, B.EMP_NAME, B.POSITION, B.EMAIL
FROM HR_EMPLOYEES B
JOIN HR_GRADE C ON B.EMP_NO = C.EMP_NO
GROUP BY EMP_NO
ORDER BY SCORE DESC
LIMIT 1