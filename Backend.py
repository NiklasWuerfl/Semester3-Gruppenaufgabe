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
from flask import Flask
import database as db
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
    """ Methode zum Erhalt des Namens des Dozenten

    Args: dozent_id: ID des angeforderten Dozenten
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

    Args: admin_id: ID des angeforderten Admins
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
    """ Methode zum Ändern der Prüfungsdaten

    Args: pruefungsleistung_student: Pruefungsleistung des angeforderten Studenten als int
          pruefungsleistung_veranstaltung: pruefungsleistung der gesamten Veranstaltung als Liste

    Returns: data_raw: veränderte Prüfungsdaten

    Test:
         1) Prüfungsleistung eines vorhandenen Studentens verändern
            -> erwartetes Ergebnis:
                 * verändert die Note des Studentens
         2) Prüfungsleistung eines nicht vorhandenen Studentens verändern
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """

    querystring = url + f"/edit_pruefungsleistung_by_student_and_veranstaltung/{pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw


def create_pruefungsleistung(pruefungsleistung):
    """ Methode zum Erstellen der Prüfungsdaten

    Args: pruefungsleistung: prüfungsleistung als int

    Returns: data_raw: erstellte Prüfungsdaten

    Test:
         1) Prüfungsleistung eines vorhandenen Studentens erstellen
            -> erwartetes Ergebnis:
                 * erstellt die Prüfungsleistung des Studentens
         2) Prüfungsleistung eines nicht vorhandenen Studentens erstellen
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """

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
    """ Methode, um die Veranstaltungen eines Dozenten zu bekommen

    Args: dozent_id: ID des Dozierenden, von dem man die Veranstaltungen möchte

    Returns: data_raw: die Veranstaltungen des Dozenten als Liste

    Test:
         1) gültige ID angeben
                -> erwartetes Ergebnis:
                     * Veranstaltungen des Dozenten
             2) ungültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """

    querystring = url + f"/get_all_veranstaltungen_by_dozent/{dozent_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return [data_raw]


def get_all_pruefungsleistungen_by_veranstaltung(veranstaltung_id: int) -> list[list]:
    """ Methode, um die Prüfungsleistungen einer Veranstaltung zu bekommen

    Args: veranstaltung_id: ID der Veranstaltung, von der man die Prüfungsleistungen möchte

    Returns: data_raw: die Prüfungsleistungen der Veranstaltung als Liste

    Test:
         1) gültige ID angeben
                -> erwartetes Ergebnis:
                     * Prüfungsleistungen der Veranstaltung als Liste
             2) ungültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """

    querystring = url + f"/get_all_pruefungsleistung_by_veranstaltung/{veranstaltung_id}"
    data_raw = get_values(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    return data_raw



def get_student_module(student_id: int) -> list[list]:
    """ Methode zum Erhalt aller Module und zugehörigen Informationen eines Studenten

     Args: student_id: ID des angeforderten Studenten
     Returns: list: strukturierte Liste in Form von [modul_id, name, credits, note, bestanden] für jedes Modul des
     konkreten Studenten

     Test:
          1) student_id eines vorhandenen Studenten eingeben
             -> erwartetes Ergebnis:
                  * Liste: [[modul_id, name, credits, note, bestanden], [modul_id, name, credits, note, bestanden]]
          2) student_id eines nicht vorhandenen Dozenten eingeben
              -> erwartetes Ergebnis:
                  * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                  nicht existiert.
         3) Test mit laufender bzw. nicht laufender API, bei nicht laufender, soll Exception ausgelöst werden.
     """

    return Student_be.print_student_module(student_id)


def get_gpa_and_credits_student(student_id: int) -> list[list]:
    """ Methode zum Erhalt des Durchschnitts und der erreichten Credits eines Studenten

    Args: student_id: ID des angeforderten Studenten
    Returns: list: Liste in Form von [gpa, credits_erreicht] für den konkreten Studenten

    Test:
         1) student_id eines vorhandenen Studenten eingeben
            -> erwartetes Ergebnis:
                 * Liste: [gpa, credits_erreicht]
         2) student_id eines nicht vorhandenen Dozenten eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        3) Test mit laufender bzw. nicht laufender API, bei nicht laufender, soll Exception ausgelöst werden.
    """

    return Student_be.get_gpa_and_credits_student(student_id)


# def get_modul_id_namen_student(student_id: int) -> list[list]:
#     return Student_be.get_modul_id_namen_student(student_id)


def get_best_note(veranstaltung_id):
    """ Methode, um die beste Note einer Veranstaltung zu bekommen

    Args: veranstaltung_id: ID der Veranstaltung, von der man die beste Note möchte

    Returns: data_raw: die beste Note der Veranstaltungen 

    Test:
         1) gültige ID angeben
                -> erwartetes Ergebnis:
                     * beste Note der Veranstaltungen
             2) ungültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """
    return DozentB.best_note(veranstaltung_id)


def get_worst_note(veranstaltung_id):
    """ Methode, um die schlechteste Note einer Veranstaltung zu bekommen

    Args: veranstaltung_id: ID der Veranstaltung, von der man die schlechteste Note möchte

    Returns: data_raw: die schlechteste Note der Veranstaltungen 

    Test:
         1) gültige ID angeben
                -> erwartetes Ergebnis:
                     * schlechteste Note der Veranstaltungen
             2) ungültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """
    return DozentB.worst_note(veranstaltung_id)


def get_mean(veranstaltung_id):
    """ Methode, um den Mittelwert einer Veranstaltung zu bekommen

    Args: veranstaltung_id: ID der Veranstaltung, von der man den Mittelwert möchte

    Returns: data_raw: der Mittelwert der Veranstaltungen 

    Test:
         1) gültige ID angeben
                -> erwartetes Ergebnis:
                     * Mittelwert der Veranstaltungen
             2) ungültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """
    return DozentB.get_mean(veranstaltung_id)


def get_median(veranstaltung_id):
    """ Methode, um den Median einer Veranstaltung zu bekommen

    Args: veranstaltung_id: ID der Veranstaltung, von der man den Median möchte

    Returns: data_raw: der Median der Veranstaltungen 

    Test:
         1) gültige ID angeben
                -> erwartetes Ergebnis:
                     * Median der Veranstaltungen
             2) ungültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        """
    return DozentB.get_median(veranstaltung_id)


def internal_pruefungen_in_modul (student_id: int) -> list[list]:
    """ Methode zum Erhalt aller Prüfungen eines Studenten (egal welches Modul)

    Args:   student_id: ID des angeforderten Studenten
    Returns: list: Liste von Listen in Form von [veranstaltung_id,punkte_gesamt,punkte_erreicht] für den konkreten
    Studenten

    Test:
         1) student_id eines vorhandenen Studenten eingeben
            -> erwartetes Ergebnis:
                 * Liste: [veranstaltung_id,punkte_gesamt,punkte_erreicht]
         2) student_id eines nicht vorhandenen Studenten eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        3) Test mit laufender bzw. nicht laufender API, bei nicht laufender, soll Exception ausgelöst werden.
    """
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


# def print_all_pruefungen_student (student_id: int, modul_id: int) -> list[list]:
#     """ Methode zum Erhalt aller Prüfungen eines Studenten in einem Modul
#
#     Args:   student_id: ID des angeforderten Studenten
#             modul_id: ID des angefragten Moduls
#     Returns: list: Liste von Listen in Form von [veranstaltung_id,punkte_gesamt,punkte_erreicht] für den konkreten
#     Studenten und das konkrete Modul
#
#     Test:
#          1) student_id eines vorhandenen Studenten und modul_id eines vorhandenen Moduls eingeben
#             -> erwartetes Ergebnis:
#                  * Liste: [veranstaltung_id,punkte_gesamt,punkte_erreicht]
#          2) student_id eines nicht vorhandenen Dozenten eingeben
#              -> erwartetes Ergebnis:
#                  * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
#                  nicht existiert.
#         3) Test mit laufender bzw. nicht laufender API, bei nicht laufender, soll Exception ausgelöst werden.
#     """
#     pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
#     result = []
#     for p in pruefungen:
#         details = []
#         v_id = p[1]
#         querystring = url + f"/getVeranstaltung/{v_id}"
#         data_raw = get_values(querystring)
#         veranstaltung = data_raw[0]
#         details.append(veranstaltung[1])  # Veranstaltungsname
#         details.append(p[2])  # gesamte Punkte
#         details.append(p[3])  # erreichte Punkte
#         details.append(Student_be.notenberechnung(p[3], p[2]))
#         result.append(details)
#     return result


