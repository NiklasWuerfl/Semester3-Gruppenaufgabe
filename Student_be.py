"""
Modul um die nötigen Informationen für die Studenten-Startseite zu erhalten

    author: Niklas Würfl
    date: 04.12.2022
    version: 1.3
    licence: free (open source)
"""
import Backend as be


def notenberechnung(p_erreicht: int, p_gesamt: int) -> float:
    """ berechnet aus Gesamtpunktzahl und erreichter Punktzahl die Note aus (nach DHBW-Richtlinien

    :param p_erreicht:
    :param p_gesamt:
    :return:
    """
    note = 1 + 3 * ((p_gesamt-p_erreicht)/(p_gesamt/2))
    note = int(note*10)
    note /= 10
    return note


def get_raw_pruefung_data(student_id):
    pruefungen = be.access_pruefung_data(student_id)
    veranstaltung_ids = []
    modul_ids = []
    veranstaltung_namen =[]
    # unnötige Variablen enthalten
    modul_namen = []
    modul_credits = []
    modul_noten = []  # Namen der Module des Studenten
    p_gesamt_list =[]
    p_erreicht_list = []
    note_list = []
    bestanden_list = []
    for i in pruefungen:
        v_id = i[1]
        veranstaltung_ids.append(v_id)
        querystring = be.url + f"/getVeranstaltung/{v_id}"
        veranstaltung = be.get_values(querystring)[0]
        veranstaltung_namen.append(veranstaltung[1])
        m_id = veranstaltung[3]
        modul_ids.append(m_id)
        querystring = be.url + f"/getModul/{m_id}"
        modul = be.get_values(querystring)[0]
        # m = db.get_modul_by_id(my_connect, m_id)[0] # gesamte Modul-Infos
        modul_namen.append(modul[1])
        modul_credits.append(modul[2])

        p_erreicht_list.append(i[3])
        p_gesamt_list.append(i[2])
        note = notenberechnung(i[3], i[2])
        note_list.append(note)
        bestanden_list.append(note <= 4.0)

    # raw_pruefung_data =
    # [modul_namen, modul_credits, p_gesamt_list, p_erreicht_list, note_list, bestanden_list, modul_ids]
    raw_pruefung_data = []
    # raw_pruefung_data.append(veranstaltung_ids)
    raw_pruefung_data.append(modul_namen)
    raw_pruefung_data.append(modul_credits)
    raw_pruefung_data.append(p_gesamt_list)
    raw_pruefung_data.append(p_erreicht_list)
    raw_pruefung_data.append(note_list)
    raw_pruefung_data.append(bestanden_list)
    raw_pruefung_data.append(modul_ids)

    #pruefungen_result = []
    #for i in range(len(raw_pruefung_data[0])):
    #    pruefungen_result.append([row[i] for row in raw_pruefung_data])

    return raw_pruefung_data


def get_raw_modul_data (student_id):
    """
    Error einfügen wenn Prüfungen doppelt sind?
    :param student_id:
    :return:
    """
    pruefungen_raw = get_raw_pruefung_data(student_id)
    m_ids = [*set(pruefungen_raw[6])]
    m_namen = [*set(pruefungen_raw[0])]
    m_credits = [] # [*set(get_raw_pruefung_data(student_id)[1])]
    m_note = []
    note_dict = {}# {m : 'pass' for m in m_ids}
    p_ids = [] # noch berechnen!
    pruefungen_result = []
    for i in range(len(pruefungen_raw[0])):
        pruefungen_result.append([row[i] for row in pruefungen_raw])
    # print(pruefungen_result)

    for modul in m_ids:
        p_e = 0.0
        p_g = 0.0
        for p in pruefungen_result:
            if p[6] == modul: # and p[0] not in p_ids:
                p_g += p[2]
                p_e += p[3]
                # p_ids.append(p[0])
        note_dict[modul] = notenberechnung(p_e, p_g)

    # noch durcheinander
    # module_raw = [m_ids, m_namen, m_credits, m_note]
    module_raw = []
    module_raw.append(m_ids)
    m_namen = []
    m_bestanden = []
    for m in m_ids:
        querystring = be.url + f"/getModul/{m}"
        modul = be.get_values(querystring)[0]
        m_namen.append(modul[1])
        m_credits.append(modul[2])
        note = note_dict.get(m)
        m_note.append(note)
        m_bestanden.append(note <= 4.0)
    module_raw.append(m_namen)
    module_raw.append(m_credits)
    module_raw.append(m_note)
    module_raw.append(m_bestanden)

    return module_raw


