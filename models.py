""" Modelle für Datenbank-Objekte

    author: Emma Müller
    date: 14.11.2022
    version: 1.1.0
    licence: free (open source)
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Table   # help to define model attributes
from sqlalchemy.orm import relationship, backref                    # create relationships between objects
from sqlalchemy.ext.declarative import declarative_base             # connects the database engine to the SQLAlchemy functionality of the models

# creates Base class (what all models inherit from & how they get SQLAlcheny ORM functionality)
Base = declarative_base()


class Student(Base):
    __tablename__ = "student"
    student_id = Column(Integer,primary_key=True)
    vorname = Column(String)
    nachname = Column(String)
    kurs_id = Column(Integer, ForeignKey("kurs.kurs_id"))
    kurs = relationship("Kurs", backref="studenten")
    passwort = Column(String)
    pruefungsleistungen = relationship("Veranstaltung", back_populates="student")

class Kurs(Base):
    __tablename__ = "kurs"
    kurs_id = Column(Integer,primary_key=True)
    name = Column(String)
    dozent_id = Column(Integer, ForeignKey("dozent.dozent_id"))
    studenten = relationship("Student", back_populates="kurs")
    module = relationship("Modul", back_populates="kurs")

class Dozent(Base):
    __tablename__ = "dozent"
    dozent_id = Column(Integer,primary_key=True)
    vorname = Column(String)
    nachname = Column(String)
    passwort = Column(String)
    veranstaltungen = relationship("Veranstaltung", back_populates="dozent")

class Modul(Base):
    __tablename__ = "modul"
    modul_id = Column(Integer,primary_key=True)
    modulname = Column(String)
    credits = Column(Integer)
    kurs_id = Column(Integer, ForeignKey("kurs.kurs_id"))
    kurs = relationship("Kurs", backref="module")
    veranstaltungen = relationship("Veranstaltung", back_populates="modul")

class Veranstaltung(Base):
    __tablename__ = "veranstaltung"
    veranstaltung_id = Column(Integer,primary_key=True)
    name = Column(String)
    dozent_id = Column(Integer, ForeignKey("dozent.dozent_id"))
    dozent = relationship("Dozent", backref="veranstaltungen")
    modul_id = Column(Integer, ForeignKey("modul.modul_id"))
    modul = relationship("Modul", backref="veranstaltungen")
    studenten = relationship("Pruefungsleistung", back_populates="veranstaltung")

class Admin(Base):
    __tablename__ = "admin"
    admin_id = Column(Integer,primary_key=True)
    vorname = Column(String)
    nachname = Column(String)
    passwort = Column(String)


class Pruefungsleistung(Base):
    __tablename__ = "pruefungsleistung"
    student_id = Column(Integer, ForeignKey("student.student_id"), primary_key=True)
    veranstaltung_id = Column(Integer, ForeignKey("veranstaltung.veranstaltung_id"), primary_key=True)
    punkte_gesamt = Column(Integer)
    punkte_erreicht = Column(Integer)
