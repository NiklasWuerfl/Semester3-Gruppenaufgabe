"""Modul für Datenbankkommunikation

    author: Emma Müller
    date: 01.12.2022
    version: 1.0.4
    licence: free (open source)
"""

import sqlite3
from sqlite3 import Connection, Error


def create_database_connection(database_path: str):
    """Verbindung zur SQLite-Datenbank herstellen

        Args:
            database_path (str): Quellpfad zur Datenbank-Datei

        Returns:
            Connection: Connection Objekt für Verbindung zur Datenbank

        Test:
            1) Ausführen der Funktion mit gültigem database_path (data.db)
                -> erwartetes Ergebnis:
                    * Connection-Objekt wird erstellt & keine Exception wird ausgelöst
                    * Rückgabewert: passendes Connection-Objekt
            2) Ausführen der Funktion mit ungültigem database_path
                -> erwartetes Ergebnis:
                    * beim Versuch Connection-Objekt zu erstellt wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    conn = None
    try:
        conn = sqlite3.connect(database_path, check_same_thread=False)
    except Error as connection_error:
        print(connection_error)
    return conn


def create_table(conn: Connection, sql_create_table: str):
    """Tabelle in Datenbank mit Hilfe des sql_create_table-Befehls

        Args:
            conn (Connection): Connection Objekt für Verbindung zur Datenbank
            sql_create_table (str): SQL-Befehl der neue Tabelle erstellt

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und SQL-Befehl
                -> erwartetes Ergebnis:
                    * Cursor wird erstellt
                    * SQL-Befehl wird ausgeführt
                    * SQL-Befehl entsprechende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    try:
        cur = conn.cursor()
        cur.execute(sql_create_table)
    except Error as connection_error:
        print(connection_error)
    return None


def create_student(conn: Connection, student: tuple[int, str, str, int, str, str]):
    """neuen Student in Tabelle 'Student' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student (tuple): Tupel mit Werten der Attribute eines Students in Reihenfolge
                (student_id, vorname, nachname, kurs_id, nutzername, passwort)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neuer Student wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Student' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
        VALUES (?,?,?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, student)
        conn.commit()
    except Error as create_student_error:
        print(create_student_error)
    return None


def create_kurs(conn: Connection, kurs: tuple[int, str, int]):
    """neuen Kurs in Tabelle 'Kurs' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            kurs (tuple): Tupel mit Werten der Attribute eines Kurses in
                Reihenfolge (kurs_id, name, dozent_id)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neuer Kurs wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Kurs' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """INSERT INTO Kurs(kurs_id,name,dozent_id) VALUES (?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, kurs)
        conn.commit()
    except Error as create_kurs_error:
        print(create_kurs_error)
    return None


def create_dozent(conn: Connection, dozent: tuple[int, str, str, str, str]):
    """neuen Dozent in Tabelle 'Dozent' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent (tuple): Tupel mit Werten der Attribute eines Dozenten in
                Reihenfolge (dozent_id, vorname, nachname, nutzername, passwort)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neuer Dozent wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Dozent' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort)
        VALUES (?,?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, dozent)
        conn.commit()
    except Error as create_dozent_error:
        print(create_dozent_error)
    return None


def create_modul(conn: Connection, modul: tuple[int, str, int, int]):
    """neues Modul in Tabelle 'Modul' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            modul (tuple): Tupel mit Werten der Attribute eines Moduls in
                Reihenfolge (modul_id, modulname, credits, kurs_id)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neues Modul wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Modul' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, modul)
        conn.commit()
    except Error as create_modul_error:
        print(create_modul_error)
    return None


