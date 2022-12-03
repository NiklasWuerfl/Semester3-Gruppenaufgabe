"""
    Modul für interne Berechnungen und Datenbereitstellung
    Frontend greift auf dieses Modul zu. Die Daten werden dann über die API in "app.py" geladen und intern so
    modifiziert, dass sie direkt im Frontend integriert werden können.


    Grundlage der Notenberechnungen: DHBW Richtlinien
    Berechnung der Gesamtnote (zwar von Informatik aber etwas anderes gibt es nicht): https://www.dhbw-stuttgart.de/studierendenportal/informatik/studienbetrieb/bachelorarbeiten/notenberechnung/

    https://www.dhbw.de/fileadmin/user_upload/Dokumente/Amtliche_Bekanntmachungen/2022/31_2022_Bekanntmachung_StuPrO_Wirtschaft_inkl._Vierte_AEnderungssatzung.pdf
    ECTS Übersicht: S. 70
    Berechnung der Note einer Prüfungsleistung: S. 73

    author:
    date: 26.10.2022
    version: 1.0.0
    licence: free (open source)
"""
import Student_be
import DozentB
import app
import database as db
from flask import Flask
import requests as r

url = "http://localhost:5000"


def get_values (querystring: str) -> list[list]:
    """ Schnittstellenfunktion zur API. Führt eine request an den querystring aus und gibt das Ergebnis als
        (strukturiertes) Array bzw. json zurück bzw. erstellt und verändert Datensätze.
        Funktioniert nur bei laufender API!

        Args:
            querystring (int): Studenten-ID des Studenten dessen Prüfungsleistungen abgefragt werden

        Returns:
            list: Liste mit angeforderten Rohdaten aus der Datenbank (via API)

        Test:
            1) funktionierende API-Verbindung & zulässigen Querystring übergeben
                -> erwartetes Ergebnis:
                    * Rückgabewert: Liste mit angeforderten Rohdaten
            2) funktionierende API-Verbindung & unzulässigen Querystring übergeben
                -> erwartetes Ergebnis:
                    * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat.
            3) nicht funktionierende API-Verbindung
                -> erwartetes Ergebnis:
                    * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat.
    """
    response = r.get(querystring) #.content.decode('UTF-8')
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Es ist ein Fehler beim Zugriff auf die API aufgetreten oder es besteht kein Objekt mit der "
                        f"angefragten ID.\n\tError Code: {response.status_code}")


def get_student_name(student_id: int) -> str:
    """ Methode zum Erhalt des Namens des Students

    Args: student_id: ID des angeforderten Studentens
    Returns: name: String in Form: "Vorname Nachname"

    Test:
         1) student_id eines vorhandenen Studenten eingeben
            -> erwartetes Ergebnis:
                 * String: "Vorname Nachname" des Studentens
         2) student_id eines nicht vorhandenen Studentens eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
    """
    querystring = url + f"/getStudent/{student_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    data = data_raw[0]
    vorname = data[1]
    nachname = data[2]
    name = vorname + " " + nachname
    return name


def get_dozent_name(dozent_id: int) -> str:
    """ Methode zum Erhalt des Namens des Dozents

    Args: dozent_id: ID des angeforderten Studentens
    Returns: name: String in Form: "Vorname Nachname"

    Test:
         1) dozent_id eines vorhandenen Dozenten eingeben
            -> erwartetes Ergebnis:
                 * String: "Vorname Nachname" des Dozenten
         2) dozent_id eines nicht vorhandenen Dozenten eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
    """
    querystring = url + f"/getDozent/{dozent_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    data = data_raw[0]
    vorname = data[1]
    nachname = data[2]
    name = vorname + " " + nachname
    return name


