from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Client, Tour, Country, client_tour, Base 
from tabulate import tabulate

engine = create_engine('sqlite:///travel.db', echo=True) 
Session = sessionmaker(bind=engine)
session = Session()

# 1. Найти всех клиентов
clients = session.query(Client).all()
print("\n--- Список всех клиентов ---")
data = [[client.name, client.email, client.phone_number] for client in clients]
headers = ["Имя", "Email", "Телефон"]
print(tabulate(data, headers=headers, tablefmt="grid"))

# 2. Найти все туры во Францию
france = session.query(Country).filter_by(country_name="France").first()
if france:
    tours_to_france = france.tours
    print("\n--- Туры во Францию ---")
    data = [[tour.tour_name, tour.start_date, tour.price] for tour in tours_to_france]
    headers = ["Название тура", "Дата начала", "Цена"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
else:
    print("\nНет туров во Францию")

# 3. Найти всех клиентов, которые забронировали тур "Итальянское приключение"
italian_adventure = session.query(Tour).filter_by(tour_name="Italian Adventure").first()
if italian_adventure:
    clients_on_italian_adventure = italian_adventure.clients
    print("\n--- Клиенты, забронировавшие Italian Adventure ---")
    data = [[client.name, client.email] for client in clients_on_italian_adventure]
    headers = ["Имя клиента", "Email"]
    print(tabulate(data, headers=headers, tablefmt="grid"))
else:
    print("\nТур Italian Adventure не найден")

# 4. Найти туры стоимостью более 1500 долларов
expensive_tours = session.query(Tour).filter(Tour.price > 1500).all()
print("\n--- Туры дороже $1500 ---")
data = [[tour.tour_name, tour.price] for tour in expensive_tours]
headers = ["Название тура", "Цена"]
print(tabulate(data, headers=headers, tablefmt="grid"))

# 5. Количества туров на одного клиента
tour_counts = session.query(
    Client.name,
    func.count(client_tour.c.tour_id)
).join(
    client_tour,
    Client.client_id == client_tour.c.client_id
).group_by(
    Client.name
).all()

print("\n--- Количество туров, забронированных каждым клиентом ---")
data = [[client_name, tour_count] for client_name, tour_count in tour_counts]
headers = ["Имя клиента", "Количество туров"]
print(tabulate(data, headers=headers, tablefmt="grid"))

session.close()
