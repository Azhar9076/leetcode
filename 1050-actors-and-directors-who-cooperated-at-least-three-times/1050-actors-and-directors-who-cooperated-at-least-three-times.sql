# Write your MySQL query statement below
SELECT actor_id , director_id FROM ActorDirector GROUP BY Actor_id , director_id HAVING count(*) >= 3;