def get_admin_name(admin_id: int) -> str:
    """
    Methode zum Erhalt des Namens des Admins

    Args: admin_id: ID des angeforderten Studentens
    Returns: name: String in Form: "Vorname Nachname"

    Test:
         1) admin_id eines vorhandenen Admins eingeben
            -> erwartetes Ergebnis:
                 * String: "Vorname Nachname" des Admins
         2) admin_id eines nicht vorhandenen Admins eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
    """
    querystring = url + f"/getAdmin/{admin_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    data = data_raw[0]
    vorname = data[1]
    nachname = data[2]
    name = vorname + " " + nachname
    return name


def login_student(student_id: int, passwort: str) -> bool:
    """ Überprüft Login Daten des Benutzers

    Args: student_id: ID des Studierenden, der sich anmelden möchte
    Returns: True, wenn Passwort zu User passt, ansonsten False
    Test:
         1) gültige ID und dazugehöriges Passwort angeben
            -> erwartetes Ergebnis:
                 * Rückgabewert: True
         2) gültige ID und falsches Passwort angeben
             -> erwartetes Ergebnis:
                 * Rückgabewert: False
    """
    querystring = url + f"/getStudent/{student_id}"
    data_raw = get_values(querystring)[0]
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    if passwort == data_raw[5]:
        return True
    else:
        return False


def login_dozent(dozent_id: int, passwort: str) ->bool:
    """ Überprüft Login Daten des Benutzers

        Args: dozent_id: ID des Dozierenden, der sich anmelden möchte
        Returns: True, wenn Passwort zu User passt, ansonsten False
        Test:
             1) gültige ID und dazugehöriges Passwort angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: True
             2) gültige ID und falsches Passwort angeben
                 -> erwartetes Ergebnis:
                     * Rückgabewert: False
        """
    querystring = url + f"/getDozent/{dozent_id}"
    data_raw = get_values(querystring)[0]
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    if passwort == data_raw[4]:
        return True
    else:
        return False


def login_admin(admin_id: int, passwort: str) -> bool:
    """ Überprüft Login Daten des Benutzers

        Args: admin_id: ID des Admins, der sich anmelden möchte
        Returns: True, wenn Passwort zu User passt, ansonsten False
        Test:
             1) gültige ID und dazugehöriges Passwort angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: True
             2) gültige ID und falsches Passwort angeben
                 -> erwartetes Ergebnis:
                     * Rückgabewert: False
        """
    querystring = url + f"/getAdmin/{admin_id}"
    data_raw = get_values(querystring)[0]
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    if passwort == data_raw[4]:
        return True
    else:
        return False


def edit_pruefung_data(pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung):
    querystring = url + f"/edit_pruefungsleistung_by_student_and_veranstaltung/{pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def create_pruefungsleistung(pruefungsleistung):
    querystring = url + f"/create_pruefungsleistung/{pruefungsleistung}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def access_pruefung_data(student_id: int) -> list[list]:
    querystring = url + f"/getPruefungsleistungenByStudent/{student_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def get_veranstaltung_by_dozent(dozent_id: int) -> list[list]:
    querystring = url + f"/get_all_veranstaltungen_by_dozent/{dozent_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return [data_raw]


def get_all_pruefungsleistungen_by_veranstaltung(veranstaltung_id: int) -> list[list]:
    querystring = url + f"/get_all_pruefungsleistung_by_veranstaltung/{veranstaltung_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw



def get_student_module(student_id: int) -> list[list]:
    # result = []
    # result.append([1234, "Modul1", 5, 1.5])
    # result.append([4234, "Modul2", 7, 2.7])
    # return result
    return Student_be.print_student_module(student_id)


def get_credits_erreicht(student_id: int) -> list[list]:
    return Student_be.get_credits_erreicht(student_id)


def get_gpa_by_student(student_id: int) -> list[list]:
    return Student_be.get_gpa_by_student(student_id)


def get_modul_id_namen_student(student_id: int) -> list[list]:
    return Student_be.get_modul_id_namen_student(student_id)


def get_best_note(student_id):
    return DozentB.best_note(student_id)


def get_worst_note(student_id):
    return DozentB.worst_note(student_id)


def get_mean(student_id):
    return DozentB.get_mean(student_id)


