SELECT state_name ,city,sum(n_killed)
FROM dbapp.gun_violence
GROUP BY state_name, city
ORDER BY sum(n_killed) desc;