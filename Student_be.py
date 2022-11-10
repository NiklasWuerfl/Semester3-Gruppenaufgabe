"""
Modul um die nötigen Informationen für die Studenten-Startseite zu erhalten
noch mit Modul "DATABASE" implementiert

    author: Niklas Würfl
    date: 07.11.2022
    version: 1.1.1
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

def get_raw_pruefung_data(student_id):
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

    raw_modul_data = [modul_namen, modul_credits, p_gesamt_list, p_erreicht_list, note_list, bestanden_list, modul_ids]
    return raw_modul_data

def get_raw_modul_data (student_id):
    """
    Error einfügen wenn Prüfungen doppelt sind?
    :param student_id:
    :return:
    """
    m_ids = [*set(get_raw_modul_data(student_id)[6])]
    m_namen = [*set(get_raw_modul_data(student_id)[0])]
    m_credits = [*set(get_raw_modul_data(student_id)[1])]
    m_note = [] # noch berechnen!
    for i in range(len(m_ids)):
        p_e, p_g = 0.0
        for p in get_raw_pruefung_data(student_id):
            if p[6] in m_ids:
                p_g += p[3]
                p_e += p[4]
        m_note.insert(i,notenberechnung(p_e, p_g))

    module_raw = [m_ids, m_namen, m_credits, m_note]
    module_result = []
    for i in range(len(module_raw[0])):
        module_result.append([row[i] for row in module_raw])
    return module_result

def get_student_pruefungen(student_id):
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

    pruefungen = []
    for i in range(len(raw_modul_data[0])):
        pruefungen.append([row[i] for row in raw_modul_data])

    return pruefungen



def get_credits_erreicht(student_id: int):
    ects_list = get_raw_pruefung_data(student_id)[1]
    bestanden = get_raw_pruefung_data(student_id)[5] # evtl. vereinfachbar in ein Array
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


def get_modul_id_namen_student(student_id):
    modul_ids = [*set(get_raw_pruefung_data(student_id)[6])]
    # modul_namen = [*set(get_raw_modul_data(student_id)[0])]
    # module_raw = [modul_ids, modul_namen]
    # module_result = []
    # for i in range(len(module_raw[0])):
    #     module_result.append([row[i] for row in module_raw])
    return modul_ids


def get_pruefungen_in_modul(student_id, modul_id):
    pruefungen = db.get_all_pruefungsleistung_by_student(student_id)
    result = []
    for p in pruefungen:
        if db.get_veranstaltung_by_id(p[1])[3] == modul_id:
            result.append(p)

