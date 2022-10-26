""" Modul für Datenbankkommunikation
    * bisher implementierte Funktionen:
        * Tabellen erstellen
        * Entitäten in Tabellen einfügen
        * Entitäten aus Tabellen löschen

    * fehlende Funktionen:
        * bestimmte Attribute bestimmter Entitäten abfragen
        * bestimmte Attribute bestimmter Entitäten ändern
        * Berechnung der Note einer Prüfungsleistung?

    * andere TO DO's:
        * Sicherstellen des richtigen Datentyps bei Übergabe einer Entität als Liste

    * weitere Anmerkungen bzw. zu Dokumentieren:
        * welche Module müssen in Entwicklungsumgebung installiert sein?
        * auch testen?

    author: Emma Müller
    date: 25.10.2022
    version: 1.0.0
    licence: free (open source)
"""

import sqlite3
from sqlite3 import Error


def create_database_connection(database_path):
    """ Verbindung zur SQLite-Datenbank herstellen

        Args:
            database_path (str): Quellpfad zur Datenbank-Datei

        Returns:
            Connection: Connection Objekt für Verbindung zur Datenbank

        Test:
            *
            *
    """
    conn = None
    try:
        conn = sqlite3.connect(database_path)
    except Error as connection_error:
        print(connection_error)
    return conn


def create_table(conn, sql_create_table):
    """Tabelle in Datenbank mit Hilfe des sql_create_table-Befehls

        Args:
            conn (Connection): Connection Objekt für Verbindung zur Datenbank
            sql_create_table (str): SQL-Befehl der neue Tabelle erstellt

        Returns:
            None

        Test:
            *
            *
    """
    try:
        cur = conn.cursor()
        cur.execute(sql_create_table)
    except Error as connection_error:
        print(connection_error)


def create_student(conn, student):
    """ neuen Student in Tabelle 'Student' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student (list): Liste mit Werten der Attribute eines Students in Reihenfolge (student_id, vorname, nachname, kurs_id)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschen Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Student(student_id,vorname,nachname,kurs_id) VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()


def create_kurs(conn, kurs):
    """ neuen Kurs in Tabelle 'Kurs' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            kurs (list): Liste mit Werten der Attribute eines Kurses in Reihenfolge (kurs_id, name, dozent_id)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschem Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Kurs(kurs_id,name,dozent_id) VALUES (?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, kurs)
    conn.commit()


def create_dozent(conn, dozent):
    """ neuen Dozent in Tabelle 'Dozent' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent (list): Liste mit Werten der Attribute eines Dozenten in Reihenfolge (dozent_id, vorname, nachname)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschen Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Dozent(dozent_id,vorname,nachname) VALUES (?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, dozent)
    conn.commit()


def create_modul(conn, modul):
    """ neues Modul in Tabelle 'Modul' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            modul (list): Liste mit Werten der Attribute eines Moduls in Reihenfolge (modul_id, modulname, credits, kurs_id)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschen Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, modul)
    conn.commit()


def create_veranstaltung(conn, veranstaltung):
    """ neue Veranstaltung in Tabelle 'Veranstaltung' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            veranstaltung (list): Liste mit Werten der Attribute einer Veranstaltung in Reihenfolge (veranstaltung_id, name, dozent_id, modul_id)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschen Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, veranstaltung)
    conn.commit()


def create_pruefungsleistung(conn, pruefugsleistung):
    """ neue Prüfungsleistung in Tabelle 'Pruefungsleistung' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            pruefungsleistung (list): Liste mit Werten der Attribute einer Prüfungsleistung in Reihenfolge (student_id, veranstaltung_id, punkte_gesamt, punkte_erreicht)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschen Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, pruefugsleistung)
    conn.commit()


def create_admin(conn, admin):
    """ neuen Admin in Tabelle 'Admin' einfügen
        * Admins können nur im Backend angelegt werden
        * kein Usertyp kann über das Frontend die Tabelle 'Admin' bearbeiten

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            admin (list): Liste mit Werten der Attribute eines Admins in Reihenfolge (admin_id, vorname, nachname)

        Returns:
            None

        Test:
            * Werte der Attribute mit falschen Datentyp (z.B. Integer anstatt String)
            *
    """
    sql = '''INSERT INTO Admin(admin_id,vorname,nachname) VALUES (?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, admin)
    conn.commit()



def delete_student(conn, student_id):
    """ bestimmten Student aus der Tabelle 'Student' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student_id (int): einzigartige ID des Studenten, die in Tabelle 'Student' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            *
            *
    """
    sql = '''DELETE FROM Student WHERE student_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (student_id,))
    conn.commit()


