"""
    Modul für interne Berechnungen bzw. Datenbereitstellung
    muss wahrscheinlich noch aufgeteilt werden für Unterfunktionen

    benötigte Funktionen
        * Jegliche Datenarten aus der Datenbank holen/Datenbank aktualisieren
        * Rollenüberprüfung -> Ausgabe an Frontend
        * Durchschnitt/Beste bzw. schlechteste Note/Median für Klausur bestimmen
        * GPA für Student berechnen


    Beinhaltet API? -> FastAPI

    Frontend -> Backend:
        -	Login
        -	Anfragen je nach User:
            o	Startseite (wird immer angefragt)
                -	Spezielle Anfrage (wird nur nach User-Interaktion angefragt)
            o	Studenten: GPA, bisherige Credits
                -	Unterseite: Alle Module, Noten (pro Semester?)
            o	Dozenten: Klausuren und deren Durchschnitte
                -	Einstellung: bester, schlechteste, Median
                -	Eingabe: Noten der Studierenden
            o	Admin: Liste der angelegten User
                -	Eingabe: User verwalten (erstellen, zuweisen, löschen)

    Backend -> Frontend:
        -	Rolle des Users


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

# querystring = url + f"/getPruefungsleistungenByStudent/{student_id}"


def getValues (querystring):
    response = r.get(querystring) #.content.decode('UTF-8')
    if (response.status_code == 200):
        return response.json()
    else:
        raise Exception(f"Es ist ein Fehler beim Zugriff auf die API aufgetreten.\n\tError Code: {response.status_code}")


def get_student_name(student_id):
    """
    Methode zum Erhalt des Namens des Students

    :param student_id:
    :return: name: String in Form: "Nachname, Vorname"

    Tests:
    * ungültige Student_id eingeben
    *
    """
    querystring = url + f"/getStudent/{student_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    data = data_raw[0]
    vorname = data[1]
    nachname = data[2]
    name = nachname + ", " + vorname
    return name


def get_dozent_name(dozent_id):
    """
    Methode zum Erhalt des Namens des Students

    :param dozent_id:
    :return: name: String in Form: "Nachname, Vorname"

    Tests:
    * ungültige Dozent_id eingeben
    *
    """
    querystring = url + f"/getDozent/{dozent_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    data = data_raw[0]
    vorname = data[1]
    nachname = data[2]
    name = nachname + ", " + vorname
    return name


def get_admin_name(admin_id):
    """
    Methode zum Erhalt des Namens des Students

    :param admin_id:
    :return: name: String in Form: "Nachname, Vorname"

    Tests:
    * ungültige Student_id eingeben
    *
    """
    querystring = url + f"/getAdmin/{admin_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    data = data_raw[0]
    vorname = data[1]
    nachname = data[2]
    name = nachname + ", " + vorname
    return name


def edit_pruefung_data(pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung):
    querystring = url + f"/edit_pruefungsleistung_by_student_and_veranstaltung/{pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def create_pruefungsleistung(pruefungsleistung):
    querystring = url + f"/create_pruefungsleistung/{pruefungsleistung}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def access_pruefung_data(student_id):
    querystring = url + f"/getPruefungsleistungenByStudent/{student_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def get_student_module(student_id):
    return Student_be.print_student_module(student_id)


def get_credits_erreicht(student_id):
    return Student_be.get_credits_erreicht(student_id)


def get_gpa_by_student(student_id):
    return Student_be.get_gpa_by_student(student_id)


def get_modul_id_namen_student(student_id):
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
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    pruefungen = data_raw
    return pruefungen
    result = []
    for p in pruefungen:
        veranstaltung_id = p[1]
        querystring2 = url + f"/getVeranstaltung/{veranstaltung_id}"
        data_raw2 = getValues(querystring2)
        m_id = data_raw2[3]
        if m_id == modul_id:
            result.append(p)
    return result


def print_all_pruefungen_student (student_id, modul_id):
    pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
    result = []
    for p in pruefungen:
        details = []
        v_id = p[1]
        querystring = url + f"/getVeranstaltung/{v_id}"
        data_raw = getValues(querystring)
        veranstaltung = data_raw[0]
        details.append(veranstaltung[1])  # Veranstaltungsname
        details.append(p[2])  # gesamte Punkte
        details.append(p[3])  # erreichte Punkte
        details.append(Student_be.notenberechnung(p[3], p[2]))
        result.append(details)
    return result


def print_pruefungen_in_modul(student_id, modul_id):
    pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
    result = []
    for p in pruefungen:
        details = []
        v_id = p[1]
        querystring = url + f"/getVeranstaltung/{v_id}"
        data_raw = getValues(querystring)
        veranstaltung = data_raw[0]
        if veranstaltung[3] == modul_id:
            details.append(veranstaltung[1])  # Veranstaltungsname
            details.append(p[2])  # gesamte Punkte
            details.append(p[3])  # erreichte Punkte
            details.append(Student_be.notenberechnung(p[3], p[2]))
            result.append(details)
    return result


def create_student(student_id: int, vorname: str, nachname: str, kurs_id: int, nutzername: str, passwort:str):
    querystring = url + f"/createStudent/{student_id}/{vorname}/{nachname}/{kurs_id}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_dozent(dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort:str):
    querystring = url + f"/createDozent/{dozent_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_admin(admin_id: int, vorname: str, nachname: str, nutzername: str, passwort:str):
    querystring = url + f"/createAdmin/{admin_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_kurs(kurs_id: int, name: str, dozent_id: int):
    querystring = url + f"/createKurs/{kurs_id}/{name}/{dozent_id}"
    r.get(querystring)
    return None


def create_modul(modul_id: int, modulname: str, module_credits: int, kurs_id: int):
    querystring = url + f"/createModul/{modul_id}/{modulname}/{module_credits}"
    r.get(querystring)
    return None


def create_veranstaltung(veranstaltung_id: int, name: str, dozent_id: int, modul_id: int):
    querystring = url + f"/createVeranstaltung/{veranstaltung_id}/{name}/{dozent_id}/{modul_id}"
    r.get(querystring)
    return None


def create_pruefungsleistung(
        student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int):
    querystring = url + f"/createPruefungsleistung/{student_id}/{veranstaltung_id}/{punkte_gesamt}/{punkte_erreicht}"
    r.get(querystring)
    return None


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
    querystring = url + f"/createDozent/{dozent_id_old}/{dozent_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
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


def get_student(student_id: int):
    querystring = url + f"/getStudent/{student_id}"
    response = getValues(querystring)
    return response # als Array


def get_dozent(dozent_id: int):
    querystring = url + f"/deleteDozent/{dozent_id}"
    response = getValues(querystring)
    return response # als Array


def get_admin(admin_id: int):
    querystring = url + f"/getAdmin/{admin_id}"
    response = getValues(querystring)
    return response # als Array


def get_kurs(kurs_id: int):
    querystring = url + f"/getKurs/{kurs_id}"
    response = getValues(querystring)
    return response # als Array


def get_modul(modul_id: int):
    querystring = url + f"/getModul/{modul_id}"
    response = getValues(querystring)
    return response # als Array


def get_veranstaltung(veranstaltung_id: int):
    querystring = url + f"/getVeranstaltung/{veranstaltung_id}"
    response = getValues(querystring)
    return response # als Array


def get_pruefungsleistung(pruefungsleistung_id: int):
    querystring = url + f"/getPruefungsleistung/{pruefungsleistung_id}"
    response = getValues(querystring)
    return response # als Array


if __name__ == "__main__":
    print(create_student(1456, "Niklas", "Würfl", 1400, "Nicube", "pässwör1"))
    print((get_student_name(1459)))
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
