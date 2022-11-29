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


def internal_pruefungen_in_modul (student_id, modul_id):
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
def print_pruefungen_in_modul (student_id, modul_id):
    pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
    result = []
    for p in pruefungen:
        details = []
        v_id = p[1]
        querystring = url + f"/getVeranstaltung/{v_id}"
        data_raw = getValues(querystring)
        veranstaltung = data_raw
        details.append(veranstaltung[1])  # Veranstaltungsname
        details.append(p[2])  # gesamte Punkte
        details.append(p[3])  # erreichte Punkte
        details.append(Student_be.notenberechnung(p[3], p[2]))
        result.append(details)
    return result

if __name__ == "__main__":
    print(print_pruefungen_in_modul(1000,1200))
