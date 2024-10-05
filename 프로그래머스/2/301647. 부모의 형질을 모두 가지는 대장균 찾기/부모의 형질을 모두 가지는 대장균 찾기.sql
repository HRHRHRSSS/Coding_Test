-- 코드를 작성해주세요
SELECT C.ID, C.GENOTYPE, P.GENOTYPE AS PARENT_GENOTYPE
from ECOLI_DATA C
join ECOLI_DATA P ON C.parent_id = p.id
where C.genotype & P.genotype = p.genotype
order by c.id