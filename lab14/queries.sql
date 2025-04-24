-- 1. Получить всех клиентов и их транспортные средства
SELECT c.first_name, c.last_name, v.make, v.model
FROM CLIENT c
JOIN VEHICLE v ON c.client_id = v.client_id;

-- 2. Получить все ремонты для конкретного транспортного средства (например, с vehicle_id = 1)
SELECT r.repair_date, r.description, r.cost
FROM REPAIR r
WHERE r.vehicle_id = 1;

-- 3. Получить общее количество ремонтов для каждого клиента
SELECT c.first_name, c.last_name, COUNT(r.repair_id) AS total_repairs
FROM CLIENT c
JOIN VEHICLE v ON c.client_id = v.client_id
LEFT JOIN REPAIR r ON v.vehicle_id = r.vehicle_id
GROUP BY c.client_id, c.first_name, c.last_name;

-- 4. Получить среднюю стоимость ремонта
SELECT AVG(cost) AS average_repair_cost
FROM REPAIR;

-- 5. Получить клиентов, которые имеют машины старше 2010 года
SELECT c.first_name, c.last_name, v.make, v.model, v.year
FROM CLIENT c
JOIN VEHICLE v ON c.client_id = v.client_id
WHERE v.year < 2010;

-- 6. Получить все ремонты, выполненные в определенный период (например, между '2023-01-01' и '2023-03-31')
SELECT r.repair_date, r.description, r.cost, v.make, v.model, c.first_name, c.last_name
FROM REPAIR r
JOIN VEHICLE v ON r.vehicle_id = v.vehicle_id
JOIN CLIENT c ON v.client_id = c.client_id
WHERE r.repair_date BETWEEN '2023-01-01' AND '2023-03-31';

-- 7. Получить клиента с самой дорогой машиной по году выпуска
SELECT c.first_name, c.last_name, v.make, v.model, v.year
FROM CLIENT c
JOIN VEHICLE v ON c.client_id = v.client_id
ORDER BY v.year DESC
LIMIT 1;