from sqlalchemy import create_engine, Column, Integer, String, Date, Numeric, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import date

Base = declarative_base()

tour_country = Table('tour_country', Base.metadata,
    Column('tour_id', Integer, ForeignKey('tour.tour_id'), primary_key=True),
    Column('country_id', Integer, ForeignKey('country.country_id'), primary_key=True)
)

client_tour = Table('client_tour', Base.metadata,
    Column('client_id', Integer, ForeignKey('client.client_id'), primary_key=True),
    Column('tour_id', Integer, ForeignKey('tour.tour_id'), primary_key=True),
    Column('booking_date', Date) 
)


class Client(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)

    tours = relationship("Tour", secondary=client_tour, back_populates="clients")

    def __repr__(self):
        return f"<Client(name='{self.name}', email='{self.email}')>"


class Tour(Base):
    __tablename__ = 'tour'

    tour_id = Column(Integer, primary_key=True)
    tour_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    price = Column(Numeric)

    countries = relationship("Country", secondary=tour_country, back_populates="tours")
    clients = relationship("Client", secondary=client_tour, back_populates="tours")

    def __repr__(self):
        return f"<Tour(name='{self.tour_name}', start_date='{self.start_date}', price='{self.price}')>"


class Country(Base):
    __tablename__ = 'country'

    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)

    tours = relationship("Tour", secondary=tour_country, back_populates="countries")

    def __repr__(self):
        return f"<Country(name='{self.country_name}')>"


engine = create_engine('sqlite:///travel.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

client1 = Client(name="Alice Smith", email="alice@example.com", phone_number="123-456-7890")
client2 = Client(name="Bob Johnson", email="bob@example.com", phone_number="098-765-4321")
client3 = Client(name="Charlie Brown", email="charlie@example.com", phone_number="111-222-3333")

country1 = Country(country_name="France")
country2 = Country(country_name="Italy")
country3 = Country(country_name="Spain")

tour1 = Tour(tour_name="Romantic Paris", start_date=date(2024, 1, 15), end_date=date(2024, 1, 22), price=1500.00)
tour2 = Tour(tour_name="Italian Adventure", start_date=date(2024, 2, 1), end_date=date(2024, 2, 10), price=1800.00)
tour3 = Tour(tour_name="Spanish Fiesta", start_date=date(2024, 3, 10), end_date=date(2024, 3, 17), price=1200.00)
tour4 = Tour(tour_name="European Getaway", start_date=date(2024, 4, 1), end_date=date(2024, 4, 15), price=2500.00)

tour1.countries = [country1]
tour2.countries = [country2]
tour3.countries = [country3]
tour4.countries = [country1, country2, country3]

session.add_all([client1, client2, client3, country1, country2, country3, tour1, tour2, tour3, tour4])
session.commit() 

session.execute(client_tour.insert().values(client_id=client1.client_id, tour_id=tour1.tour_id, booking_date=date(2023, 12, 10)))
session.execute(client_tour.insert().values(client_id=client1.client_id, tour_id=tour2.tour_id, booking_date=date(2023, 12, 15)))
session.execute(client_tour.insert().values(client_id=client2.client_id, tour_id=tour2.tour_id, booking_date=date(2023, 11, 20)))
session.execute(client_tour.insert().values(client_id=client2.client_id, tour_id=tour3.tour_id, booking_date=date(2023, 11, 25)))
session.execute(client_tour.insert().values(client_id=client3.client_id, tour_id=tour1.tour_id, booking_date=date(2023, 10, 5)))
session.execute(client_tour.insert().values(client_id=client3.client_id, tour_id=tour4.tour_id, booking_date=date(2023, 10, 10)))

session.commit() 

clients = session.query(Client).all()
print("All Clients:")
for client in clients:
    print(client)

session.close()
