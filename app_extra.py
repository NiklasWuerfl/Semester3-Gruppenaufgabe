""" Modul für API

    author: Emma Müller
    date: 09.11.2022
    version: 1.1.0
    licence: free (open source)
"""

from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *
import models as my_data
import database as db
import test_frontend as tf

SQLALCHEMY_DATABASE_URL = "sqlite:///data.db/?check_same_thread=False"

# create the Flask application object
app = Flask("app")
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# initialise app with the extension
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
my_data.Base.metadata.drop_all(engine)
my_data.Base.metadata.create_all(engine)


@app.route('/')
def hello():
    return 'hello :)'


#@app.route('/signup/<string:nutzername>/<string:passwort>', methods=['GET'])
#def anmeldung(username: str, passwort: str):

#@app.route('/logout/')
#def abmeldung():
#    return1

@app.route('/createStudent/<int:student_id>/<string:vorname>/<string:nachname>/<int:kurs_id>/<string:nutzername>/<string:passwort>', methods=['GET'])
def createStudent(student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str):
    student = session.execute(Student).filter_by(student_id=student_id).first()

    if student:
        return 'Es existiert bereits ein Student mit dieser ID!'
    else:
        neuerStudent = Student(student_id=student_id,vorname=vorname,nachname=nachname,kurs_id=kurs_id,nutzername=nutzername,passwort=passwort)
        session.add(neuerStudent)
        session.commit()
        return 'Student wurde erfolgreich angelegt!'

@app.route('/createKurs/<int:kurs_id>/<string:name>/<int:dozent_id>', methods=['GET'])
def createKurs(kurs_id: int, name: str, dozent_id: int):
    kurs = session.execute(Kurs).filter_by(kurs_id=kurs_id).first()

    if kurs:
        return 'Es existiert bereits ein Kurs mit dieser ID!'
    else:
        neuerKurs = Kurs(kurs_id=kurs_id,name=name,dozent_id=dozent_id)
        session.add(neuerKurs)
        session.commit()
        return 'Kurs wurde erfolgreich angelegt!'

