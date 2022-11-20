from sqlalchemy import Column, Integer, String, create_engine, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker



Base = declarative_base()

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(50))