def create_veranstaltung(conn: Connection, veranstaltung: tuple[int, str, int, int]):
    """neue Veranstaltung in Tabelle 'Veranstaltung' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            veranstaltung (tuple): Tupel mit Werten der Attribute einer Veranstaltung in
                Reihenfolge (veranstaltung_id, name, dozent_id, modul_id)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neue Veranstaltung wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Veranstaltung' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, veranstaltung)
        conn.commit()
    except Error as create_veranstaltung_error:
        print(create_veranstaltung_error)
    return None


def create_pruefungsleistung(conn: Connection, pruefugsleistung: tuple[int, int, int, int]):
    """neue Prüfungsleistung in Tabelle 'Pruefungsleistung' einfügen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            pruefungsleistung (tuple): Tupel mit Werten der Attribute einer Prüfungsleistung in
                Reihenfolge (student_id, veranstaltung_id, punkte_gesamt, punkte_erreicht)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neue Prüfungsleistung wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Pruefungsleistung' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    if pruefugsleistung[2] >= pruefugsleistung[3]:
        sql = """
            INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht)
                VALUES (?,?,?,?)"""
        try:
            cur = conn.cursor()
            cur.execute(sql, pruefugsleistung)
            conn.commit()
        except Error as create_pruefungsleistung_error:
            print(create_pruefungsleistung_error)
    else:
        print("Es können nicht mehr Punkte erreicht werden, als möglich ist zu erreichen!")
    return None


def create_admin(conn: Connection, admin: tuple[int, str, str, str, str]):
    """neuen Admin in Tabelle 'Admin' einfügen
        * Admins können nur im Backend angelegt werden
        * kein Usertyp kann über das Frontend die Tabelle 'Admin' bearbeiten

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            admin (tuple): Tupel mit Werten der Attribute eines Admins in
                Reihenfolge (admin_id, vorname, nachname, nutzername, passwort)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * neuer Admin wird mit Attributwerten aus Eingabeparametern in
                        Tabelle 'Admin' erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """INSERT INTO Admin(admin_id,vorname,nachname,nutzername,passwort) VALUES (?,?,?,?,?)"""
    try:
        cur = conn.cursor()
        cur.execute(sql, admin)
        conn.commit()
    except Error as create_admin_error:
        print(create_admin_error)
    return None



def delete_student(conn: Connection, student_id: int):
    """bestimmten Student aus der Tabelle 'Student' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student_id (int): einzigartige ID des Studenten, die in Tabelle 'Student'
                als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Student mit Eingabeparameter als Student-ID wird aus
                        Tabelle 'Student' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Student WHERE student_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (student_id,))
        conn.commit()
    except Error as delete_student_error:
        print(delete_student_error)
    return None


def delete_kurs(conn: Connection, kurs_id: int):
    """bestimmten Kurs aus der Tabelle 'Kurs' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            kurs_id (int): einzigartige ID des Kurses, die in Tabelle 'Kurs'
                als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Kurs mit Eingabeparameter als Kurs-ID wird aus
                        Tabelle 'Kurs' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Kurs WHERE kurs_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (kurs_id,))
        conn.commit()
    except Error as delete_kurs_error:
        print(delete_kurs_error)
    return None


def delete_dozent(conn: Connection, dozent_id: int):
    """bestimmten Dozent aus der Tabelle 'Dozent' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent_id (int): einzigartige ID des Dozenten, die in Tabelle 'Dozent'
                als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Dozent mit Eingabeparameter als Dozent-ID wird aus
                        Tabelle 'Dozent' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Dozent WHERE dozent_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (dozent_id,))
        conn.commit()
    except Error as delete_dozent_error:
        print(delete_dozent_error)
    return None


def delete_modul(conn: Connection, modul_id: int):
    """bestimmtes Modul aus der Tabelle 'Modul' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            modul_id (int): einzigartige ID des Moduls, die in Tabelle 'Modul'
                als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Modul mit Eingabeparameter als Modul-ID wird aus
                        Tabelle 'Modul' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Modul WHERE modul_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (modul_id,))
        conn.commit()
    except Error as delete_modul_error:
        print(delete_modul_error)
    return None


def delete_veranstaltung(conn: Connection, veranstaltung_id: int):
    """bestimmte Veranstaltung aus der Tabelle 'Veranstaltung' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            veranstaltung_id (int): einzigartige ID der Veranstaltung, die in Tabelle
                'Veranstaltung' als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Veranstaltung mit Eingabeparameter als Veranstaltung-ID wird aus
                        Tabelle 'Veranstaltung' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Veranstaltung WHERE veranstaltung_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (veranstaltung_id,))
        conn.commit()
    except Error as delete_veranstaltung_error:
        print(delete_veranstaltung_error)
    return None


