# solution of https://www.hackerrank.com/challenges/placements/problem
====================================================================================================
select name from (select name, salary as "Salary", f.friends_salary from students a join packages b on a.id = b.id join friends c on 
a.id = c.id join (select d.id "ID", salary as "friends_salary" from students d join packages e on d.id = e.id) f on f.ID = c.friend_id) 
g where g.Salary < g.friends_salary order by friends_salary

      
# solution of https://www.hackerrank.com/challenges/earnings-of-employees/problem
====================================================================================================    
select salary*months, count(employee_id) from employee where salary*months = (select max(salary*months) from Employee) group by 
salary*months
          
 
# solution of https://www.hackerrank.com/challenges/weather-observation-station-2/problem    
====================================================================================================          
select round(sum(LAT_N),2), round(sum(LONG_W), 2) from station

                                    
# solution of https://www.hackerrank.com/challenges/full-score/problem
====================================================================================================                                   
select m.hacker_id, n.name from (select a.hacker_id, count(submission_id) as 'NumberS' from submissions a join (select c.challenge_id, 
d.score from challenges c join difficulty d on c.difficulty_level = d.difficulty_level) b on a.challenge_id = b.challenge_id where 
a.score = b.score group by a.hacker_id having count(submission_id)>1) m join hackers n on m.hacker_id = n.hacker_id order by NumberS desc,
m.hacker_id asc


                                          
# solution of https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
                                          
select a.id, b.age, a.coins_needed, a.power from Wands a inner join Wands_Property b on a.code=b.code where b.is_evil!=1 and 
a.coins_needed=(select min(Wands.coins_needed) from Wands inner join Wands_Property on Wands.code=Wands_Property.code where 
Wands_Property.age=b.age and Wands.power=a.power) order by a.power desc,b.age desc
                                                      
