-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성
-- 진료예약일시를 기준으로 오름차순 정렬
SELECT C.APNT_NO, A.PT_NAME, C.PT_NO, 
    C.MCDP_CD, B.DR_NAME, C.APNT_YMD
FROM APPOINTMENT C
JOIN PATIENT A ON C.PT_NO = A.PT_NO
JOIN DOCTOR B ON C.MDDR_ID = B.DR_ID
WHERE C.MCDP_CD = 'CS'
    AND C.APNT_CNCL_YN = 'N'
    AND DATE_FORMAT(C.APNT_YMD,'%Y-%m-%d') = '2022-04-13'
ORDER BY C.APNT_YMD
