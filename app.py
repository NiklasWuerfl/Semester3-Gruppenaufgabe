""" Modul für API
    - arbeitet mit database.py um Zugriffe auf Datenbank auszuführen

    author: Emma Müller
    date: 01.12.2022
    version: 1.0.2
    licence: free (open source)
"""

from flask import Flask
import database as db

app = Flask("app")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'data.db' + '?check_same_thread=False'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DATABASE_FILE = "data.db"
my_connect = db.create_database_connection(DATABASE_FILE)
my_cursor = my_connect.cursor()


@app.route('/')
def index():
    """Index-Seite um anzuzeigen, ob Server läuft

        Args:
            None

        Returns:
            String: Zeichenkette, die im Browser beim Zugriff auf Adresse angezeigt werden soll

        Test:
            1) Aufrufen der URL 'localhost:5000' während Programm noch nicht gestartet ist
                -> erwartetet Ergebnis:
                    Browser kann nicht mit Server verbinden (sofern kein anderer Server läuft)
            2) Aufrufen der URL 'localhost:5000' nachdem Programm gestartet
                -> erwartetes Ergebnis:
                    Ausgabe 'Der Server für die Verbindung zu Datenbank ist jetzt live!' angezeigt
    """
    return 'Der Server für die Verbindung zur Datenbank ist jetzt live!'


@app.route(
    '/createStudent/<int:student_id>/<string:vorname>/<string:nachname>/'
    '<int:kurs_id>/<string:nutzername>/<string:passwort>',
    methods=['GET'])
def create_student(
        student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str):
    """neuen Student in Tabelle 'Student' einfügen

        Args:
            student_id (int): Studenten-ID des Studenten der angelegt wird
            vorname (str): Vorname des Studenten der angelegt wird
            nachname (str): Nachname des Studenten der angelegt wird
            kurs_id (int): Kurs-ID des Kurses zu dem der Studenten der angelegt wird gehört
            nutzername (str): Nutzername des Studenten der angelegt wird
            passwort (str): Passwort des Studenten der angelegt wird

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_student(my_connect,[student_id,vorname,nachname,kurs_id,nutzername,passwort])


@app.route('/createKurs/<int:kurs_id>/<string:name>/<int:dozent_id>', methods=['GET'])
def create_kurs(kurs_id: int, name: str, dozent_id: int):
    """neuen Kurs in Tabelle 'Kurs' einfügen

        Args:
            kurs_id (int): Kurs-ID des Kurses der angelegt wird
            name (str): Name des Kurses der angelegt wird
            dozent_id (str): Dozent-ID des Dozenten der dem Kurs der angelegt wird als
                Studiengangsleiter zugeordnet ist

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_kurs(my_connect, [kurs_id,name,dozent_id])


@app.route(
    '/createDozent/<int:dozent_id>/<string:vorname>/<string:nachname>/'
    '<string:nutzername>/<string:passwort>',
    methods=['GET'])