def delete_pruefungsleistung(
        conn: Connection, pruefungsleistung_veranstaltung: int, pruefungsleistung_student: int):
    """bestimmten Prüfungsleistung aus der Tabelle 'Pruefungsleistung' löschen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            pruefungsleistung_veranstaltung (int): einzigartige ID der Veranstaltung
                (aus der Prüfungsleistung hervorgegangen ist), die in Tabelle 'Veranstaltung'
                als PRIMARY KEY verwendet wird
            pruefungsleistung_student (int): einzigartige ID des Studenten
                (der Prüfungsleistung erarbeitet hat), die in Tabelle 'Student'
                als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Prüfungleistung mit Eingabeparametern als Student-ID & Veranstaltung-ID wird aus
                        Tabelle 'Pruefungsleistung' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Pruefungsleistung WHERE student_id=? and veranstaltung_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (pruefungsleistung_student,pruefungsleistung_veranstaltung,))
        conn.commit()
    except Error as delete_pruefungsleistung_error:
        print(delete_pruefungsleistung_error)
    return None


def delete_admin(conn: Connection, admin_id: int):
    """bestimmten Admin aus der Tabelle 'Admin' löschen
        * Admins können nur aus dem Backend gelöscht werden
        * kein Usertyp kann über das Frontend die Tabelle 'Admin' bearbeiten

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            admin_id (int): einzigartige ID des Admins, die in Tabelle 'Admin'
                als PRIMARY KEY verwendet wird

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * Admin mit Eingabeparameter als Admin-ID wird aus
                        Tabelle 'Admin' gelöscht
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """DELETE FROM Admin WHERE admin_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (admin_id,))
        conn.commit()
    except Error as delete_admin_error:
        print(delete_admin_error)
    return None


def get_student_by_id(conn: Connection, student_id: int) -> list:
    """Attribut-Werte eines Studenten aus Tabelle 'Student' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student_id (int): einzigartige ID des Studenten, die in Tabelle 'Student'
                als PRIMARY KEY verwendet wird

        Returns:
            list: Liste mit Attribut-Werten des gesuchten Studenten

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten des Student
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Student WHERE student_id=?"""
    student = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (student_id,))
        student = cur.fetchall()
    except Error as get_student_by_id_error:
        print(get_student_by_id_error)
    return [student[0]]


def get_kurs_by_id(conn: Connection, kurs_id: int) -> list:
    """Attribut-Werte eines Kurses aus Tabelle 'Kurs' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            kurs_id (int): einzigartige ID des Kurses, die in Tabelle 'Kurs'
                als PRIMARY KEY verwendet wird

        Returns:
            list: Liste mit Attribute-Werten des gesuchten Kurses

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten des Kurs
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Kurs WHERE kurs_id=?"""
    kurs = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (kurs_id,))
        kurs = cur.fetchall()
    except Error as get_kurs_by_id_error:
        print(get_kurs_by_id_error)
    return kurs[0]


def get_dozent_by_id(conn: Connection, dozent_id: int) -> list:
    """Attribut-Werte eines Dozenten aus Tabelle 'Dozent' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent_id (int): einzigartige ID des Dozenten, die in Tabelle 'Dozent'
                als PRIMARY KEY verwendet wird

        Returns:
            list: Liste mit Attribute-Werten des gesuchten Dozenten

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten des Dozent
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Dozent WHERE dozent_id=?"""
    dozent = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (dozent_id,))
        dozent = cur.fetchall()
    except Error as get_dozent_by_id_error:
        print(get_dozent_by_id_error)
    return [dozent[0]]


def get_modul_by_id(conn: Connection, modul_id: int) -> list:
    """Attribut-Werte eines Moduls aus Tabelle 'Modul' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            modul_id (int): einzigartige ID des Moduls, die in Tabelle 'Modul'
                als PRIMARY KEY verwendet wird

        Returns:
            list: Liste mit Attribute-Werten des gesuchten Moduls

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten des Modul
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Modul WHERE modul_id=?"""
    modul = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (modul_id,))
        modul = cur.fetchall()
    except Error as get_modul_by_id_error:
        print(get_modul_by_id_error)
    return modul


def get_veranstaltung_by_id(conn: Connection, veranstaltung_id: int) -> list:
    """Attribut-Werte einer Veranstaltung aus Tabelle 'Veranstaltung' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            veranstaltung_id (int): einzigartige ID der Veranstaltung, die in Tabelle
                'Veranstaltung' als PRIMARY KEY verwendet wird

        Returns:
            list: Liste mit Attribute-Werten der gesuchten Veranstaltung

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten der Veranstaltung
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Veranstaltung WHERE veranstaltung_id=?"""
    veranstaltung = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (veranstaltung_id,))
        veranstaltung = cur.fetchall()
    except Error as get_veranstaltung_by_id_error:
        print(get_veranstaltung_by_id_error)
    return [veranstaltung[0]]


def get_pruefungsleistung_by_id(
        conn: Connection, pruefungsleistung_student_id: int,
        pruefungsleistung_veranstaltung_id: int) -> list:
    """Attribut-Werte einer Prüfungsleistung aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            pruefungsleistung_student_id (int): einzigartige ID des Studenten
                (der Prüfungsleistung abgelegt hat), die in Tabelle 'Student' als PRIMARY KEY
                verwendet wird & in Tabelle 'Pruefungsleistung' als FOREIGN KEY zum PRIMARY KEY
                gehört
            pruefungsleistung_veranstaltung_id (int): einzigartige ID der Veranstaltung
                (in welcher Prüfungleistung abgelegt wurde), die in Tabelle 'Veranstaltung'
                als PRIMARY KEY verwendet wird & in Tabelle 'Pruefungsleistung' als FOREIGN KEY
                zum PRIMARY KEY gehört

        Returns:
            list: Liste mit Attribute-Werten der gesuchten Prüfungsleistung

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten der Prüfungsleistung
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Pruefungsleistung WHERE student_id=? AND veranstaltung_id=?"""
    pruefungsleistung = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (pruefungsleistung_student_id,pruefungsleistung_veranstaltung_id,))
        pruefungsleistung = cur.fetchall()
    except Error as get_pruefungsleistung_by_id_error:
        print(get_pruefungsleistung_by_id_error)
    return pruefungsleistung[0]


def get_admin_by_id(conn: Connection, admin_id: int) -> list:
    """Attribut-Werte eines Admins aus Tabelle 'Admin' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            admin_id (int): einzigartige ID des Admins, die in Tabelle 'Admin'
                als PRIMARY KEY verwendet wird

        Returns:
            list: Liste mit Attribute-Werten des gesuchten Admins

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Attributwerten des Admin
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Admin WHERE admin_id=?"""
    admin = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (admin_id,))
        admin = cur.fetchall()
    except Error as get_admin_by_id_error:
        print(get_admin_by_id_error)
    return [admin[0]]


def edit_student_by_id(
        conn: Connection, student_id: int, student: tuple[int, str, str, int, str, str]):
    """Attribute eines Studenten in Tabelle 'Student' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_student_by_id-Funktion & Auswahl aus Liste, Attribut in übergebenem Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student_id (int): einzigartige ID des Studenten zur Identifizierung
            student (tuple): Tupel mit neuen Werten der Attribute eines Students in
                Reihenfolge (student_id, vorname, nachname, kurs_id, nutzername, passwort)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Student SET student_id=?, vorname=?, nachname=?,
        kurs_id=?, nutzername=?, passwort=?
        WHERE student_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(
            sql,
            (student[0],student[1],student[2],student[3],student[4],student[5],student_id))
        conn.commit()
    except Error as edit_student_by_id_error:
        print(edit_student_by_id_error)
    return None