def print_student_module(student_id):
    """
    Redundante Methode. get_raw_modul_data() gibt das gleiche aus (andersrum tabelliert)
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


def get_gpa_and_credits_student(student_id):
    """ Methode zum Erhalt des Durchschnitts und der erreichten Credits eines Studenten

    Args: student_id: ID des angeforderten Studenten
    Returns: list: Liste in Form von [gpa, credits_erreicht] für den konkreten Studenten

    Test:
         1) student_id eines vorhandenen Studenten eingeben
            -> erwartetes Ergebnis:
                 * Liste: [gpa, credits_erreicht]
         2) student_id eines nicht vorhandenen Studenten eingeben
             -> erwartetes Ergebnis:
                 * Exception: Mitteilung, dass Datenbankverbindung nicht funktioniert hat bzw. das angeforderte Objekt
                 nicht existiert.
        3) Test mit laufender bzw. nicht laufender API, bei nicht laufender, soll Exception ausgelöst werden.
    """
    modul_data = get_raw_modul_data(student_id)
    gewichtete_noten_sum = 0.0
    ects_reached = 0.0
    credits = modul_data[2]
    note = modul_data[3]
    # bestanden = get_raw_modul_data(student_id)[5]
    for i in range(len(credits)):
        if note[i] <= 4.0:
            gewichtete_noten_sum += credits[i] * note[i]
            ects_reached += credits[i]

    gpa = gewichtete_noten_sum/ects_reached
    # truncate
    gpa = int(gpa*10)
    gpa /= 10
    return [gpa, ects_reached]


# def get_modul_id_namen_student(student_id):
#     """
#     obsolete Funktion
#     :param student_id:
#     :return:
#     """
#     modul_ids = [*set(get_raw_pruefung_data(student_id)[6])]
#     # modul_namen = [*set(get_raw_modul_data(student_id)[0])]
#     # module_raw = [modul_ids, modul_namen]
#     # module_result = []
#     # for i in range(len(module_raw[0])):
#     #     module_result.append([row[i] for row in module_raw])
#     return modul_ids


# def internal_pruefungen_in_modul(student_id, modul_id):
#     # pruefungen = db.get_all_pruefungsleistung_by_student(my_connect, student_id)
#     querystring = be.url + f"/getPruefungsleistungenByStudent/{student_id}"
#     pruefungen = be.get_values(querystring)
#     result = []
#     for p in pruefungen:
#         querystring = be.url + f"/getVeranstaltung/{p[1]}"
#         veranstaltung = be.get_values(querystring)
#         if veranstaltung[3] == modul_id:
#             result.append(p)
#     return result


# def print_pruefungen_in_modul (student_id: int, modul_id: int) -> list[list]:
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
#         querystring = be.url + f"/getVeranstaltung/{p[1]}"
#         veranstaltung = be.get_values(querystring)
#         details.append(veranstaltung[1]) # Veranstaltungsname
#         details.append(p[2]) # gesamte Punkte
#         details.append(p[3]) # erreichte Punkte
#         details.append(notenberechnung(p[3], p[2]))
#         result.append(details)
#     return result


# database elements
# my_connect = app.my_connect
# DATABASE_FILE = "data.db"
# my_connect = db.create_database_connection(DATABASE_FILE)
# my_cursor = my_connect.cursor()


if __name__ == '__main__':
    print(get_raw_modul_data(1000))
    print(print_student_module(1000))
   # print("_______________TEST START:________________")
   # print(print_student_module(2000))
   # print(' ')
   # print(print_pruefungen_in_modul(1000, 1200))
   # print(internal_pruefungen_in_modul(1000, 1200))
   # print(get_gpa_by_student(2000))
#
   # print(get_student_name(2000))
   # # print(notenberechnung(99,100))
   # print(db.get_modul_by_id(my_connect, 9980))
   # print(db.get_all_pruefungsleistung_by_student(my_connect, 1000))
   # print(get_raw_pruefung_data(2000))
   # print(get_raw_modul_data(2000))
   # print("relevante Zeile")
   # print(print_student_module(2000))
   # print(get_credits_erreicht(2000))
#
   # print("\n bis hier funktioniert alles\n")
   # print(db.get_student_by_id(my_connect, 2000))
   # print(app.abmeldung())
   # test = app.getPruefungsleistungenByStudent(2000)
   # # print(db.get_all_pruefungsleistung_by_student(my_connect, 1000))
   # # print(get_credits_erreicht(1000))
   # print (test)
   # print("_______________TEST ENDE:________________")
    