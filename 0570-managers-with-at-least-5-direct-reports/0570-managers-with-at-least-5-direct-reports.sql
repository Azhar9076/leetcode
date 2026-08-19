# Write your MySQL query statement below
SELECT e.name FROM Employee e JOIN Employee r ON e.id = r.managerId GROUP BY e.name, e.id HAVING count(e.id) >= 5;