def get_median(student_id):
    return DozentB.get_median(student_id)


def internal_pruefungen_in_modul (student_id: int, modul_id: int):
    querystring = url + f"/getPruefungsleistungenByStudent/{student_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    pruefungen = data_raw
    return pruefungen
    result = []
    for p in pruefungen:
        veranstaltung_id = p[1]
        querystring2 = url + f"/getVeranstaltung/{veranstaltung_id}"
        data_raw2 = get_values(querystring2)
        m_id = data_raw2[3]
        if m_id == modul_id:
            result.append(p)
    return result


def print_all_pruefungen_student (student_id: int, modul_id: int) -> list[list]:
    pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
    result = []
    for p in pruefungen:
        details = []
        v_id = p[1]
        querystring = url + f"/getVeranstaltung/{v_id}"
        data_raw = get_values(querystring)
        veranstaltung = data_raw[0]
        details.append(veranstaltung[1])  # Veranstaltungsname
        details.append(p[2])  # gesamte Punkte
        details.append(p[3])  # erreichte Punkte
        details.append(Student_be.notenberechnung(p[3], p[2]))
        result.append(details)
    return result


def print_pruefungen_in_modul(student_id: int, modul_id: int) -> list[list]:
    pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
    result = []
    for p in pruefungen:
        details = []
        v_id = p[1]
        querystring = url + f"/getVeranstaltung/{v_id}"
        data_raw = get_values(querystring)
        veranstaltung = data_raw[0]
        if veranstaltung[3] == modul_id:
            details.append(veranstaltung[0])  # veranstaltung_id
            details.append(veranstaltung[1])  # Veranstaltungsname
            details.append(p[2])  # gesamte Punkte
            details.append(p[3])  # erreichte Punkte
            details.append(Student_be.notenberechnung(p[3], p[2]))
            result.append(details)
    return result


def create_student(student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str) -> None:
    querystring = url + f"/createStudent/{student_id}/{vorname}/{nachname}/{kurs_id}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_dozent(dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort:str) -> None:
    querystring = url + f"/createDozent/{dozent_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_admin(admin_id: int, vorname: str, nachname: str, nutzername: str, passwort:str) -> None:
    querystring = url + f"/createAdmin/{admin_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_kurs(kurs_id: int, name: str, dozent_id: int) -> None:
    querystring = url + f"/createKurs/{kurs_id}/{name}/{dozent_id}"
    r.get(querystring)
    return None


def create_modul(modul_id: int, modulname: str, module_credits: int, kurs_id: int) -> None:
    querystring = url + f"/createModul/{modul_id}/{modulname}/{module_credits}"
    r.get(querystring)
    return None


def create_veranstaltung(veranstaltung_id: int, name: str, dozent_id: int, modul_id: int) -> None:
    querystring = url + f"/createVeranstaltung/{veranstaltung_id}/{name}/{dozent_id}/{modul_id}"
    r.get(querystring)
    return None


def create_pruefungsleistung(
        student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int) -> None:
    querystring = url + f"/createPruefungsleistung/{student_id}/{veranstaltung_id}/{punkte_gesamt}/{punkte_erreicht}"
    r.get(querystring)
    return None


def change_pw_student(student_id,old_password, new_password):
    old_data = get_student(student_id)[0]
    if old_data[5] == old_password:
        change_student(old_data[0], old_data[0], old_data[1], old_data[2], old_data[3], old_data[4], new_password)
        return "Das Passwort wurde erfolgreich geändert"
    else:
        raise Exception("Ihr Passwort ist nicht korrekt")


def change_pw_dozent(dozent_id, old_password, new_password):
    old_data = get_dozent(dozent_id)
    if old_data[5] == old_password:
        change_dozent(old_data[0], old_data[0], old_data[1], old_data[2], old_data[3], old_data[4], new_password)
        return "Das Passwort wurde erfolgreich geändert"
    else:
        raise Exception("Ihr Passwort ist nicht korrekt")


