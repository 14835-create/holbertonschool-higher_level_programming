#!/usr/bin/python3
"""Lists all city object grouped by state."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    Cities = session.query(State, City).join(
            State, State.id == City.state_id).order_by(City.id).all()

    for state, city in Cities:
    print("{}: ({}) {}".format(states.name, city.id, city.name))

    session.close()