def edit_kurs_by_id(conn: Connection, kurs_id: int, kurs: tuple[int, str, int]):
    """Attribute eines Kurses in Tabelle 'Kurs' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_kurs_by_id-Funktion & Auswahl aus Liste, Attribut in übergebenem Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            kurs_id (int): einzigartige ID des Kurses zur Identifizierung
            kurs (tuple): Tupel mit neuen Werten der Attribute eines Kurses in
                Reihenfolge (kurs_id, name, dozent_id)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellenwird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Kurs SET kurs_id=?, name=?, dozent_id=? WHERE kurs_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (kurs[0],kurs[1],kurs[2],kurs_id))
        conn.commit()
    except Error as edit_kurs_by_id_error:
        print(edit_kurs_by_id_error)
    return None


def edit_dozent_by_id(conn: Connection, dozent_id: int, dozent: tuple[int, str, str, str, str]):
    """Attribute eines Dozenten in Tabelle 'Dozent' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_dozent_by_id-Funktion & Auswahl aus Liste, Attribut in übergebenem Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent_id (int): einzigartige ID des Dozenten zur Identifizierung
            dozent (tuple): Tupel mit neuen Werten der Attribute eines Dozent in
                Reihenfolge (dozent_id, vorname, nachname, nutzername, passwort)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Dozent SET dozent_id=?, vorname=?, nachname=?, nutzername=?, passwort=?
        WHERE dozent_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (dozent[0],dozent[1],dozent[2],dozent[3],dozent[4],dozent_id))
        conn.commit()
    except Error as edit_dozent_by_id_error:
        print(edit_dozent_by_id_error)
    return None


