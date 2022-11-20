from datetime import datetime

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


class Onlinecourse(Base):
    __tablename__ = "online_course"

    id = Column(Integer, primary_key=True)
    url = Column(String(50), nullable=False)

class Studentgrade(Base):
    __tablename__ = "studentgrade"
    enrollment_id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    grade = Column(Integer)


class Course(Base):
    __tablename__ = "course"
    course_id = Column(Integer, primary_key=True)
    title = Column(String(50))
    credits = Column(String(50))
    department_id = Column(Integer)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    price = Column(Float)



class OnsiteCourse(Base):
    __tablename__ = "onsitecourse"
    course_id = Column(Integer, primary_key=True)
    address = Column(String(50))
    time = Column(String(10), nullable=False)
    days = Column(Integer, nullable=False)

class Onlinecourse(Base):
    __tablename__ = "onlinecourse"
    course_id = Column(Integer, primary_key=True)
    url = Column(String(50))

class CourseInstructor(Base):
    __tablename__ = "courseInstructor"
    course_id = Column(Integer, primary_key=True)
    stuff_id = Column(Integer)
    enrollment_date = Column(DateTime, nullable=False, default=datetime.now())


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    budget = Column(Integer)
    address = Column(String(50))


class Administraor(Base):
    __tablename__ = "administraor"
    stuff_id = Column(Integer, primary_key=True)
    department_id = Column(Integer)
    enrollment_date = Column(DateTime, nullable=False, default=datetime.now())


class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    enrollment_date = Column(DateTime, nullable=False, default=datetime.now())
    pesel = Column(String(11), unique=True, nullable=False)
    phone = Column(Integer)
    address = Column(Integer)
