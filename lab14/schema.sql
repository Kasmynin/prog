DROP TABLE IF EXISTS REPAIR;
DROP TABLE IF EXISTS VEHICLE;
DROP TABLE IF EXISTS CLIENT;

-- Создание таблицы Клиенты
CREATE TABLE CLIENT (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    email VARCHAR(255)
);

-- Создание таблицы Транспортные средства
CREATE TABLE VEHICLE (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    client_id INT NOT NULL,
    make VARCHAR(255) NOT NULL,
    model VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    license_plate VARCHAR(20),
    FOREIGN KEY (client_id) REFERENCES CLIENT(client_id)
);

-- Создание таблицы Ремонты
CREATE TABLE REPAIR (
    repair_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    repair_date DATE NOT NULL,
    description TEXT,
    cost DECIMAL(10, 2),
    FOREIGN KEY (vehicle_id) REFERENCES VEHICLE(vehicle_id)
);