def delete_kurs(conn, kurs_id):
    """ bestimmten Kurs aus der Tabelle 'Kurs' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            kurs_id (int): einzigartige ID des Kurses, die in Tabelle 'Kurs' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            * nur von berechtigtem Kursleiter möglich (oder in anderer funktion durchführen?)
            *
    """
    sql = '''DELETE FROM Kurs WHERE kurs_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (kurs_id,))
    conn.commit()


def delete_dozent(conn, dozent_id):
    """ bestimmten Dozent aus der Tabelle 'Dozent' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent_id (int): einzigartige ID des Dozenten, die in Tabelle 'Dozent' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            *
            *
    """
    sql = '''DELETE FROM Dozent WHERE dozent_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (dozent_id,))
    conn.commit()


def delete_modul(conn, modul_id):
    """ bestimmtes Modul aus der Tabelle 'Modul' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            modul_id (int): einzigartige ID des Moduls, die in Tabelle 'Modul' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            *
            *
    """
    sql = '''DELETE FROM Modul WHERE modul_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (modul_id,))
    conn.commit()


def delete_veranstlatung(conn, veranstaltung_id):
    """ bestimmte Veranstaltung aus der Tabelle 'Veranstaltung' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            veranstaltung_id (int): einzigartige ID der Veranstaltung, die in Tabelle 'Veranstaltung' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            *
            *
    """
    sql = '''DELETE FROM Veranstaltung WHERE veranstaltung_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (veranstaltung_id,))
    conn.commit()