def create_dozent(dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    """neuen Dozent in Tabelle 'Dozent' einfügen

        Args:
            dozent_id (int): Dozent-ID des Dozenten der angelegt wird
            vorname (str): Vorname des Dozenten der angelegt wird
            nachname (str): Nachname des Dozenten der angelegt wird
            nutzername (str): Nutzername des Dozenten der angelegt wird
            passwort (str): Passwort des Dozenten der angelegt wird

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_dozent(my_connect, [dozent_id,vorname,nachname,nutzername,passwort])


@app.route(
    '/createModul/<int:modul_id>/<string:modulname>/<int:credits>/<int:kurs_id>',
    methods=['GET'])
def create_modul(modul_id: int, modulname: str, module_credits: int, kurs_id: int):
    """neues Modul in Tabelle 'Modul' einfügen

        Args:
            modul_id (int): Modul-ID des Moduls das angelegt wird
            modulname (str): Name des Moduls das angelegt wird
            credits (int): Credits welche das Modul das angelegt wird Wert ist
            kurs_id (int): Kurs-ID des Kurses zu dem das Modul das angelegt wird gehört

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_modul(my_connect, [modul_id,modulname,module_credits,kurs_id])


@app.route(
    '/createVeranstaltung/<int:veranstaltung_id>/<string:name>/<int:dozent_id>/<int:modul_id>',
    methods=['GET'])
def create_veranstaltung(veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    """neue Veranstaltung in Tabelle 'Veranstaltung' einfügen

        Args:
            veranstaltung_id (int): Veranstaltung-ID der Veranstaltung die angelegt wird
            name (str): Name der Veranstaltung die angelegt wird
            dozent_id (int): Dozent-ID des Dozenten der die Veranstaltung die angelegt
                wird unterrichtet
            modul_id (int): Modul-ID des Moduls zu dem die Veranstaltung die angelegt wird gehört

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_veranstaltung(my_connect, [veranstaltung_id,name,dozent_id,modul_id])


@app.route(
    '/createPruefungsleistung/<int:student_id>/<int:veranstaltung_id>/'
    '<int:punkte_gesamt>/<int:punkte_erreicht>',
    methods=['GET'])
def create_pruefungsleistung(
        student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    """neue Prüfungsleistung in Tabelle 'Pruefungsleistung' einfügen

        Args:
            student_id (int): Studenten-ID des Studenten der die Prüfungleistung die angelegt wird
                abgelegt hat
            veranstaltung_id (int): Veranstaltung-ID der Veranstaltung in der die Prüfungsleistung
                die angelegt wird abgelegt wurde
            punkte_gesamt (int): Punkte die in Prüfungsleistung die angelegt wird maximal
                erreichbar waren
            punkte_erreicht (int): Punkte die in der Prüfungsleisutng die angelegt wird
                tatsächlich erreicht wurden

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_pruefungsleistung(
        my_connect, [student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht])


@app.route(
    '/createAdmin/<int:admin_id>/<string:vorname>/<string:nachname>/'
    '<string:nutzername>/<string:passwort>',
    methods=['GET'])
def create_admin(admin_id: int, vorname: str, nachname: str, nutzername: str, passwort: str):
    """ neuen Admin in Tabelle 'Admin' einfügen

        Args:
            admin_id (int): SAdmin-ID des Admins der angelegt wird
            vorname (str): Vorname des Admins der angelegt wird
            nachname (str): Nachname des Admins der angelegt wird
            nutzername (str): Nutzername des Admins der angelegt wird
            passwort (str): Passwort des Admins der angelegt wird

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * neuer Student mit erhaltenen Eingabeparametern als Attributwerte in Datenbank
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.create_admin(my_connect, [admin_id,vorname,nachname,nutzername,passwort])


@app.route('/deleteStudent/<int:student_id>', methods=['GET'])
def delete_student(student_id: int):
    """ Student aus Tabelle 'Student' entfernen

        Args:
            student_id (int): Studenten-ID des Studenten der gelöscht werden soll

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Student mit erhaltener Student-ID aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_student(my_connect, student_id)


@app.route('/deleteKurs/<int:kurs_id>', methods=['GET'])
def delete_kurs(kurs_id: int):
    """ Kurs aus Tabelle 'Kurs' entfernen

        Args:
            kurs_id (int): Kurs-ID des Kurses der gelöscht werden soll

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Kurs mit erhaltener Kurs-ID aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_kurs(my_connect, kurs_id)


@app.route('/deleteDozent/<int:dozent_id>', methods=['GET'])
def delete_dozent(dozent_id: int):
    """ Dozent aus Tabelle 'Dozent' entfernen

        Args:
            dozent_id (int): Dozent-ID des Dozenten der gelöscht werden soll

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Dozent mit erhaltener Dozent-ID aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_dozent(my_connect, dozent_id)


@app.route('/deleteModul/<int:modul_id>', methods=['GET'])
def delete_modul(modul_id: int):
    """ Modul aus Tabelle 'Modul' entfernen

        Args:
            modul_id (int): Modul-ID des Moduls das gelöscht werden soll

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Modul mit erhaltener Modul-ID aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_modul(my_connect, modul_id)


@app.route('/deleteVeranstaltung/<int:veranstaltung_id>', methods=['GET'])
def delete_veranstaltung(veranstaltung_id: int):
    """ Veranstaltung aus Tabelle 'Veranstaltung' entfernen

        Args:
            veranstaltung_id (int): Veranstaltung-ID der Veranstaltung die gelöscht werden soll

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Veranstaltung mit erhaltener Veranstaltung-ID aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_veranstaltung(my_connect, veranstaltung_id)


@app.route('/deletePruefungsleistung/<int:student_id>/<int:veranstaltung_id>', methods=['GET'])
def delete_pruefungsleistung(student_id: int, veranstaltung_id: int):
    """ Prüfungsleistung aus Tabelle 'Pruefungsleistung' entfernen

        Args:
            student_id (int): Studenten-ID des Studenten der Prüfungsleistung die gelöscht
                werden soll abgelegt hat
            veranstaltung_id (int): Veranstaltung-ID der Veranstaltung in der Prüfungsleistung
                die gelöscth werden sol abgelegt wurde

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Prüfungsleistung mit erhaltener Student-ID & Veranstaltung-ID
                        aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_pruefungsleistung(my_connect, student_id,veranstaltung_id)


@app.route('/deleteAdmin/<int:admin_id>', methods=['GET'])
def delete_admin(admin_id: int):
    """ Admin aus Tabelle 'Admin' entfernen

        Args:
            admin_id (int): Admin-ID des Admins der gelöscht werden soll

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Admin mit erhaltener Admin-ID aus Datenbank entfernt
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.delete_admin(my_connect, admin_id)


@app.route(
    '/changeStudent/<int:student_id_old>/<int:student_id>/<string:vorname>/<string:nachname>/'
    '<int:kurs_id>/<string:nutzername>/<string:passwort>',
    methods=['GET'])
def change_student(
        student_id_old: int, student_id: int, vorname: str, nachname: str,
        kurs_id: int, nutzername: str, passwort:str):
    """ Attributwerte eines Studenten aus Tabelle 'Student' verändern

        Args:
            student_id_old (int): bisherige Studenten-ID des Studenten der verändert wird
            student_id (int): neue Studenten-ID des Studenten der verändert wird
            vorname (str): neuer Vorname des Studenten der verändert wird
            nachname (str): neuer Nachname des Studenten der verändert wird
            kurs_id (int): neue Kurs-ID des Studenten der verändert wird
            nutzername (str): neuer Nutzername des Studenten der verändert wird
            passwort(str): neues Passwort des Studenten der verändert wird

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte des Student mit erhaltener alter Student-ID in
                        Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_student_by_id(
        my_connect, student_id_old, [student_id,vorname,nachname,kurs_id,nutzername,passwort])


@app.route(
    '/changeKurs/<int:kurs_id_old>/<int:kurs_id>/<string:name>/<int:dozent_id>',
    methods=['GET'])
def change_kurs(kurs_id_old: int,kurs_id: int, name: str, dozent_id: int):
    """ Attributwerte eines Kurses aus Tabelle 'Kurs' verändern

        Args:
            kurs_id_old (int): bisherige Kurs-ID des Kurses der verändert wird
            kurs_id (int): neue Kurs-ID des Kurses der verändert wird
            name (str): neuer Name des Kurses der verändert wird
            dozent_id (str): neuer Dozent-ID des Dozenten der dem Kurs der
                verändert wird als Studiengangsleiter zugeordnet ist

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte des Kurs mit erhaltener alter Kurs-ID in Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_kurs_by_id(my_connect, kurs_id_old, [kurs_id,name,dozent_id])


@app.route(
    '/changeDozent/<int:dozent_id_old>/<int:dozent_id>/<string:vorname>/'
    '<string:nachname>/<string:nutzername>/<string:passwort>',
    methods=['GET'])
def change_dozent(
        dozent_id_old: int,dozent_id: int, vorname: str,
        nachname: str, nutzername: str, passwort: str):
    """ Attributwerte eines Dozenten aus Tabelle 'Dozent' verändern

        Args:
            dozent_id_old (int): bisherige Dozent-ID des Dozenten der verändert wird
            dozent_id (int): neue Dozent-ID des Dozenten der verändert wird
            vorname (str): neuer Vorname des Dozenten der verändert wird
            nachname (str): neuer Nachname des Dozenten der verändert wird
            nutzername (str): neuer Nutzername des Dozenten der verändert wird
            passwort (str): neues Passwort des Dozenten der verändert wird

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte des Dozent mit erhaltener alter Dozent-ID in Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_dozent_by_id(
        my_connect, dozent_id_old, [dozent_id,vorname,nachname,nutzername,passwort])


@app.route(
    '/changeModul/<int:modul_id_old>/<int:modul_id>/<string:modulname>/<int:credits>/<int:kurs_id>',
    methods=['GET'])
def change_modul(
        modul_id_old: int, modul_id: int, modulname: str, module_credits: int, kurs_id: int):
    """ Attributwerte eines Moduls aus Tabelle 'Modul' verändern

        Args:
            modul_id_old (int): bisherige Modul-ID des Moduls das verändert wird
            modul_id (int): neue Modul-ID des Moduls das verändert wird
            modulname (str): neuer Name des Moduls das verändert wird
            credits (int): neue Credits welche das Modul das verändert wird Wert ist
            kurs_id (int): neue Kurs-ID des Kurses zu dem das Modul das verändert wird gehört

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte des Modul mit erhaltener alter Modul-ID in Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_modul_by_id(
        my_connect, modul_id_old, [modul_id,modulname,module_credits,kurs_id])


@app.route(
    '/changeVeranstaltung/<int:veranstaltung_id_old>/<int:veranstaltung_id>/'
    '<string:name>/<int:dozent_id>/<int:modul_id>',
    methods=['GET'])
def change_veranstaltung(
        veranstaltung_id_old: int, veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    """ Attributwerte einer Veranstaltung aus Tabelle 'Veranstaltung' verändern

        Args:
            veranstaltung_id_old (int): bisherige Veranstlatung-ID der Veranstaltung
                die verändert wird
            veranstaltung_id (int): neue Veranstaltung-ID der Veranstaltung die verändert wird
            name (str): neuer Name der Veranstaltung die verändert wird
            dozent_id (int): neue Dozent-ID des Dozenten der die Veranstaltung die verändert
                wird unterrichtet
            modul_id (int): neue Modul-ID des Moduls zu dem die Veranstaltung die verändert
                wird gehört

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte der Veranstaltung mit erhaltener alter Veranstaltung-ID
                        in Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_veranstaltung_by_id(
        my_connect, veranstaltung_id_old, [veranstaltung_id,name,dozent_id,modul_id])


@app.route(
    '/changePruefungsleistung/<int:student_id_old>/<int:veranstaltung_id_old>/'
    '<int:student_id>/<int:veranstaltung_id>/<int:punkte_gesamt>/<int:punkte_erreicht>',
    methods=['GET'])
def change_pruefungsleistung(
        student_id_old: int, veranstaltung_id_old: int, student_id: int,
        veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    """ Attributwerte einer Prüfungsleistung aus Tabelle 'Pruefungsleistung' verändern

        Args:
            student_id_old (int): bisherige Studenten-ID des Studenten der die Prüfungsleistung
                die verändert wird abgelegt hat
            veranstaltung_id_old (int): bisherige Veranstaltung-ID der Veranstaltung in der die
                Prüfungsleistung die verändert wird abgelegt wurde
            student_id (int): neue Studenten-ID des Studenten der die Prüfungleistung die verändert
                wird abgelegt hat
            veranstaltung_id (int): neue Veranstaltung-ID der Veranstaltung in der die
                Prüfungsleistung die verändert wird abgelegt wurde
            punkte_gesamt (int): neue Punkte die in Prüfungsleistung die verändert wird maximal
                erreichbar waren
            punkte_erreicht (int): neue Punkte die in der Prüfungsleisutng die verändert wird
                tatsächlich erreicht wurden

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte der Prüfungsleistung mit erhaltener alter Student-ID
                        & alter Veranstaltung-ID in Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_pruefungsleistung_by_student_and_veranstaltung(
        my_connect, student_id_old, veranstaltung_id_old,
        [student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht])


@app.route(
    '/changeAdmin/<int:admin_id_old>/<int:admin_id>/<string:vorname>/'
    '<string:nachname>/<string:nutzername>/<string:passwort>',
    methods=['GET'])
def change_admin(
        admin_id_old: int, admin_id: int, vorname: str,
        nachname: str, nutzername: str, passwort: str):
    """ Attributwerte eines Admins aus Tabelle 'Admin' verändern

        Args:
            admin_id_old (int): bisherige Admin-ID des Admins der verändert wird
            admin_id (int): neue Admin-ID des Admins der verändert wird
            vorname (str): neuer Vorname des Admins der verändert wird
            nachname (str): neuer Nachname des Admins der verändert wird
            nutzername (str): neuer Nutzername des Admins der verändert wird
            passwort (str): neues Passwort des Admins der verändert wird

        Returns:
            None

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * Attributwerte des Admin mit erhaltener alter Admin-ID in Datenbank verändert
                    * neue Attributwerte entsprechen übergebenen Eingabeparameter
                    * Rückgabewert None
            2)
                -> erwartetes Ergebnis:
    """
    return db.edit_admin_by_id(
        my_connect, admin_id_old, [admin_id,vorname,nachname,nutzername,passwort])


@app.route('/getStudent/<int:student_id>', methods=["GET"])
def get_student(student_id: int):
    """ Attribute eines Studenten aus Tabelle 'Student' abfragen

        Args:
            student_id (int): Studenten-ID des Studenten dessen Attributwerte abgefragt werden

        Returns:
            list: Liste mit Attributwerten des Studenten

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten des Student mit erhaltener Student-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_student_by_id(my_connect, student_id)


@app.route('/getKurs/<int:kurs_id>', methods=["GET"])
def get_kurs(kurs_id: int):
    """ Attribute eines Kurses aus Tabelle 'Kurs' abfragen

        Args:
            kurs_id (int): Kurs-ID des Kurses dessen Attributwerte abgefragt werden

        Returns:
            list: Liste mit Attributwerten des Kurses

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten des Kurs mit erhaltener Kurs-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_kurs_by_id(my_connect, kurs_id)


@app.route('/getDozent/<int:dozent_id>', methods=["GET"])
def get_dozent(dozent_id: int):
    """ Attribute eines Dozenten aus Tabelle 'Dozent' abfragen

        Args:
            dozent_id (int): Dozent-ID des Dozenten dessen Attributwerte abgefragt werden

        Returns:
            list: Liste mit Attributwerten des Dozenten

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten des Dozent mit erhaltener Dozent-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_dozent_by_id(my_connect, dozent_id)


@app.route('/getModul/<int:modul_id>', methods=["GET"])
def get_modul(modul_id: int):
    """ Attribute eines Moduls aus Tabelle 'Modul' abfragen

        Args:
            modul_id (int): Modul-ID des Moduls dessen Attributwerte abgefragt werden

        Returns:
            list: Liste mit Attributwerten des Moduls

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten des Modul mit erhaltener Modul-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_modul_by_id(my_connect, modul_id)


@app.route('/getVeranstaltung/<int:veranstaltung_id>', methods=["GET"])
def get_veranstaltung(veranstaltung_id: int):
    """ Attribute einer Veranstaltung aus Tabelle 'Veranstaltung' abfragen

        Args:
            veranstaltung_id (int): Veranstaltung-ID der Veranstaltung deren Attributwerte
                abgefragt werden

        Returns:
            list: Liste mit Attributwerten der Veranstaltung

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten der Veranstaltung mit erhaltener
                        Veranstaltung-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_veranstaltung_by_id(my_connect, veranstaltung_id)


@app.route('/getPruefungsleistung/<int:student_id>/<int:veranstaltung_id>', methods=["GET"])
def get_pruefungsleistung(student_id: int, veranstaltung_id: int):
    """ Attribute einer Prüfungsleistung aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            student_id (int): Studenten-ID des Studenten der Prüfungsleistung abgelegt hat
                deren Attributwerte abgefragt werden
            veranstaltung_id (int): Veranstlatung-ID der Veranstaltung in der Prüfungsleistung
                abgelegt wurde deren Attributwerte abgefragt werden

        Returns:
            list: Liste mit Attributwerten der Prüfungsleistung

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten der Prüfungsleistung mit erhaltener
                        Student-ID & Veranstaltung-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_pruefungsleistung_by_id(my_connect, student_id, veranstaltung_id)


@app.route('/getAdmin/<int:admin_id>', methods=["GET"])
def get_admin(admin_id: int):
    """ Attribute eines Admins aus Tabelle 'Admin' abfragen

        Args:
            admin_id (int): Admin-ID des Admins dessen Attributwerte abgefragt werden

        Returns:
            list: Liste mit Attributwerten des Admins

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Attributwerten des Admin mit erhaltener Admin-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_admin_by_id(my_connect, admin_id)


@app.route('/getPruefungsleistungenByStudent/<int:student_id>', methods=["GET"])
def get_pruefungsleistungen_by_student(student_id: int):
    """ alle Prüfungsleistungen eines Studenten aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            student_id (int): Studenten-ID des Studenten dessen Prüfungsleistungen abgefragt werden

        Returns:
            list: Liste mit mit Prüfungsleistungen (entsprechen je: Liste welche Attributwerte der
                Prüfungsleistungen beinhaltet)

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Prüfungsleistungen des Students mit erhaltener
                        Student-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_all_pruefungsleistung_by_student(my_connect, student_id)


@app.route('/get_all_veranstaltungen_by_dozent/<int:dozent_id>', methods=["GET"])
def get_all_veranstaltungen_by_dozent(dozent_id: int):
    """ alle Prüfungsleistungen eines Studenten aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            student_id (int): Studenten-ID des Studenten dessen Prüfungsleistungen abgefragt werden

        Returns:
            list: Liste mit mit Prüfungsleistungen (entsprechen je: Liste welche Attributwerte der
                Prüfungsleistungen beinhaltet)

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Prüfungsleistungen des Students mit erhaltener
                        Student-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_all_veranstaltungen_by_dozent(my_connect, dozent_id)


@app.route('/get_all_pruefungsleistung_by_veranstaltung/<int:dozent_id>', methods=["GET"])
def get_all_pruefungsleistung_by_veranstaltung(dozent_id: int):
    """ alle Prüfungsleistungen eines Studenten aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            student_id (int): Studenten-ID des Studenten dessen Prüfungsleistungen abgefragt werden

        Returns:
            list: Liste mit mit Prüfungsleistungen (entsprechen je: Liste welche Attributwerte der
                Prüfungsleistungen beinhaltet)

        Test:
            1) funktionierende Datenbankverbindung & zulässige Eingabeparameter an Funktion
                übergeben
                -> erwartetes Ergebnis:
                    * keine Änderungen in Datenbank
                    * Rückgabewert: Liste mit Prüfungsleistungen des Students mit erhaltener
                        Student-ID
            2)
                -> erwartetes Ergebnis:
    """
    return db.get_all_pruefungsleistung_by_veranstaltung(my_connect, dozent_id)

if __name__ == '__main__':
    db.database_setup(my_connect)
    db.fill_testdatabase(my_connect)
    app.run(debug=True)