def edit_modul_by_id(conn: Connection, modul_id: int, modul: tuple[int, str, int, int]):
    """Attribute eines Moduls in Tabelle 'Modul' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_modul_by_id-Funktion & Auswahl aus Liste, Attribut in übergebenem Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            modul_id (int): einzigartige ID des Moduls zur Identifizierung
            modul (tuple): Tupel mit neuen Werten der Attribute eines Moduls in
                Reihenfolge (modul_id, modulname, credits, kurs_id)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Modul SET modul_id=?, modulname=?, credits=?, kurs_id=? WHERE modul_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (modul[0],modul[1],modul[2],modul[3],modul_id))
        conn.commit()
    except Error as edit_modul_by_id_error:
        print(edit_modul_by_id_error)
    return None


def edit_veranstaltung_by_id(
        conn: Connection, veranstaltung_id: int, veranstaltung: tuple[int, str, int, int]):
    """Attribute einer Veranstaltung in Tabelle 'Veranstaltung' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_veranstaltung_by_id-Funktion & Auswahl aus Liste, Attribut in
            übergebenem Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            veranstaltung_id (int): einzigartige ID der Veranstaltung zur Identifizierung
            veranstaltung (tuple): Tupel mit neuen Werten der Attribute einer Veranstaltung in
                Reihenfolge (veranstaltung_id, name, dozent_id, modul_id)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Veranstaltung SET veranstaltung_id=?, name=?, dozent_id=?, modul_id=?
        WHERE veranstaltung_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(
            sql,
            (veranstaltung[0],veranstaltung[1],veranstaltung[2],veranstaltung[3],veranstaltung_id))
        conn.commit()
    except Error as edit_veranstaltung_by_id_error:
        print(edit_veranstaltung_by_id_error)
    return None


