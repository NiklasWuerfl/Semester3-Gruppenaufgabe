""" Modul für API mit database.py

    author: Emma Müller
    date: 09.11.2022
    version: 1.0.0
    licence: free (open source)
"""

from flask import Flask

import Student_be
import database as db

# create the Flask application object
app = Flask("app")
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'data.db' + '?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# database elements
DATABASE_FILE = "data.db"
my_connect = db.create_database_connection(DATABASE_FILE)
my_cursor = my_connect.cursor()


# create index page (login)
@app.route('/')
def index():
    return 'hello my friends :)'


#@app.route('/signup/<string:nutzername>/<string:passwort>', methods=['GET'])
#def anmeldung(username: str, passwort: str):

@app.route('/logout/')
def abmeldung():
   return 'du bist abgemeldet'

@app.route('/createStudent/<int:student_id>/<string:vorname>/<string:nachname>/<int:kurs_id>/<string:nutzername>/<string:passwort>', methods=['GET'])
def createStudent(student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str):
    return db.create_student(my_connect,[student_id,vorname,nachname,kurs_id,nutzername,passwort])

@app.route('/createKurs/<int:kurs_id>/<string:name>/<int:dozent_id>', methods=['GET'])
def createKurs(kurs_id: int, name: str, dozent_id: int):
    return db.create_kurs(my_connect, [kurs_id,name,dozent_id])