@app.route('/createDozent/<int:dozent_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def createDozent(dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    dozent = session.execute(Dozent).filter_by(dozent_id=dozent_id).first()

    if dozent:
        return 'Es existiert bereits ein Dozent mit dieser ID!'
    else:
        neuerDozent = Dozent(dozent_id=dozent_id,vorname=vorname,nachname=nachname,nutzername=nutzername,passwort=passwort)
        session.add(neuerDozent)
        session.commit()
        return 'Dozent wurde erfolgreich angelegt!'

@app.route('/createModul/<int:modul_id>/<string:modulname>/<int:credits>/<int:kurs_id>', methods=['GET'])
def createModul(modul_id: int, modulname: str, credits: int, kurs_id: int):
    modul = session.execute(Modul).filter_by(modul_id=modul_id).first()

    if modul:
        return 'Es existiert bereits ein Modul mit dieser ID!'
    else:
        neuesModul = Modul(modul_id=modul_id,modulname=modulname,credits=credits,kurs_id=kurs_id)
        session.add(neuesModul)
        session.commit()
        return 'Modul wurde erfolgreich angelegt!'

@app.route('/createVeranstaltung/<int:veranstaltung_id>/<string:name>/<int:dozent_id>/<int:modul_id>', methods=['GET'])
def createVeranstaltung(veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    veranstaltung = session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung_id).first()

    if veranstaltung:
        return 'Es existiert bereits eine Veranstaltung mit dieser ID!'
    else:
        neueVeranstaltung = Veranstaltung(veranstaltung_id=veranstaltung_id,name=name,dozent_id=dozent_id,modul_id=modul_id)
        session.add(neueVeranstaltung)
        session.commit()
        return 'Veranstaltung wurde erfolgreich angelegt!'

@app.route('/createPruefungsleistung/<int:student_id>/<int:veranstaltung_id>/<int:punkte_gesamt>/<int:punkte_erreicht>', methods=['GET'])
def createPruefungsleistung(student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    pruefungsleistung = session.execute(Pruefungsleistung).filter_by(student_id=student_id,veranstaltung_id=veranstaltung_id).first()

    if pruefungsleistung:
        return 'Es existiert bereits ein Prüfungsleistung dieses Studenten für diese Veranstaltung!'
    else:
        neuePruefungsleistung = Pruefungsleistung(student_id=student_id,veranstaltung_id=veranstaltung_id,punkte_gesamt=punkte_gesamt,punkte_erreicht=punkte_erreicht)
        session.add(neuePruefungsleistung)
        session.commit()
        return 'Prüfungsleistung wurde erfolgreich angelegt!'

@app.route('/createAdmin/<int:admin_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def createAdmin(admin_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    admin = session.execute(Admin).filter_by(admin_id=admin_id).first()

    if admin:
        return 'Es existiert bereits ein Admin mit dieser ID!'
    else:
        neuerAdmin = Admin(admin_id=admin_id,vorname=vorname,nachname=nachname,nutzername=nutzername,passwort=passwort)
        session.add(neuerAdmin)
        session.commit()
        return 'Admin wurde erfolgreich angelegt!'

@app.route('/deleteStudent/<int:student_id>', methods=['GET'])
def deleteStudent(student_id: int):
    student = session.execute(Student).filter_by(student_id=student_id).first()

    if student:
        session.execute(Student).filter_by(student_id=student_id).delete()
        session.execute(Pruefungsleistung).filter_by(student_id=student_id).delete()
        return 'Der Student und alle zugehörigen Prüfungsleistungen wurden gelöscht!'
    else:
        return 'Dieser Student existiert nicht!'

@app.route('/deleteKurs/<int:kurs_id>', methods=['GET'])
def deleteKurs(kurs_id: int):
    kurs = session.execute(Kurs).filter_by(kurs_id=kurs_id).first()

    if kurs:
        session.execute(Kurs).filter_by(kurs_id=kurs_id).delete()
        session.execute(Modul).filter_by(kurs_id=kurs_id).delete()
        veranstaltungen_query = session.execute(Veranstaltung).filter_by(kurs_id=kurs_id).scalars()
        veranstaltungen = veranstaltungen_query.statement.execute().fetchall()
        for veranstaltung in veranstaltungen:
            session.execute(Pruefungsleistung).filter_by(veranstaltung.veranstaltung_id).delete()
            session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung.veranstaltung_id).delete()
        session.execute(Student).filter_by(kurs_id=kurs_id).delete()
        return 'Der Kurs und alle zugehörigen Module, Veranstaltungen, Prüfungsleistungen und Studenten wurden gelöscht!'
    else:
        return 'Dieser Kurs existiert nicht!'

@app.route('/deleteDozent/<int:dozent_id>', methods=['GET'])
def deleteDozent(dozent_id: int):
    dozent = session.execute(Dozent).filter_by(dozent_id=dozent_id).first()

    if dozent:
        session.execute(Dozent).filter_by(dozent_id=dozent_id).delete()
        veranstaltungen_query = session.execute(Veranstaltung).filter_by(dozent_id=dozent_id).delete()
        veranstaltungen = veranstaltungen_query.statement.execute().fetchall()
        for veranstaltung in veranstaltungen:
            session.execute(Pruefungsleistung).filter_by(veranstaltung.veranstaltung_id).delete()
            session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung.veranstaltung_id).delete()
        return 'Der Dozent und alle seine Veranstaltungen und Prüfungsleistungen wurden gelöscht!'
    else:
        return 'Dieser Dozent existiert nicht!'

@app.route('/deleteModul/<int:modul_id>', methods=['GET'])
def deleteModul(modul_id: int):
    modul = session.execute(Modul).filter_by(modul_id=modul_id).first()

    if modul:
        session.execute(Modul).filter_by(modul_id=modul_id).delete()
        veranstaltungen_query = session.execute(Veranstaltung).filter_by(modul_id=modul_id)
        veranstaltungen = veranstaltungen_query.statement.execute().fetchall()
        for veranstaltung in veranstaltungen:
            session.execute(Pruefungsleistung).filter_by(veranstaltung.veranstaltung_id).delete()
            session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung.veranstaltung_id).delete()
        return 'Das Modul und alle zugehörigen Veranstaltungen und Prüfungsleistungen wurden gelöscht!'
    else:
        return 'Dieses Modul existiert nicht!'

@app.route('/deleteVeranstaltung/<int:veranstaltung_id>', methods=['GET'])
def deleteVeranstaltung(veranstaltung_id: int):
    veranstaltung = session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung_id).first()

    if veranstaltung:
        session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung_id).delete()
        session.execute(Pruefungsleistung).filter_by(veranstaltung_id=veranstaltung_id).delete()
        return 'Diese Veranstaltung und alle zugehörigen Prüfungsleistungen wurden gelöscht!'
    else:
        return 'Diese Veranstaltung existiert nicht!'

@app.route('/deletePruefungsleistung/<int:student_id>/<int:veranstaltung_id>', methods=['GET'])
def deletePruefungsleistung(student_id: int, veranstaltung_id: int):
    pruefungsleistung = session.execute(Pruefungsleistung).filter_by(student_id=student_id, veranstaltung_id=veranstaltung_id).first()

    if pruefungsleistung:
        session.execute(Pruefungsleistung).filter_by(student_id=student_id,veranstaltung_id=veranstaltung_id).delete()
        return 'Diese Prüfungsleistung wurde gelöscht!'
    else:
        return 'Diese Prüfungsleistung existiert nicht!'