def edit_pruefungsleistung_by_student_and_veranstaltung(
        conn: Connection, pruefungsleistung_student: int, pruefungsleistung_veranstaltung: int,
        pruefungsleistung: tuple[int, int, int, int]):
    """Attribute einer Prüfungsleistung in Tabelle 'Pruefungsleistung' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_pruefungsleistung_by_id-Funktion & Auswahl aus Liste, Attribut in übergebenem
            Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            pruefungsleistung_student (int): einzigartige ID des Studenten der Prüfungsleistung
                abgelegt hat
            pruefungsleistung_veranstaltung (int): einzigartige ID der Veranstaltung für die
                Prüfungsleistung abgelegt wurde
            pruefungsleistung (tuple): Tupel mit neuen Werten der Attribute einer Pruefungsleistung
                in Reihenfolge (student_id, veranstaltung, punkte_gesamt, punkte_erreicht)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Pruefungsleistung SET student_id=?, veranstaltung_id=?, punkte_gesamt=?,
        punkte_erreicht=? WHERE student_id=? AND veranstaltung_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(
            sql,
            (pruefungsleistung[0],pruefungsleistung[1],pruefungsleistung[2],
            pruefungsleistung[3],pruefungsleistung_student,pruefungsleistung_veranstaltung))
        conn.commit()
    except Error as edit_pruefungsleistung_by_student_and_veranstaltung_error:
        print(edit_pruefungsleistung_by_student_and_veranstaltung_error)
    return None


def edit_admin_by_id(conn: Connection, admin_id: int, admin: tuple[int, str, str, str, str]):
    """Attribute eines Admins in Tabelle 'Admin' verändern
        * neue Attribute als ein Argument übergeben
        * wenn nur einzelne Attribute geändert: nicht zu ändernde Attribute durch
            get_admin_by_id-Funktion & Auswahl aus Liste, Attribut in übergebenem Tupel angeben

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            admin_id (int): einzigartige ID des Admins zur Identifizierung
            admin (tuple): Tupel mit neuen Werten der Attribute eines Admins in
            Reihenfolge (admin_id, vorname, nachname, nutzername, passwort)

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparametern
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * entstehende Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """UPDATE Admin SET admin_id=?, vorname=?, nachname=?, nutzername=?, passwort=?
        WHERE admin_id=?"""
    try:
        cur = conn.cursor()
        cur.execute(sql, (admin[0],admin[1],admin[2],admin[3],admin[4],admin_id))
        conn.commit()
    except Error as edit_admin_by_id_error:
        print(edit_admin_by_id_error)
    return None


def get_all_pruefungsleistung_by_student(conn: Connection, student_id: int) -> list[list]:
    """alle Prüfungsleistungen eines Studenten aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student_id (int): einzigartige ID des Studenten, die in Tabelle 'Pruefungsleistung'
                als Verlinkung zum Studenten dient

        Returns:
            list: Liste mit Listen welche Attribute-Werte aller gesuchten Prüfungsleistungen
                beinhaltet

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Prüfungsleistungen (als Liste) des Student
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Pruefungsleistung WHERE student_id=?"""
    pruefungsleistungen = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (student_id,))
        pruefungsleistungen = cur.fetchall()
    except Error as get_all_pruefungsleistung_by_student_error:
        print(get_all_pruefungsleistung_by_student_error)
    return pruefungsleistungen


def get_all_veranstaltungen_by_dozent(conn: Connection, dozent_id: int) -> list[list]:
    """alle Veranstaltungen eines Dozenten aus Tabelle 'Veranstaltungen' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            dozent_id (int): einzigartige ID des Dozenten, die in Tabelle 'Veranstaltungen'
                als Verlinkung zum Dozenten dient

        Returns:
            list: Liste mit Listen welche Attribute-Werte aller gesuchten Veranstaltungen
                beinhaltet

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Veranstaltungen (als Liste) des Dozenten
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Veranstaltungen WHERE dozent_id=?"""
    veranstaltungen = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (dozent_id,))
        veranstaltungen = cur.fetchall()
    except Error as get_all_veranstaltungen_by_dozent_error:
        print(get_all_veranstaltungen_by_dozent_error)
    return veranstaltungen