def change_pw_admin(admin_id, old_password, new_password):
    old_data = get_admin(admin_id)
    if old_data[5] == old_password:
        change_admin(old_data[0], old_data[0], old_data[1], old_data[2], old_data[3], old_data[4], new_password)
        return "Das Passwort wurde erfolgreich geändert"
    else:
        raise Exception("Ihr Passwort ist nicht korrekt")


def change_student(
        student_id_old: int, student_id: int, vorname: str, nachname: str,
        kurs_id: int, nutzername: str, passwort:str):
    querystring = url + f"/changeStudent/{student_id_old}/{student_id}/{vorname}/{nachname}/{kurs_id}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def change_kurs(kurs_id_old: int,kurs_id: int, name: str, dozent_id: int):
    querystring = url + f"/changeKurs/{kurs_id_old}/{kurs_id}/{name}/{dozent_id}"
    r.get(querystring)
    return None


def change_dozent(
        dozent_id_old: int,dozent_id: int, vorname: str,
        nachname: str, nutzername: str, passwort: str):
    querystring = url + f"/changeDozent/{dozent_id_old}/{dozent_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def change_modul(
        modul_id_old: int, modul_id: int, modulname: str, module_credits: int, kurs_id: int):
    querystring = url + f"/changeModul/{modul_id_old}/{modul_id}/{modulname}/{module_credits}"
    r.get(querystring)
    return None


