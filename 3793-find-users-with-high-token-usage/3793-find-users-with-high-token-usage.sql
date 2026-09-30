# Write your MySQL query statement below
SELECT user_id , count(*) AS prompt_count, round(avg(tokens),2) as avg_tokens  
    FROM prompts 
    GROUP BY user_id
    HAVING count(*) >= 3 AND MAX(tokens) > AVG(tokens)
    ORDER BY avg_tokens DESC,  user_id ASC
    ;