def get_all_pruefungsleistung_by_veranstaltung(conn: Connection, veranstaltung_id: int) -> list[list]:
    """alle Prüfungsleistungen einer Veranstaltung aus Tabelle 'Pruefungsleistung' abfragen

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank
            student_id (int): einzigartige ID des Studenten, die in Tabelle 'Pruefungsleistung'
                als Verlinkung zum Studenten dient

        Returns:
            list: Liste mit Listen welche Attribute-Werte aller gesuchten Prüfungsleistungen
                beinhaltet

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt und Eingabeparameter
                -> erwartetes Ergebnis:
                    * SQL-Befehls-String & Cursor werden erstellt
                    * SQL-Befehl wird ausgeführt
                    * keine Veränderungen werden in Datenbank durchgeführt
                    * Rückgabewert: Liste mit Prüfungsleistungen (als Liste) des Student
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql = """SELECT * FROM Pruefungsleistung WHERE student_id=?"""
    pruefungsleistungen = None
    try:
        cur = conn.cursor()
        cur.execute(sql, (veranstaltung_id,))
        pruefungsleistungen = cur.fetchall()
    except Error as get_all_pruefungsleistung_by_veranstaltung_error:
        print(get_all_pruefungsleistung_by_veranstaltung_error)
    return pruefungsleistungen


def database_setup(conn: Connection):
    """alle Tabellen in Datenbank erstellt
            (Student, Kurs, Dozent, Veranstaltung, Modul, Pruefungsleistung, Admin)
        * im Moment: bei neuem Start der Applikation Datenbank komplett zurückgesetzt

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * Cursor wird erstellt
                    * SQL-Befehle wird ausgeführt
                    * alle Tabellen werden in Datenbank erstellt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql_create_student_table = """CREATE TABLE Student (
                                    student_id integer PRIMARY KEY,
                                    vorname text,
                                    nachname text,
                                    kurs_id integer,
                                    nutzername text,
                                    passwort text,
                                    FOREIGN KEY (kurs_id)
                                        REFERENCES Kurs (kurs_id)
                                            ON DELETE CASCADE
                                            ON UPDATE NO ACTION
                                );"""
    sql_create_kurs_table = """CREATE TABLE Kurs (
                                    kurs_id integer PRIMARY KEY,
                                    name text,
                                    dozent_id integer,
                                    FOREIGN KEY (dozent_id)
                                        REFERENCES Dozent (dozent_id)
                                            ON DELETE CASCADE
                                            ON UPDATE NO ACTION
                                );"""
    sql_create_dozent_table = """CREATE TABLE Dozent (
                                    dozent_id integer PRIMARY KEY,
                                    vorname text,
                                    nachname text,
                                    nutzername text,
                                    passwort text
                                );"""
    sql_create_modul_table = """CREATE TABLE Modul (
                                    modul_id integer PRIMARY KEY,
                                    modulname text,
                                    credits integer,
                                    kurs_id integer,
                                    FOREIGN KEY (kurs_id)
                                        REFERENCES Kurs (kurs_id)
                                            ON DELETE CASCADE
                                            ON UPDATE NO ACTION
                                );"""
    sql_create_veranstaltung_table = """CREATE TABLE Veranstaltung (
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
                                     );"""
    sql_create_pruefungsleistung_table = """CREATE TABLE Pruefungsleistung (
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
                                        );"""
    sql_create_admin_table = """CREATE TABLE Admin (
                                    admin_id integer PRIMARY KEY,
                                    vorname text,
                                    nachname text,
                                    nutzername text,
                                    passwort text
                            );"""

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute('''DROP TABLE IF EXISTS Dozent''')
            create_table(conn, sql_create_dozent_table)
            cur.execute('''DROP TABLE IF EXISTS Student''')
            create_table(conn, sql_create_student_table)
            cur.execute('''DROP TABLE IF EXISTS Kurs''')
            create_table(conn, sql_create_kurs_table)
            cur.execute('''DROP TABLE IF EXISTS Modul''')
            create_table(conn, sql_create_modul_table)
            cur.execute('''DROP TABLE IF EXISTS Veranstaltung''')
            create_table(conn, sql_create_veranstaltung_table)
            cur.execute('''DROP TABLE IF EXISTS Pruefungsleistung''')
            create_table(conn, sql_create_pruefungsleistung_table)
            cur.execute('''DROP TABLE IF EXISTS Admin''')
            create_table(conn, sql_create_admin_table)
        except Error as database_setup_error:
            print(database_setup_error)
    else:
        print("error! cannot create the database connection")
    return None