def print_pruefungen_in_modul(student_id: int, modul_id: int) -> list[list]:
    """ Methode zum Erhalt aller Prüfungen eines Studenten in einem bestimmten Modul

    Args:   student_id: ID des angeforderten Studenten
            modul_id: ID des angefragten Moduls
    Returns: list: Liste von Listen in Form von [veranstaltung_id,punkte_gesamt,punkte_erreicht] für den konkreten
    Studenten und das konkrete Modul

    Test:
         1) student_id eines vorhandenen Studenten und modul_id eines vorhandenen Moduls eingeben
            -> erwartetes Ergebnis:
                 * Liste: [veranstaltung_id,punkte_gesamt,punkte_erreicht]
         2) student_id eines nicht vorhandenen Studenten eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        3) Test mit laufender bzw. nicht laufender API, bei nicht laufender, soll Exception ausgelöst werden.
    """
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
    """ Erstellt den Datensatz eines Studenten

        Args:   student_id: int:        neue ID
                vorname: str:           neuer Vorname
                nachname: str:          neuer Nachname
                kurs_id: int:           neue Kurs_id
                nutzername: str:        neuer Nutzername
                passwort: str:          neues Passwort
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createStudent/{student_id}/{vorname}/{nachname}/{kurs_id}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_dozent(dozent_id: int, vorname: str, nachname: str, nutzername: str, passwort:str) -> None:
    """ Erstellt den Datensatz eines Dozenten

        Args:   dozent_id: int:         neue ID
                vorname: str:           neuer Vorname
                nachname: str:          neuer Nachname
                nutzername: str:        neuer Nutzername
                passwort: str:          neues Passwort
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createDozent/{dozent_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_admin(admin_id: int, vorname: str, nachname: str, nutzername: str, passwort:str) -> None:
    """ Erstellt den Datensatz eines Admins

        Args:   admin_id: int:          neue ID
                vorname: str:           neuer Vorname
                nachname: str:          neuer Nachname
                nutzername: str:        neuer Nutzername
                passwort: str:          neues Passwort
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createAdmin/{admin_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def create_kurs(kurs_id: int, name: str, dozent_id: int) -> None:
    """ Erstellt den Datensatz eines Kurses

        Args:   kurs_id: int:        neue ID
                name: str:           neuer Name
                dozent_id: str:      ID des neuen Studiengangsleiters

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createKurs/{kurs_id}/{name}/{dozent_id}"
    r.get(querystring)
    return None


def create_modul(modul_id: int, modulname: str, module_credits: int, kurs_id: int) -> None:
    """ Erstellt den Datensatz eines Moduls

        Args:   modul_id: int:        neue ID
                modulname: str:       neuer Name
                module_credits: int:  neue Anzahl an Credits

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createModul/{modul_id}/{modulname}/{module_credits}/{kurs_id}"
    r.get(querystring)
    return None


def create_veranstaltung(veranstaltung_id: int, name: str, dozent_id: int, modul_id: int) -> None:
    """ Erstellt den Datensatz einer Veranstaltung

        Args:   veranstaltung_id: int:        neue ID
                name: str:                    neuer Name
                dozent_id: int:               ID des neuen Dozenten
                modul_id: int:                neue modul_id des Moduls, in dem die Veranstaltung stattfindet

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createVeranstaltung/{veranstaltung_id}/{name}/{dozent_id}/{modul_id}"
    r.get(querystring)
    return None


def create_pruefungsleistung(
        student_id: int, veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int) -> None:
    """ Erstellt den Datensatz einer Prüfungsleistung

        Args:   student_id: int:        neue ID
                veranstaltung_id: int:  neue ID
                punkte_gesamt: int      neue Gesamtpunktzahl
                punkte_erreicht: int    neue erreichte Punktzahl

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank erstellt
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/createPruefungsleistung/{student_id}/{veranstaltung_id}/{punkte_gesamt}/{punkte_erreicht}"
    r.get(querystring)
    return None


def change_pw_student(student_id: int, old_password: str, new_password: str) -> str:
    """ Ändert das Passwort eines Studenten

        Args:   student_id: int:        ID
                old_password: str:      altes Passwort
                new_password: str:      neues Passwort

        Returns: String
        Test:
             1) laufende API, gültige ID und gültiges altes Passwort angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Passwort werden in Datenbank verändert
                     * Rückgabewert: String: "Das Passwort wurde erfolgreich geändert"
             2) laufende API, gültige ID und ungültiges altes Passwort angeben
                 -> erwartetes Ergebnis:
                     * Exception: "Ihr Passwort ist nicht korrekt"
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    old_data = get_student(student_id)[0]
    if old_data[5] == old_password:
        change_student(old_data[0], old_data[0], old_data[1], old_data[2], old_data[3], old_data[4], new_password)
        return "Das Passwort wurde erfolgreich geändert"
    else:
        raise Exception("Ihr Passwort ist nicht korrekt")


