# from sqlalchemy import Column, Integer, String, create_engine, Float, DateTime
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# Base = declarative_base()
# Session = sessionmaker()
#
#
#
# class Student(Base):
#     __tablename__ = "student"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(50))
#     last_name = Column(String(50))
#     PESEL = Column(Integer, unique=True)
#     phone = Column(Integer)
#     address = Column(Integer)
#
#
# class StudentGrade(Base):
#     __tablename__ = "studentgrade"
#     enrollment_id = Column(Integer, primary_key=True)
#     student_id = Column(Integer)
#     course_id = Column(Integer)
#     grade = Column(Integer)
#
#
# class Course(Base):
#     __tablename__ = "course"
#     course_id = Column(Integer, primary_key=True)
#     title = Column(String(50))
#     credits = Column(String(50))
#     department_id = Column(Integer)
#     start_date = Column(DateTime)
#     end_date = Column(DateTime)
#     price = Column(Float)
#
#
# class OnlineCourse(Base):
#     __tablename__ = "onlinecourse"
#     course_id = Column(Integer, primary_key=True)
#     url = Column(String(50))
#
#
# class OnsiteCourse(Base):
#     __tablename__ = "onsitecourse"
#     course_id = Column(Integer, primary_key=True)
#     address = Column(String(50))
#     days = Column(Integer)
#     time = Column(Integer)
#
#
# class CourseInstructor(Base):
#     __tablename__ = "courseInstructor"
#     course_id = Column(Integer, primary_key=True)
#     stuff_id = Column(Integer)
#     enrollment_date = Column(Integer)
#
#
# class Department(Base):
#     __tablename__ = "department"
#     id = Column(Integer, primary_key=True)
#     name = Column(String(50))
#     budget = Column(Integer)
#     address = Column(String(50))
#
#
# class Administraor(Base):
#     __tablename__ = "administraor"
#     stuff_id = Column(Integer, primary_key=True)
#     department_id = Column(Integer)
#     enrollment_date = Column(Integer)
#
#
# class Staff(Base):
#     __tablename__ = "staff"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String(50))
#     last_name = Column(String(50))
#     enrollment_date = Column(Integer)
#     PESEL = Column(Integer, unique=True)
#     phone = Column(Integer)
#     address = Column(Integer)
#
#
#
# if __name__ == '__main__':
#     engine = create_engine("mysql+pymysql://root:bFfm420zIOlo#$@localhost:3306/dropthehell")
#     Session.configure(bind=engine)
#     Base.metadata.create_all(engine)
#     session = Session()