def fill_testdatabase(conn: Connection):
    """alle Tabellen in Datenbank mit ersten Daten füllen
            (Student, Kurs, Dozent, Veranstaltung, Modul, Pruefungsleistung, Admin)
        * im Moment: bei neuem Start der Applikation Datenbank komplett zurückgesetzt

        Args:
            conn (Connection): Connection-Objekt für Verbindung zur Datenbank

        Returns:
            None

        Test:
            1) Ausführen der Funktion mit gültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * Cursor wird erstellt
                    * SQL-Befehle wird ausgeführt
                    * alle Tabellen werden in Datenbank werden mit Testdaten befüllt
                    * Rückgabewert: None
            2) Ausführen der Funktion mit ungültigem Connection-Objekt
                -> erwartetes Ergebnis:
                    * beim Versuch Cursor zu erstellen wird Exception ausgelöst
                    * Error wird ausgegeben
    """
    sql_fill_students="""
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (1000,'s1000','Lastname10',23,'Stud10','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (2000,'s2000','Lastname20',23,'Stud20','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (3000,'s3000','Lastname30',23,'Stud30','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (4000,'s4000','Lastname40',23,'Stud40','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (1100,'s1100','Lastname11',56,'Stud11','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (2100,'s2100','Lastname21',56,'Stud21','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (3100,'s3100','Lastname31',56,'Stud31','passwort');
        INSERT INTO Student(student_id,vorname,nachname,kurs_id,nutzername,passwort)
            VALUES (4100,'s4100','Lastname41',56,'Stud41','passwort');"""
    sql_fill_kurs="""
        INSERT INTO Kurs(kurs_id,name,dozent_id) VALUES (23,'WWI2021E',555);
        INSERT INTO Kurs(kurs_id,name,dozent_id) VALUES (56,'BWL1999U',666);"""
    sql_fill_dozent="""
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (110,'Peter','Kurz','PKurz','KURZpeter');
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (120,'Sebastian','Fichtner','SFichtner','FICHTNERsebastian');
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (310,'Andrea','Schlauer','ASchlauer','SCHLAUERandrea');
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (810,'Johannes','Unkreativ','JUnkreativ','UNKREATIVjohannes');
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (900,'Jochen','Grewatsch','JGrewatsch','GREWATSCHjochen');
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (555,'Marcus','Vogt','MVogt','VOGTmarcus');
        INSERT INTO Dozent(dozent_id,vorname,nachname,nutzername,passwort) VALUES (666,'Alter','Sgleiter','ASgleiter','SGLEITERalter');"""
    sql_fill_modul="""
        INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (1200,'Mathematik II',8,23);
        INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (3000,'IT Konzepte',5,23);
        INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (9980,'Finanz- und Rechnungslehre',5,23);
        INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (1201,'Mathematik II',8,56);
        INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (3001,'IT Konzepte',5,56);
        INSERT INTO Modul(modul_id,modulname,credits,kurs_id) VALUES (9981,'Finanz- und Rechnungslehre',5,56);"""
    sql_fill_veranstaltung="""
        INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (1000,'Statistik',110,1200);
        INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (1001,'Operations Research',120,1200);
        INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (2000,'Kommunikationssysteme',310,3000);
        INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (2001,'Grundlagen IT',810,3000);
        INSERT INTO Veranstaltung(veranstaltung_id,name,dozent_id,modul_id) VALUES (3000,'Finanzierung',900,9980);"""
    sql_fill_pruefungsleistung="""
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (1000,1000,60,52);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (1000,1001,60,58);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (1000,2000,80,75);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (1000,2001,40,36);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (1000,3000,120,108);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (2000,1000,60,32);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (2000,1001,60,41);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (2000,2000,80,52);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (2000,2001,40,20);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (2000,3000,120,64);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (3000,1000,60,45);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (3000,1001,60,50);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (3000,2000,80,57);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (3000,2001,40,34);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (3000,3000,120,98);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (4000,1000,60,52);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (4000,1001,60,48);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (4000,2000,80,66);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (4000,2001,40,31);
        INSERT INTO Pruefungsleistung(student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht) VALUES (4000,3000,120,null);"""
    sql_fill_admin="""
        INSERT INTO Admin(admin_id,vorname,nachname,nutzername,passwort) VALUES (99,'Power','Admin','AdminUser','AdminPW')"""

    if conn is not None:
        try:
            cur = conn.cursor()
            cur.executescript(sql_fill_students)
            cur.executescript(sql_fill_kurs)
            cur.executescript(sql_fill_dozent)
            cur.executescript(sql_fill_modul)
            cur.executescript(sql_fill_veranstaltung)
            cur.executescript(sql_fill_pruefungsleistung)
            cur.executescript(sql_fill_admin)
        except Error as fill_testdatabase_error:
            print(fill_testdatabase_error)
    else:
        print("error! cannot create the database connection")
    return None
