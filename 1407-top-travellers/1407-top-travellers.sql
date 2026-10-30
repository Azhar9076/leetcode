# Write your MySQL query statement below
SELECT u.name , COALESCE(sum(distance),0)
   as travelled_distance FROM
Users u LEFT JOIN Rides r 
    ON u.id = r.user_id
    GROUP BY U.id, u.name
ORDER BY travelled_distance DESC, 
 u.name ASC; 