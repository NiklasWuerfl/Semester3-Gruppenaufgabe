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

import database as db
import pandas as pd
import fastapi as api

def get_gpa(student_id):
    """
    Berechnet GPA
    noch wird die Bachelorarbeit und die Credit-Anzahl nicht berücksichtigt

    :param student_id
    :return: gpa: Float

    Test:
        * ungültige student_id angeben
        *
    """

    alle_noten = db.get_all_modules(student_id)
    ects_reached = 0
    # print(alle_noten)
    # print(ects_reached)
    # print (list(alle_noten.values()))
    gewichtete_noten_sum = 0.0
    for i in alle_noten.values():
        gewichtete_noten_sum += i[0] * i[1]
        ects_reached += i[0]

    gpa = gewichtete_noten_sum/ects_reached
    return gpa