def change_veranstaltung(
        veranstaltung_id_old: int, veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    querystring = url + f"/changeVeranstaltung/{veranstaltung_id_old}/{veranstaltung_id}/{name}/{dozent_id}/{modul_id}"
    r.get(querystring)
    return None


def change_pruefungsleistung(
        student_id_old: int, veranstaltung_id_old: int, student_id: int,
        veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    querystring = url + f"/changePruefungsleistung/{student_id_old}/{veranstaltung_id_old}/{student_id}/{veranstaltung_id}/{punkte_gesamt}/{punkte_erreicht}"
    r.get(querystring)
    return None


def change_admin(
        admin_id_old: int, admin_id: int, vorname: str,
        nachname: str, nutzername: str, passwort: str):
    querystring = url + f"/changeAdmin/{admin_id_old}/{admin_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def delete_student(student_id: int):
    querystring = url + f"/deleteStudent/{student_id}"
    r.get(querystring)
    return None


def delete_dozent(dozent_id: int):
    querystring = url + f"/deleteDozent/{dozent_id}"
    r.get(querystring)
    return None


def delete_admin(admin_id: int):
    querystring = url + f"/deleteAdmin/{admin_id}"
    r.get(querystring)
    return None


def delete_kurs(kurs_id: int):
    querystring = url + f"/deleteKurs/{kurs_id}"
    r.get(querystring)
    return None


def delete_modul(modul_id: int):
    querystring = url + f"/deleteModul/{modul_id}"
    r.get(querystring)
    return None


def delete_veranstaltung(veranstaltung_id: int):
    querystring = url + f"/deleteVeranstaltung/{veranstaltung_id}"
    r.get(querystring)
    return None


def delete_pruefungsleistung(pruefungsleistung_id: int):
    querystring = url + f"/deletePruefungsleistung/{pruefungsleistung_id}"
    r.get(querystring)
    return None


def get_student(student_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz eines Studenten aus der Tabelle Student und liefert diesen als Array zurück

        Args: student_id: ID des Studenten, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [student_id, Vorname, Nachname, Kurs_id,
         Nutzername, passwort]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [student_id, Vorname, Nachname, Kurs_id, Nutzername, passwort] des konkreten
                      Studenten
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getStudent/{student_id}"
    response = get_values(querystring)
    return response


def get_dozent(dozent_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz eines Dozenten aus der Tabelle Dozent und liefert diesen als Array zurück

        Args: dozent_id: ID des Dozenten, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [dozent_id, Vorname, Nachname,
         Nutzername, passwort]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [student_id, Vorname, Nachname, Nutzername, passwort] des konkreten Dozenten
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getDozent/{dozent_id}"
    response = get_values(querystring)
    return response # als Array


def get_admin(admin_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz eines Admins aus der Tabelle Admin und liefert diesen als Array zurück

        Args: admin_id: ID des Admins, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [admin_id, Vorname, Nachname, Nutzername
        , passwort]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [student_id, Vorname, Nachname, Kurs_id, Nutzername, passwort] des konkreten
                      Studenten
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getAdmin/{admin_id}"
    response = get_values(querystring)
    return response # als Array


def get_kurs(kurs_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz eines Kurses aus der Tabelle Kurs und liefert diesen als Array zurück

        Args: kurs_id: ID des Kurses, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [kurs_id,name,dozent_id]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [kurs_id,name,dozent_id] des konkreten Kurses
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getKurs/{kurs_id}"
    response = get_values(querystring)
    return response # als Array


def get_modul(modul_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz eines Moduls aus der Tabelle Modul und liefert diesen als Array zurück

        Args: modul_id: ID des Moduls, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [modul_id,modulname,credits,kurs_id]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [modul_id,modulname,credits,kurs_id] des konkreten Moduls
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getModul/{modul_id}"
    response = get_values(querystring)
    return response


def get_veranstaltung(veranstaltung_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz einer Veranstaltung aus der Tabelle Veranstaltung und liefert diesen als Array
    zurück

        Args: veranstaltung_id: ID der Veranstaltung, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [modul_id,modulname,credits,kurs_id]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [veranstaltung_id,name,dozent_id,modul_id] der konkreten Veranstaltung
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getVeranstaltung/{veranstaltung_id}"
    response = get_values(querystring)
    return response


def get_pruefungsleistung(pruefungsleistung_id: int) -> list[list]:
    """ Ermittelt den gesamten Datensatz einer Prüfungsleistung aus der Tabelle Prüfungsleistung und liefert diesen als
    Array zurück

        Args: pruefungsleistung_id: ID der Prüfungsleistung, dessen Daten angefordert werden
        Returns: Liste mit den Daten in der Reihenfolge aus der Datenbank, also [modul_id,modulname,credits,kurs_id]
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * Rückgabewert: Liste [student_id,veranstaltung_id,punkte_gesamt,punkte_erreicht] der konkreten
                     Prüfungsleistung
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/getPruefungsleistung/{pruefungsleistung_id}"
    response = get_values(querystring)
    return response


if __name__ == "__main__":
    print(get_student(1000))
    print(get_dozent(555))
    print(app.get_pruefungsleistungen_by_student(2000))
    print(get_veranstaltung_by_dozent(120))
    # print(get_modul(1200))
    # print(get_veranstaltung(1000))
    # print(get_veranstaltung(1001))
    # delete_modul(1200)
    # print(get_modul(1200))
    # print(get_veranstaltung(1000))
    # print(get_student(2000))
    # change_student(2000, 2001, "s2001", "Lastname21", 25, "Stud21", "pw")
    # print(get_student(2001))
    # delete_student(2001)
    # print(get_student(2001))
    # print(create_student(1456, "Niklas", "Würfl", 1400, "Nicube", "pässwör1"))
    # print((get_student_name(1459)))
    # print(get_student_name(1000))
    # print(get_dozent_name(110))
      #  print(app.getStudent(1000))
      #  print(app.getDozent(110))
      #  print(db.get_dozent_by_id(db.create_database_connection("data.db"),110))
    # print(get_admin_name(99))
    # print(access_pruefung_data(1000))
    # print(get_student_module(1000))
    # print(get_credits_erreicht(1000))
    # print(get_gpa_by_student(1000))
    # print(get_modul_id_namen_student(1000))
    # print(internal_pruefungen_in_modul(1000,1200))
    # print(print_all_pruefungen_student(1000,1200))
    # print(print_pruefungen_in_modul(1000,1200))