def change_pw_dozent(dozent_id: int, old_password: str, new_password: str) -> str:
    """ Ändert das Passwort eines Dozenten

        Args:   dozent_id: int:         ID
                old_password: str:      altes Passwort
                new_password: str:      neues Passwort

        Returns: String
        Test:
             1) laufende API, gültige ID und gültiges altes Passwort angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Passwort werden in Datenbank verändert
                     * Rückgabewert: String: "Das Passwort wurde erfolgreich geändert"
             2) laufende API, gültige ID und ungültiges altes Passwort angeben
                 -> erwartetes Ergebnis:
                     * Exception: "Ihr Passwort ist nicht korrekt"
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    old_data = get_dozent(dozent_id)[0]
    if old_data[4] == old_password:
        change_dozent(old_data[0], old_data[0], old_data[1], old_data[2], old_data[3], new_password)
        return "Das Passwort wurde erfolgreich geändert"
    else:
        raise Exception("Ihr Passwort ist nicht korrekt")


def change_pw_admin(admin_id: int, old_password: str, new_password: str) -> str:
    """ Ändert das Passwort eines Admins

        Args:   admin_id: int:          ID
                old_password: str:      altes Passwort
                new_password: str:      neues Passwort

        Returns: String
        Test:
             1) laufende API, gültige ID und gültiges altes Passwort angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Passwort werden in Datenbank verändert
                     * Rückgabewert: String: "Das Passwort wurde erfolgreich geändert"
             2) laufende API, gültige ID und ungültiges altes Passwort angeben
                 -> erwartetes Ergebnis:
                     * Exception: "Ihr Passwort ist nicht korrekt"
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    old_data = get_admin(admin_id)[0]
    if old_data[4] == old_password:
        change_admin(old_data[0], old_data[0], old_data[1], old_data[2], old_data[3], new_password)
        return "Das Passwort wurde erfolgreich geändert"
    else:
        raise Exception("Ihr Passwort ist nicht korrekt")


