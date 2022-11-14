"""
Modul um die nötigen Informationen für die Studenten-Startseite zu erhalten
noch mit Modul "DATABASE" implementiert

    author: Niklas Würfl
    date: 07.11.2022
    version: 1.1.1
    licence: free (open source)
"""
import database as db
import app
import app_extra as extra


def get_student_name(student_id):
    """
    Methode zum Erhalt des Namens des Students

    :param student_id:
    :return: name: String in Form: "Nachname, Vorname"

    Tests:
    * ungültige Student_id eingeben
    *
    """
    vorname = extra.getStudent(student_id)[0][1]
    nachname = extra.getStudent(student_id)[0][2]
    name = nachname + ", " + vorname
    return name


def notenberechnung(p_erreicht, p_gesamt):
    """

    :param p_erreicht:
    :param p_gesamt:
    :return:
    """
    note = 1 + 3 * ((p_gesamt-p_erreicht)/(p_gesamt/2))
    note = int(note*10)
    note /= 10
    return note


def get_raw_pruefung_data(student_id):
    pruefungen = db.get_all_pruefungsleistung_by_student(my_connect, student_id)
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
        veranstaltung_namen.append(db.get_veranstaltung_by_id(my_connect, v_id)[1])
        m_id = db.get_veranstaltung_by_id(my_connect, i[1])[3]
        modul_ids.append(m_id)
        m = db.get_modul_by_id(my_connect, m_id)[0] # gesamte Modul-Infos
        modul_namen.append(m[1])
        modul_credits.append(m[2])

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
    m_ids = [*set(get_raw_pruefung_data(student_id)[6])]
    m_namen = [*set(get_raw_pruefung_data(student_id)[0])]
    m_credits = [] # [*set(get_raw_pruefung_data(student_id)[1])]
    m_note = []
    note_dict = {}# {m : 'pass' for m in m_ids}
    p_ids = [] # noch berechnen!
    raw_pruefung_data = get_raw_pruefung_data(student_id)
    pruefungen_result = []
    for i in range(len(raw_pruefung_data[0])):
        pruefungen_result.append([row[i] for row in raw_pruefung_data])
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
        modul = db.get_modul_by_id(my_connect, m)[0]
        m_namen.append(modul[1])
        m_credits.append(modul[2])
        m_note.append(note_dict.get(m))
        m_bestanden.append(note_dict.get(m)<=4.0)
    module_raw.append(m_namen)
    module_raw.append(m_credits)
    module_raw.append(m_note)
    module_raw.append(m_bestanden)

    return module_raw


def print_student_module(student_id):
    """
    Redundante Methode. get_raw_modul_data() gibt das gleiche aus (andersrum tabelliert)
    Methode zum Erlangen des Dataframes mit allen relevanten Modulen und Noten für die Tabelle in der Startseite

    Return:
    [modul_id, modul_name, credits, note, bestanden]
    [[1200, 'Mathematik II', 8, 3.3], [9980, 'Finanz- und Rechnungslehre', 5, 3.8], [3000, 'IT Konzepte', 5, 3.4]]

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
    ects_list = get_raw_modul_data(student_id)[2]
    noten = get_raw_modul_data(student_id)[3] # evtl. vereinfachbar in ein Array
    credits_erreicht = 0

    for i in range(len(noten)):
        if noten[i] <= 4.0:
            credits_erreicht += ects_list[i]

    # kurs_id = db.get_student_by_id(my_connect, student_id)[3]

    # punkte_erreicht = 0
    # for pruefung in db.get_all_pruefungsleistung_by_student(my_connect, student_id):
    #     punkte_erreicht += pruefung[1]
    # credits_list = db.get_modul_by_id()[2]

    return credits_erreicht


def get_gpa_by_student(student_id):
    gewichtete_noten_sum = 0.0
    ects_reached = 0.0
    credits = get_raw_modul_data(student_id)[2]
    note = get_raw_modul_data(student_id)[3]
    # bestanden = get_raw_modul_data(student_id)[5]
    for i in range(len(credits)):
        if note[i] <= 4.0:
            gewichtete_noten_sum += credits[i] * note[i]
            ects_reached += credits[i]
    # alle_noten = db.get_all_modules(my_connect, student_id)
    # ects_reached = get_credits_erreicht(my_connect, student_id)
    # print(alle_noten)
    # print(ects_reached)
    # print (list(alle_noten.values()))

    gpa = gewichtete_noten_sum/ects_reached
    # truncate
    gpa = int(gpa*10)
    gpa /= 10
    return gpa


def get_modul_id_namen_student(student_id):
    """
    obsolete Funktion
    :param student_id:
    :return:
    """
    modul_ids = [*set(get_raw_pruefung_data(student_id)[6])]
    # modul_namen = [*set(get_raw_modul_data(student_id)[0])]
    # module_raw = [modul_ids, modul_namen]
    # module_result = []
    # for i in range(len(module_raw[0])):
    #     module_result.append([row[i] for row in module_raw])
    return modul_ids


def internal_pruefungen_in_modul(student_id, modul_id):
    pruefungen = db.get_all_pruefungsleistung_by_student(my_connect, student_id)
    result = []
    for p in pruefungen:
        if db.get_veranstaltung_by_id(my_connect, p[1])[3] == modul_id:
            result.append(p)
    return result


def print_pruefungen_in_modul (student_id, modul_id):
    pruefungen = internal_pruefungen_in_modul(student_id, modul_id)
    result = []
    for p in pruefungen:
        details = []
        veranstaltung = db.get_veranstaltung_by_id(my_connect, p[1])
        details.append(p[1])
        details.append(veranstaltung[1]) # Veranstaltungsname
        details.append(p[2]) # gesamte Punkte
        details.append(p[3]) # erreichte Punkte
        details.append(notenberechnung(p[3], p[2]))
        result.append(details)
    return result


# database elements
my_connect = db.create_database_connection("data.db")
# DATABASE_FILE = "data.db"
# my_connect = db.create_database_connection(DATABASE_FILE)
# my_cursor = my_connect.cursor()
# url = "http://localhost:5000"

# in Frontend einfügen:
#     link = url + f"/ModuleStudent/{student_id}"
#     response = requests.get(link)
#     modul_information_array = response.json()
# if __name__ == '__main__':
  #   print(extra.getPruefungsleistungenByStudent(2000))
#   print("_______________TEST START:________________")
#     print(print_student_module(2000))
#     print(' ')
#   print(print_pruefungen_in_modul(1000, 1200))
#   print(internal_pruefungen_in_modul(1000, 1200))
#   print(get_gpa_by_student(2000))
#
#   print(get_student_name(2000))
#   # print(notenberechnung(99,100))
#   print(db.get_modul_by_id(my_connect, 9980))
#   print(db.get_all_pruefungsleistung_by_student(my_connect, 1000))
#   print(get_raw_pruefung_data(2000))
#   print(get_raw_modul_data(2000))
#   print("relevante Zeile")
#   print(print_student_module(2000))
#   print(get_credits_erreicht(2000))

#   print("\n bis hier funktioniert alles\n")
#   print(db.get_student_by_id(my_connect, 2000))
#   print(app.abmeldung())
#   test = app.getPruefungsleistungenByStudent(2000)
    # print(db.get_all_pruefungsleistung_by_student(my_connect, 1000))
    # print(get_credits_erreicht(1000))
#   print (test)
#   print("_______________TEST ENDE:________________")