@app.route('/createDozent/<int:dozent_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def createDozent(dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    return db.create_dozent(my_connect, [dozent_id,vorname,nachname,nutzername,passwort])

@app.route('/createModul/<int:modul_id>/<string:modulname>/<int:credits>/<int:kurs_id>', methods=['GET'])
def createModul(modul_id: int, modulname: str, credits: int, kurs_id: int):
    return db.create_modul(my_connect, [modul_id,modulname,credits,kurs_id])

@app.route('/createVeranstaltung/<int:veranstaltung_id>/<string:name>/<int:dozent_id>/<int:modul_id>', methods=['GET'])
def createVeranstaltung(veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    return db.create_veranstaltung(my_connect, [veranstaltung_id,name,dozent_id,modul_id])

@app.route('/createPruefungsleistung/<int:student_id>/<int:veranstaltung_id>/<int:punkte_gesamt>/<int:punkte_erreicht>', methods=['GET'])
def createPruefungsleistung(student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    return db.create_pruefungsleistung(my_connect, [student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht])

@app.route('/createAdmin/<int:admin_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def createAdmin(admin_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    return db.create_admin(my_connect, [admin_id,vorname,nachname,nutzername,passwort])

@app.route('/deleteStudent/<int:student_id>', methods=['GET'])
def deleteStudent(student_id: int):
    return db.delete_student(my_connect, student_id)

@app.route('/deleteKurs/<int:kurs_id>', methods=['GET'])
def deleteKurs(kurs_id: int):
    return db.delete_kurs(my_connect, kurs_id)

@app.route('/deleteDozent/<int:dozent_id>', methods=['GET'])
def deleteDozent(dozent_id: int):
    return db.delete_dozent(my_connect, dozent_id)

@app.route('/deleteModul/<int:modul_id>', methods=['GET'])
def deleteModul(modul_id: int):
    return db.delete_modul(my_connect, modul_id)

@app.route('/deleteVeranstaltung/<int:veranstaltung_id>', methods=['GET'])
def deleteVeranstaltung(veranstaltung_id: int):
    return db.delete_veranstaltung(my_connect, veranstaltung_id)

@app.route('/deletePruefungsleistung/<int:student_id>/<int:veranstaltung_id>', methods=['GET'])
def deletePruefungsleistung(student_id: int, veranstaltung_id: int):
    return db.delete_pruefungsleistung(my_connect, student_id,veranstaltung_id)

@app.route('/deleteAdmin/<int:admin_id>', methods=['GET'])
def deleteAdmin(admin_id: int):
    return db.delete_admin(my_connect, admin_id)

@app.route('/changeStudent/<int:student_id_old>/<int:student_id>/<string:vorname>/<string:nachname>/<int:kurs_id>/<string:nutzername>/<string:passwort>', methods=['GET'])
def changeStudent(student_id_old: int, student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str):
    return db.edit_student_by_id(my_connect, student_id_old, [student_id,vorname,nachname,kurs_id,nutzername,passwort])

@app.route('/changeKurs/<int:kurs_id_old>/<int:kurs_id>/<string:name>/<int:dozent_id>', methods=['GET'])
def changeKurs(kurs_id_old: int,kurs_id: int, name: str, dozent_id: int):
    return db.edit_kurs_by_id(my_connect, kurs_id_old, [kurs_id,name,dozent_id])

@app.route('/changeDozent/<int:dozent_id_old>/<int:dozent_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def changeDozent(dozent_id_old: int,dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    return db.edit_dozent_by_id(my_connect, dozent_id_old, [dozent_id,vorname,nachname,nutzername,passwort])

@app.route('/changeModul/<int:modul_id_old>/<int:modul_id>/<string:modulname>/<int:credits>/<int:kurs_id>', methods=['GET'])
def changeModul(modul_id_old: int, modul_id: int, modulname: str, credits: int, kurs_id: int):
    return db.edit_modul_by_id(my_connect, modul_id_old, [modul_id,modulname,credits,kurs_id])

@app.route('/changeVeranstaltung/<int:veranstaltung_id_old>/<int:veranstaltung_id>/<string:name>/<int:dozent_id>/<int:modul_id>', methods=['GET'])
def changeVeranstaltung(veranstaltung_id_old: int, veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    return db.edit_veranstaltung_by_id(my_connect, veranstaltung_id_old, [veranstaltung_id,name,dozent_id,modul_id])

@app.route('/changePruefungsleistung/<int:student_id_old>/<int:veranstaltung_id_old>/<int:student_id>/<int:veranstaltung_id>/<int:punkte_gesamt>/<int:punkte_erreicht>', methods=['GET'])
def changePruefungsleistung(student_id_old: int, veranstaltung_id_old: int, student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    return db.edit_pruefungsleistung_by_student_and_veranstaltung(my_connect, student_id_old, veranstaltung_id_old, [student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht])

@app.route('/changeAdmin/<int:admin_id_old>/<int:admin_id>/<string:vorname>/<string:nachname>/<string:nutzername>/<string:passwort>', methods=['GET'])
def changeAdmin(admin_id_old: int, admin_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    return db.edit_admin_by_id(my_connect, admin_id_old, [admin_id,vorname,nachname,nutzername,passwort])

@app.route('/getStudent/<int:student_id>', methods=["GET"])
def getStudent(student_id: int):
    return db.get_student_by_id(my_connect, student_id)

@app.route('/getKurs/<int:kurs_id>', methods=["GET"])
def getKurs(kurs_id: int):
    return db.get_kurs_by_id(my_connect, kurs_id)

@app.route('/getDozent/<int:dozent_id>', methods=["GET"])
def getDozent(dozent_id: int):
    return db.get_dozent_by_id(my_connect, dozent_id)

@app.route('/getModul/<int:modul_id>', methods=["GET"])
def getModul(modul_id: int):
    return db.get_modul_by_id(my_connect, modul_id)

@app.route('/getVeranstaltung/<int:veranstaltung_id>', methods=["GET"])
def getVeranstaltung(veranstaltung_id: int):
    return db.get_veranstaltung_by_id(my_connect, veranstaltung_id)

@app.route('/getPruefungsleistung/<int:student_id>/<int:veranstaltung_id>', methods=["GET"])
def getPruefungsleistung(student_id: int, veranstaltung_id: int):
    return db.get_pruefungsleistung_by_id(my_connect, student_id, veranstaltung_id)

@app.route('/getAdmin/<int:admin_id>', methods=["GET"])
def getAdmin(admin_id: int):
    return db.get_admin_by_id(my_connect, admin_id)

@app.route('/getPruefungsleistungenByStudent/<int:student_id>', methods=["GET"])
def getPruefungsleistungenByStudent(student_id: int):
    return db.get_all_pruefungsleistung_by_student(my_connect, student_id)

@app.route('/ModuleStudent/<int:student_id>', methods= ["GET"])
def getModuleStudent(student_id: int):
    return Student_be.print_student_module(student_id)

@app.route('/PruefungenInModulStudent/<int:student_id>/<int:modul_id>', methods= ["GET"])
def getPruefungenInModulStudent(student_id: int, modul_id):
    return Student_be.print_pruefungen_in_modul(student_id, modul_id)

@app.route('/CreditsStudent/<int:student_id>', methods= ["GET"])
def getCreditsStudent(student_id: int):
    return Student_be.get_credits_erreicht(student_id)

@app.route('/GPAStudent/<int:student_id>', methods= ["GET"])
def getGPAStudent(student_id: int):
    return Student_be.get_gpa_by_student(student_id)

@app.route('/StudentName/<int:student_id>', methods= ["GET"])
def getStudentName(student_id: int):
    return Student_be.get_student_name(student_id)

if __name__ == '__main__':
    db.database_setup(my_connect)
    db.fill_testdatabase(my_connect)
    app.run(debug=True)