def delete_pruefungsleistung(conn, pruefungsleistung_veranstaltung, pruefungsleistung_student):
    """ bestimmten Prüfungsleistung aus der Tabelle 'Pruefungsleistung' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            pruefungsleistung_veranstaltung (int): einzigartige ID der Veranstaltung (aus der Prüfungsleistung hervorgegangen ist), die in Tabelle 'Veranstaltung' als PRIMARY KEY verwendet wird
            pruefungsleistung_student (int): einzigartige ID des Studenten (der Prüfungsleistung erarbeitet hat), die in Tabelle 'Student' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            *
            *
    """
    sql = '''DELETE FROM Pruefungsleistung WHERE student_id=? and veranstaltung_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (pruefungsleistung_student,pruefungsleistung_veranstaltung,))
    conn.commit()


def delete_admin(conn, admin_id):
    """ bestimmter Admin aus der Tabelle 'Admin' löschen
        * Admins können nur aus dem Backend gelöscht werden
        * kein Usertyp kann über das Frontend die Tabelle 'Admin' bearbeiten

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            admin_id (int): einzigartige ID des Admins, die in Tabelle 'Admin' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            *
            *
    """
    sql = '''DELETE FROM Admin WHERE admin_id=?'''
    cur = conn.cursor()
    cur.execute(sql, (admin_id,))
    conn.commit()



def database_setup(database_path):
    """ alle Tabellen in Datenbank erstellt (Student, Kurs, Dozent, Veranstaltung, Modul, Pruefungsleistung, Admin)
        * im Moment: bei neuem Start der Applikation Datenbank komplett zurückgesetzt

        Args:
            database_path (str): Quellpfad zur Datenbank-Datei

        Returns:
            None

        Test:
            *
            *
    """
    sql_create_student_table = '''CREATE TABLE Student (
                                    student_id integer PRIMARY KEY,
                                    vorname text,
                                    nachname text,
                                    kurs_id integer,
                                    FOREIGN KEY (kurs_id)
                                        REFERENCES Kurs (kurs_id)
                                            ON DELETE CASCADE
                                            ON UPDATE NO ACTION
                                );'''
    sql_create_kurs_table = '''CREATE TABLE Kurs (
                                    kurs_id integer PRIMARY KEY,
                                    name text,
                                    dozent_id integer,
                                    FOREIGN KEY (dozent_id)
                                        REFERENCES Dozent (dozent_id)
                                            ON DELETE CASCADE
                                            ON UPDATE NO ACTION
                                );'''
    sql_create_dozent_table = '''CREATE TABLE Dozent (
                                    dozent_id integer PRIMARY KEY,
                                    vorname text,
                                    nachname text
                                );'''
    sql_create_modul_table = '''CREATE TABLE Modul (
                                    modul_id integer PRIMARY KEY,
                                    modulname text,
                                    credits integer,
                                    kurs_id integer,
                                    FOREIGN KEY (kurs_id)
                                        REFERENCES Kurs (kurs_id)
                                            ON DELETE CASCADE
                                            ON UPDATE NO ACTION
                                );'''
    sql_create_veranstaltung_table = '''CREATE TABLE Veranstaltung (
                                        veranstaltung_id integer PRIMARY KEY,
                                        name text,
                                        dozent_id integer,
                                        modul_id integer,
                                        FOREIGN KEY (dozent_id)
                                            REFERENCES Dozent (dozent_id)
                                                ON DELETE CASCADE
                                                ON UPDATE NO ACTION,
                                        FOREIGN KEY (modul_id)
                                            REFERENCES Modul (moudl_id)
                                                ON DELETE CASCADE
                                                ON UPDATE NO ACTION
                                     );'''
    sql_create_pruefungsleistung_table = '''CREATE TABLE Pruefungsleistung (
                                                student_id INTEGER,
                                                veranstaltung_id INTEGER,
                                                punkte_gesamt integer,
                                                punkte_erreicht integer,
                                                PRIMARY KEY (student_id, veranstaltung_id),
                                                FOREIGN KEY (student_id)
                                                    REFERENCES Student (student_id)
                                                        ON DELETE CASCADE
                                                        ON UPDATE NO ACTION,
                                                FOREIGN KEY (veranstaltung_id)
                                                    REFERENCES Veranstaltung (veranstaltung_id)
                                                        ON DELETE CASCADE
                                                        ON UPDATE NO ACTION
                                        );'''
    sql_create_admin_table = '''CREATE TABLE Admin (
                                    admin_id integer PRIMARY KEY,
                                    vorname text,
                                    nachname text
                            );'''

    # create a database connection
    conn = create_database_connection(database_path)
    cur = conn.cursor()

    # create tables
    if conn is not None:
        # create dozent table
        cur.execute('''DROP TABLE IF EXISTS Dozent''')
        create_table(conn, sql_create_dozent_table)
        # create student table
        cur.execute('''DROP TABLE IF EXISTS Student''')
        create_table(conn, sql_create_student_table)
        # create kurs table
        cur.execute('''DROP TABLE IF EXISTS Kurs''')
        create_table(conn, sql_create_kurs_table)
        # create modul table
        cur.execute('''DROP TABLE IF EXISTS Modul''')
        create_table(conn, sql_create_modul_table)
        # create veranstaltung table
        cur.execute('''DROP TABLE IF EXISTS Veranstaltung''')
        create_table(conn, sql_create_veranstaltung_table)
        # create pruefungsleitung table
        cur.execute('''DROP TABLE IF EXISTS Pruefungsleistung''')
        create_table(conn, sql_create_pruefungsleistung_table)
        # create admin table
        cur.execute('''DROP TABLE IF EXISTS Admin''')
        create_table(conn, sql_create_admin_table)
    else:
        print("error! cannot create the database connection")


def get_all_modules(student_id):
    """
    noch nicht implementiert!
    alle Module eines Studenten ausgeben

    Args:
        student_id: Student, für den die Noten ausgegeben werden sollen

    Returns:
        data: Dictionary mit allen Modulen des Studenten {modul_name: [credits, note]}
    """

    sql = '''SELECT * FROM Pruefungsleistung WHERE student_id=?'''
    # cur = conn.cursor()
    # cur.execute(sql, (pruefungsleistung_student, pruefungsleistung_veranstaltung,))
    # conn.commit()
    return {1:[5, 1.8], 2:[5, 2.8], 3: [10, 2.4]}



if __name__ == '__main__':
    DATABASE_FILE = "test.db"
    database_setup(DATABASE_FILE)
