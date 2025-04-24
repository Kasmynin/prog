-- Заполнение таблицы Клиенты
INSERT INTO CLIENT (first_name, last_name, phone_number, email) VALUES
('John', 'Doe', '555-123-4567', 'john.doe@example.com'),
('Jane', 'Smith', '555-987-6543', 'jane.smith@example.com'),
('Alice', 'Johnson', '555-111-2222', 'alice.johnson@example.com');

-- Заполнение таблицы Транспортные средства
INSERT INTO VEHICLE (client_id, make, model, year, license_plate) VALUES
(1, 'Toyota', 'Camry', 2018, 'ABC-123'),
(1, 'Honda', 'Civic', 2020, 'XYZ-789'),
(2, 'Ford', 'F-150', 2022, 'DEF-456'),
(3, 'Nissan', 'Altima', 2019, 'GHI-012');

-- Заполнение таблицы Ремонты
INSERT INTO REPAIR (vehicle_id, repair_date, description, cost) VALUES
(1, '2023-01-15', 'Замена масла', 75.00),
(1, '2023-03-20', 'Замена тормозных колодок', 150.00),
(2, '2023-02-10', 'Ремонт двигателя', 500.00),
(3, '2023-04-01', 'Замена шин', 400.00),
(4, '2023-05-05', 'Замена аккумулятора', 120.00);