@app.route('/deleteAdmin/<int:admin_id>', methods=['GET'])
def deleteAdmin(admin_id: int):
    admin = session.execute(Admin).filter_by(admin_id=admin_id).first()

    if admin:
        session.execute(Admin).filter_by(admin_id=admin_id).delete()
        return 'Dieser Admin wurde gelöscht!'
    else:
        return 'Dieser Admin existiert nicht!'

@app.route('/changeStudent/<int:student_id_old>/<int:student_id>/<string:vorname>/<string:nachname>/<int:kurs_id>/<string:nutzername>/<string:passwort>', methods=['GET'])
def changeStudent(student_id_old: int, student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str):
    student = session.execute(Student).filter_by(student_id=student_id_old).first()

    if student:
        student.student_id = student_id
        student.vorname = vorname
        student.nachname = nachname
        student.kurs_id = kurs_id
        student.nutzername = nutzername
        student.passwort = passwort
        session.commit()
        return 'Student wurde bearbeitet!'
    else:
        return 'Es existiert kein Student mit dieser ID!'

@app.route('/changeKurs/<int:kurs_id_old>/<int:kurs_id>/<string:name>/<int:dozent_id>', methods=['GET'])
def changeKurs(kurs_id_old: int,kurs_id: int, name: str, dozent_id: int):
    kurs = session.execute(Kurs).filter_by(kurs_id=kurs_id_old).first()

    if kurs:
        kurs.kurs_id = kurs_id
        kurs.name = name
        kurs.dozent_id = dozent_id
        session.commit()
        return 'Kurs wurde bearbeitet!'
    else:
        return 'Es existiert kein Kurs mit dieser ID!'

