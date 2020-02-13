# solution of https://www.hackerrank.com/challenges/placements/problem

select name from (select name, salary as "Salary", f.friends_salary from students a join packages b on a.id = b.id join friends c on 
a.id = c.id join (select d.id "ID", salary as "friends_salary" from students d join packages e on d.id = e.id) f on f.ID = c.friend_id) 
g where g.Salary < g.friends_salary order by friends_salary

      
# solution of https://www.hackerrank.com/challenges/earnings-of-employees/problem
    
select salary*months, count(employee_id) from employee where salary*months = (select max(salary*months) from Employee) group by 
salary*months
          
 
# solution of https://www.hackerrank.com/challenges/weather-observation-station-2/problem    
          
select round(sum(LAT_N),2), round(sum(LONG_W), 2) from station
