select users.name, sum(coalesce(rides.distance, 0)) as travelled_distance
from users 
left join rides on users.id = rides.user_id
group by rides.user_id
order by travelled_distance desc, users.name asc
