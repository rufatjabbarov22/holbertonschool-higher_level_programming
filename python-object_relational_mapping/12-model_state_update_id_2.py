#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def update_state(username, password, database):
    try:

        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)


        Session = sessionmaker(bind=engine)
        session = Session()


        state_to_update = session.query(State).filter_by(id=2).first()


        if state_to_update:

            state_to_update.name = "New Mexico"


            session.commit()


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


    update_state(username, password, database)

