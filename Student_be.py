"""
Modul um die nötigen Informationen für die Studenten-Startseite zu erhalten

    author: Niklas Würfl
    date: 03.11.2022
    version: 1.1.0
    licence: free (open source)
"""
import database as db

def get_student_name(student_id):
    """
    Methode zum Erhalt des Namens des Students

    :param student_id:
    :return: name: String in Form: "Nachname, Vorname"

    Tests:
    * ungültige Student_id eingeben
    *
    """
    vorname = db.get_student_by_id(student_id)[1]
    nachname = db.get_student_by_id(student_id)[2]
    name = nachname + ", " + vorname
    return name



def notenberechnung(p_erreicht, p_gesamt):
    note = 1 + 3 * ((p_gesamt-p_erreicht)/(p_gesamt/2))
    return note

def get_raw_modul_data(student_id):
    pruefungen = db.get_all_pruefungsleistung_by_student(student_id)
    veranstaltung_ids, modul_ids, veranstaltung_namen = []
    modul_namen, modul_credits, modul_noten = []  # Namen der Module des Studenten
    p_gesamt_list, p_erreicht_list, note_list, bestanden_list = []
    for i in pruefungen:
        veranstaltung_ids.append(i[1])
        veranstaltung_namen.append(db.get_veranstaltung_by_id(i[1])[1])
        modul_ids.append(db.get_veranstaltung_by_id(i[1])[3])
        modul_namen.append(db.get_modul_by_id(db.get_veranstaltung_by_id(i[1])[2]))

        p_erreicht_list.append(i[3])
        p_gesamt_list.append(i[2])
        note = notenberechnung(i[3], i[2])
        note_list.append(note)
        bestanden_list.append(note <= 4.0)

    raw_modul_data = []
    raw_modul_data.append(modul_namen)
    raw_modul_data.append(modul_credits)
    raw_modul_data.append(p_gesamt_list)
    raw_modul_data.append(p_erreicht_list)
    raw_modul_data.append(note_list)
    raw_modul_data.append(bestanden_list)
    return raw_modul_data

def get_student_module(student_id):
    """
    Methode zum Erlangen des Dataframes mit allen relevanten Modulen und Noten für die Tabelle in der Startseite
    :param student_id:
    :return: module_df: Dataframe mit allen Modul-Namen, deren Veranstaltungen, Teilpunkten, Credits und Gesamtnoten

    Tests:
    *
    *
    """
    # noch nicht gelöst: Veranstaltungen in ein Modul einbauen
    raw_modul_data = get_raw_modul_data(student_id)

    module = []
    for i in range(len(raw_modul_data[0])):
        module.append([row[i] for row in raw_modul_data])

    return module


def get_credits_erreicht(student_id: int):
    ects_list = get_raw_modul_data(student_id)[1]
    bestanden = get_raw_modul_data(student_id)[5] # evtl. vereinfachbar in ein Array
    credits_erreicht = 0

    for i in range(len(ects_list)):
        if bestanden[i]:
            credits_erreicht += ects_list[i]

    # kurs_id = db.get_student_by_id(student_id)[3]

    # punkte_erreicht = 0
    # for pruefung in db.get_all_pru vbefungsleistung_by_student(student_id):
    #     punkte_erreicht += pruefung[1]
    # credits_list = db.get_modul_by_id()[2]

    return credits_erreicht


def get_gpa_by_student(student_id):
    gewichtete_noten_sum, ects_reached = 0.0
    credits = get_raw_modul_data(student_id)[1]
    note = get_raw_modul_data(student_id)[4]
    bestanden = get_raw_modul_data(student_id)[5]
    for i in range(len(credits)):
        if bestanden[i]:
            gewichtete_noten_sum += credits[i] * note[i]
            ects_reached += credits[i]
    #alle_noten = db.get_all_modules(student_id)
    #ects_reached = get_credits_erreicht(student_id)
    # print(alle_noten)
    # print(ects_reached)
    # print (list(alle_noten.values()))

    gpa = gewichtete_noten_sum/ects_reached
    return gpa