@app.route('/changeDozent/<int:dozent_id_old>/<int:dozent_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def changeDozent(dozent_id_old: int,dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    dozent = session.execute(Dozent).filter_by(dozent_id=dozent_id_old).first()

    if dozent:
        dozent.dozent_id = dozent_id
        dozent.vorname = vorname
        dozent.nachname = nachname
        dozent.nutzername = nutzername
        dozent.passwort = passwort
        session.commit()
        return 'Dozent wurde bearbeitet!'
    else:
        return 'Es existiert kein Dozent mit dieser ID!'

@app.route('/changeModul/<int:modul_id_old>/<int:modul_id>/<string:modulname>/<int:credits>/<int:kurs_id>', methods=['GET'])
def changeModul(modul_id_old: int, modul_id: int, modulname: str, credits: int, kurs_id: int):
    modul = session.execute(Modul).filter_by(modul_id=modul_id_old).first()

    if modul:
        modul.modul_id = modul_id
        modul.modulname = modulname
        modul.credits = credits
        modul.kurs_id = kurs_id
        session.commit()
        return 'Modul wurde bearbeitet!'
    else:
        return 'Es existiert kein Modul mit dieser ID!'

@app.route('/changeVeranstaltung/<int:veranstaltung_id_old>/<int:veranstaltung_id>/<string:name>/<int:dozent_id>/<int:modul_id>', methods=['GET'])
def changeVeranstaltung(veranstaltung_id_old: int, veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    veranstaltung = session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung_id_old).first()

    if veranstaltung:
        veranstaltung.veranstaltung_id = veranstaltung_id
        veranstaltung.name = name
        veranstaltung.dozent_id = dozent_id
        veranstaltung.modul_id = modul_id
        session.commit()
        return 'Veranstaltung wurde bearbeitet!'
    else:
        return 'Es existiert keine Veranstaltung mit dieser ID!'

@app.route('/changePruefungsleistung/<int:student_id_old>/<int:veranstaltung_id_old>/<int:student_id>/<int:veranstaltung_id>/<int:punkte_gesamt>/<int:punkte_erreicht>', methods=['GET'])
def changePruefungsleistung(student_id_old: int, veranstaltung_id_old: int, student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    pruefungsleistung = session.execute(Pruefungsleistung).filter_by(student_id=student_id_old,veranstaltung_id=veranstaltung_id_old).first()

    if pruefungsleistung:
        pruefungsleistung.student_id = student_id
        pruefungsleistung.veranstaltung_id = veranstaltung_id
        pruefungsleistung.punkte_gesamt = punkte_gesamt
        pruefungsleistung.punkte_erreicht = punkte_erreicht
        session.commit()
        return 'Prüfungsleistung wurde bearbeitet!'
    else:
        return 'Es existiert keine Prüfungsleistung von diesem Studenten in dieser Veranstaltung!'

@app.route('/changeAdmin/<int:admin_id_old>/<int:admin_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def changeAdmin(admin_id_old: int, admin_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    admin = session.execute(Admin).filter_by(admin_id=admin_id_old).first()

    if admin:
        admin.admin_id = admin_id
        admin.vorname = vorname
        admin.nachname = nachname
        admin.nutzername = nutzername
        admin.passwort = passwort
        session.commit()
        return 'Admin wurde bearbeitet!'
    else:
        return 'Es existiert kein Admin mit dieser ID!'

@app.route('/getStudent/<int:student_id>', methods=["GET"])
def getStudent(student_id: int):
    student = session.execute(Student).filter_by(student_id=student_id).first()

    if student:
        return [student.student_id,student.vorname,student.nachname,student.kurs_id,student.nutzername,student.passwort]
    else:
        return 'Es existiert kein Student mit dieser ID!'

@app.route('/getKurs/<int:kurs_id>', methods=["GET"])
def getKurs(kurs_id: int):
    kurs = session.execute(Kurs).filter_by(kurs_id=kurs_id).first()

    if kurs:
        return [kurs.kurs_id,kurs.name,kurs.dozent_id]
    else:
        return 'Es existiert kein Kurs mit dieser ID!'

@app.route('/getDozent/<int:dozent_id>', methods=["GET"])
def getDozent(dozent_id: int):
    dozent = session.execute(Dozent).filter_by(dozent_id=dozent_id).first()

    if dozent:
        return [dozent.dozent_id,dozent.vorname,dozent.nachname,dozent.nutzername,dozent.passwort]
    else:
        return 'Es existiert kein Dozent mit dieser ID!'

@app.route('/getModul/<int:modul_id>', methods=["GET"])
def getModul(modul_id: int):
    modul = session.execute(Modul).filter_by(modul_id=modul_id).first()

    if modul:
        return [modul.modul_id,modul.modulname,modul.credits,modul.kurs_id]
    else:
        return 'Es existiert kein Modul mit dieser ID!'

@app.route('/getVeranstaltung/<int:veranstaltung_id>', methods=["GET"])
def getVeranstaltung(veranstaltung_id: int):
    veranstaltung = session.execute(Veranstaltung).filter_by(veranstaltung_id=veranstaltung_id).first()

    if veranstaltung:
        return [veranstaltung.veranstaltung_id,veranstaltung.name,veranstaltung.dozent_id,veranstaltung.modul_id]
    else:
        return 'Es existiert keine Veranstaltung mit dieser ID!'

@app.route('/getPruefungsleistung/<int:student_id>/<int:veranstaltung_id>', methods=["GET"])
def getPruefungsleistung(student_id: int, veranstaltung_id: int):
    pruefungsleistung = session.execute(Pruefungsleistung).filter_by(student_id=student_id,veranstaltung_id=veranstaltung_id).first()

    if pruefungsleistung:
        return [pruefungsleistung.student_id,pruefungsleistung.veranstaltung_id,pruefungsleistung.punkte_gesamt,pruefungsleistung.punkte_erreicht]
    else:
        return 'Es existiert keine Prüfungsleistung von diesem Studenten in dieser Veranstaltung!'

@app.route('/getAdmin/<int:kurs_id>', methods=["GET"])
def getAdmin(admin_id: int):
    admin = session.execute(Admin).filter_by(admin_id=admin_id).first()

    if admin:
        return [admin.admin_id,admin.vorname,admin.nachname,admin.nutzername,admin.passwort]
    else:
        return 'Es existiert kein Admin mit dieser ID!'

@app.route('/getPruefungsleistungenByStudent/<int:student_id>', methods=["GET"])
def getPruefungsleistungenByStudent(student_id: int):
    student = session.execute(Student).filter_by(student_id=student_id).first()

    if student:
        pruefungsleistungen_query = session.execute(Pruefungsleistung).filter_by(student_id=student_id)
        pruefungsleistungen = pruefungsleistungen_query.statement.execute().fetchall()
        counter = 0
        return_values = []
        for pruefungsleistung in pruefungsleistungen:
            pl = session.execute(Pruefungsleistung).filter_by(pruefungsleistung.student_id).first()
            return_values[counter] = [pl.student_id,pl.veranstaltung_id,pl.punkte_gesamt,pl.punke_erreicht]
            counter += counter
        return return_values
    else:
        return 'Es existiert kein Student mit dieser ID!'


if __name__ == '__main__':
    db.fill_testdatabase(db.create_database_connection("data.db"))
    app.run(debug=True)
    