def change_student(
        student_id_old: int, student_id: int, vorname: str, nachname: str,
        kurs_id: int, nutzername: str, passwort: str) -> None:
    """ Verändert den Datensatz eines Studenten

        Args:   student_id_old: int:    ID vor dem Bearbeiten des Datensatzes
                student_id: int:        neue ID
                vorname: str:           neuer Vorname
                nachname: str:          neuer Nachname
                kurs_id: int:           neue Kurs_id
                nutzername: str:        neuer Nutzername
                passwort: str:          neues Passwort
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changeStudent/{student_id_old}/{student_id}/{vorname}/{nachname}/{kurs_id}/{nutzername}/" \
                        f"{passwort}"
    r.get(querystring)
    return None


def change_kurs(kurs_id_old: int,kurs_id: int, name: str, dozent_id: int) -> None:
    """ Verändert den Datensatz eines Kurses

        Args:   kurs_id_old: int:    ID vor dem Bearbeiten des Datensatzes
                kurs_id: int:        neue ID
                name: str:           neuer Name
                dozent_id: str:      ID des neuen Studiengangsleiters

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changeKurs/{kurs_id_old}/{kurs_id}/{name}/{dozent_id}"
    r.get(querystring)
    return None


def change_dozent(
        dozent_id_old: int,dozent_id: int, vorname: str,
        nachname: str, nutzername: str, passwort: str) -> None:
    """ Verändert den Datensatz eines Dozenten

        Args:   dozent_id_old: int:     ID vor dem Bearbeiten des Datensatzes
                dozent_id: int:         neue ID
                vorname: str:           neuer Vorname
                nachname: str:          neuer Nachname
                nutzername: str:        neuer Nutzername
                passwort: str:          neues Passwort
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changeDozent/{dozent_id_old}/{dozent_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def change_modul(
        modul_id_old: int, modul_id: int, modulname: str, module_credits: int, kurs_id: int) -> None:
    """ Verändert den Datensatz eines Moduls

        Args:   modul_id_old: int:    ID vor dem Bearbeiten des Datensatzes
                modul_id: int:        neue ID
                modulname: str:       neuer Name
                module_credits: int:  neue Anzahl an Credits

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changeModul/{modul_id_old}/{modul_id}/{modulname}/{module_credits}/{kurs_id}"
    r.get(querystring)
    return None


