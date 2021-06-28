question 1
===========================================================
select roll_number, name from student_information a 
    join faculty_information b 
    on a.advisor = b.employee_id
    where (b.gender='F' and b.salary>20000) 
    or (b.gender='M' and b.salary > 15000)


question 2
===========================================================
select roll_number, name from (
select a.roll_number, name, sum(subject_one +  subject_two+subject_three) AS `total` from student_information a
    join examination_marks b 
    on a.roll_number = b.roll_number 
    group by a.roll_number, name having total < 100) mm
    
-- every derived table has to be given an alias - "mm"
    
