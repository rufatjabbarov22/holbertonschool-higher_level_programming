#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def fetch_cities_by_state(username, password, database):
    try:

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)


        Session = sessionmaker(bind=engine)
        session = Session()


        cities = session.query(City).order_by(City.id).all()


        for city in cities:
            print("{}: ({}) {}".format(city.state.name, city.id, city.name))


        session.close()

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]


    fetch_cities_by_state(username, password, database)