def change_veranstaltung(
        veranstaltung_id_old: int, veranstaltung_id: int, name: str, dozent_id: int, modul_id: int) -> None:
    """ Verändert den Datensatz einer Veranstaltung

        Args:   veranstaltung_id_old: int:    ID vor dem Bearbeiten des Datensatzes
                veranstaltung_id: int:        neue ID
                name: str:                    neuer Name
                dozent_id: int:               ID des neuen Dozenten
                modul_id: int:                neue modul_id des Moduls, in dem die Veranstaltung stattfindet

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changeVeranstaltung/{veranstaltung_id_old}/{veranstaltung_id}/{name}/{dozent_id}/{modul_id}"
    r.get(querystring)
    return None


def change_pruefungsleistung(
        student_id_old: int, veranstaltung_id_old: int, student_id: int,
        veranstaltung_id: int, punkte_gesamt: int, punkte_erreicht: int) -> None:
    """ Verändert den Datensatz einer Prüfungsleistung

        Args:   student_id_old: int:    ID vor dem Bearbeiten des Datensatzes
                veranstaltung_id_old: int: ID vor dem Bearbeiten des Datensatzes
                student_id: int:        neue ID
                veranstaltung_id: int:  neue ID
                punkte_gesamt: int      neue Gesamtpunktzahl
                punkte_erreicht: int    neue erreichte Punktzahl

        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changePruefungsleistung/{student_id_old}/{veranstaltung_id_old}/{student_id}/{veranstaltung_id}/{punkte_gesamt}/{punkte_erreicht}"
    r.get(querystring)
    return None


def change_admin(
        admin_id_old: int, admin_id: int, vorname: str,
        nachname: str, nutzername: str, passwort: str) -> None:
    """ Verändert den Datensatz eines Admins

        Args:   admin_id_old: int:    ID vor dem Bearbeiten des Datensatzes
                admin_id: int:        neue ID
                vorname: str:           neuer Vorname
                nachname: str:          neuer Nachname
                nutzername: str:        neuer Nutzername
                passwort: str:          neues Passwort
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Daten werden in Datenbank aktualisiert
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/changeAdmin/{admin_id_old}/{admin_id}/{vorname}/{nachname}/{nutzername}/{passwort}"
    r.get(querystring)
    return None


def delete_student(student_id: int) -> None:
    """ Löscht den Datensatz eines Studenten

        Args: student_id: ID des Studenten, dessen Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
        """
    querystring = url + f"/deleteStudent/{student_id}"
    r.get(querystring)
    return None


def delete_dozent(dozent_id: int) -> None:
    """ Löscht den Datensatz eines Dozenten

        Args: dozent_id: ID des Dozenten, dessen Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
    """
    querystring = url + f"/deleteDozent/{dozent_id}"
    r.get(querystring)
    return None


def delete_admin(admin_id: int) -> None:
    """ Löscht den Datensatz eines Admins

        Args: admin_id: ID des Admins, dessen Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
    """
    querystring = url + f"/deleteAdmin/{admin_id}"
    r.get(querystring)
    return None


def delete_kurs(kurs_id: int) -> None:
    """ Löscht den Datensatz eines Kurses

        Args: kurs_id: ID des Kurses, dessen Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
    """
    querystring = url + f"/deleteKurs/{kurs_id}"
    r.get(querystring)
    return None


def delete_modul(modul_id: int) -> None:
    """ Löscht den Datensatz eines Moduls

        Args: modul_id: ID des Moduls, dessen Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
    """
    querystring = url + f"/deleteModul/{modul_id}"
    r.get(querystring)
    return None


def delete_veranstaltung(veranstaltung_id: int) -> None:
    """ Löscht den Datensatz einer Veranstaltung

        Args: veranstaltung_id: ID der Veranstaltung, deren Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
    """
    querystring = url + f"/deleteVeranstaltung/{veranstaltung_id}"
    r.get(querystring)
    return None


def delete_pruefungsleistung(pruefungsleistung_id: int) -> None:
    """ Löscht den Datensatz einer Prüfungsleistung

        Args: pruefungsleistung_id: ID der Prüfungsleistung, deren Daten gelöscht werden sollen
        Returns: None
        Test:
             1) laufende API und gültige ID angeben
                -> erwartetes Ergebnis:
                     * kein Fehler
                     * Rückgabewert: None
             2) nicht laufende API und gültige ID angeben
                 -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API
            3) laufende API und ungültige ID angeben
                -> erwartetes Ergebnis:
                     * Exception: Fehler bei Verbindung zu API bzw. Objekt nicht gefunden
    """
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
    print(app.get_all_veranstaltungen_by_dozent(110))
    # print(change_pw_student(1000, "passwort", "neu"))
    # print(get_veranstaltung_by_dozent(310))
    # print(get_student(1000))
    # print(get_dozent(555))
    # print(app.get_pruefungsleistungen_by_student(2000))
    # print(get_veranstaltung_by_dozent(120))
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
