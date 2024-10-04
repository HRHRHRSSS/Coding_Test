-- 2트
-- 12세 이하인 '여자'환자
-- 환자이름,환자번호,성별코드,나이,전화번호
-- 전화번호가 없으면 'NONE'으로 출력
-- 나이 내림차순, 환자이름 오름차순
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO,'NONE') AS TLNO
FROM PATIENT
WHERE AGE <= 12 AND GEND_CD = 'W'
ORDER BY AGE DESC, PT_NAME ASC