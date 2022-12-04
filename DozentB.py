"""
Modul um die nötigen Informationen für die Dozenten-Startseite zu erhalten und zu geben
noch mit Modul "DATABASE" implementiert
    author: Emanuel Forderer
    date: 11.11.2022
    version: 1.1.1
    licence: free (open source)
"""
import app
import database as db
import requests as r
import Backend

url = "http://localhost:5000"

# querystring = url + f"/getPruefungsleistungenByStudent/{student_id}"


def getValues (querystring):
    response = r.get(querystring) #.content.decode('UTF-8')
    if (response.status_code == 200):
        return response.json()
    else:
        raise Exception(f"Es ist ein Fehler beim Zugriff auf die API aufgetreten oder es besteht kein Objekt mit der "
                        f"angefragten ID.\n\tError Code: {response.status_code}")


def get_dozent_name(dozent_id):
    """
    Methode zum Erhalt des Namens des Students
    :param student_id:
    :return: name: String in Form: "Nachname, Vorname"
    Tests:
    * ungültige Student_id eingeben
    *
    """
    vorname = db.get_dozent_by_id(my_connect, dozent_id)[0][1]
    nachname = db.get_dozent_by_id(my_connect, dozent_id)[0][2]
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


def set_pruefung_data(pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung):
    pruefungen = Backend.edit_pruefungsleistung_by_student_and_veranstaltung(pruefungsleistung_student, pruefungsleistung_veranstaltung, pruefungsleistung)
    veranstaltung_ids = []
    modul_ids = []
    veranstaltung_namen =[]
    modul_namen = []
    modul_credits = []
    modul_noten = []  
    p_gesamt_list =[]
    p_erreicht_list = []
    note_list = []
    
    for i in pruefungen:
        
        v_id = i[1]
        veranstaltung_ids.append(v_id)
        veranstaltung_namen.append(db.get_veranstaltung_by_id(my_connect, v_id)[1])
        m_id = db.get_veranstaltung_by_id(my_connect, i[1])[3]
        modul_ids.append(m_id)
        m = db.get_modul_by_id(my_connect, m_id)[0] 
        modul_namen.append(m[1])
        modul_credits.append(m[2])

        p_erreicht_list.append(i[3])
        p_gesamt_list.append(i[2])
        note = notenberechnung(i[3], i[2])
        note_list.append(note)

    
    
        pruefung_data = []
        pruefung_data.append(modul_namen)
        pruefung_data.append(modul_credits)
        pruefung_data.append(p_gesamt_list)
        pruefung_data.append(p_erreicht_list)
        pruefung_data.append(note_list)
        pruefung_data.append(modul_ids)

    return pruefung_data


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
        
        feature = []
        veranstaltung = db.get_veranstaltung_by_id(my_connect, p[1])
        feature.append(veranstaltung[1]) 
        feature.append(p[2]) 
        feature.append(p[3]) 
        feature.append(notenberechnung(p[3], p[2]))
        result.append(feature)
    
    return result


def best_note(veranstaltung_id):
    """"" 
    Methode, um die beste Note zu ermitteln
    :param student_id:
    :return: bNote
    """

    querystring = url + f"/get_all_pruefungsleistung_by_veranstaltung/{veranstaltung_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    pruefungsleistungen = data_raw
    result = []
    bNote = []
    bestNote = 0
    
    for p in pruefungsleistungen:
        
        if result[p] > result[bestNote]:
        
            bestNote = p
            bNote.append(bestNote)

        return bNote


def worst_note(veranstaltung_id):
    """"" 
    Methode, um die schlechteste Note zu ermitteln
    :param student_id
    :return: wNote
    """

    querystring = url + f"/get_all_pruefungsleistung_by_veranstaltung/{veranstaltung_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    pruefungsleistungen = data_raw
    result = []
    wNote = []
    worstNote = 0
    
    for p in pruefungsleistungen:
        
        if result[p] < result[worstNote]:
        
            worstNote = p
            wNote.append(worstNote)

        return wNote


def get_mean(veranstaltung_id):
    """"" 
    Methode, um den Mittelwert zu ermitteln
    :param student_id
    :return: mean_list
    """

    querystring = url + f"/get_all_pruefungsleistung_by_veranstaltung/{veranstaltung_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    pruefungsleistungen = data_raw
    result = []
    mean_list = []
    mean = 0
    
    for p in pruefungsleistungen:
        
        sum = result[p] + sum
        mean = sum / p

        mean_list.append(mean)

        return mean_list


def get_median(veranstaltung_id):
    """"" 
    Methode, um den Median zu ermitteln
    :param student_id
    :return: mean_list
    """

    querystring = url + f"/get_all_pruefungsleistung_by_veranstaltung/{veranstaltung_id}"
    data_raw = getValues(querystring)
    if type(data_raw) is Exception:
        raise Exception(data_raw)
    pruefungsleistungen = data_raw
    data = sorted(pruefungsleistungen)
    index = len(data) // 2
    
    # If the dataset is odd  
    if len(pruefungsleistungen) % 2 != 0:
        return data[index]
    
    # If the dataset is even
    return (data[index - 1] + data[index]) / 2



# database elements
my_connect = app.my_connect
# DATABASE_FILE = "data.db"
# my_connect = db.create_database_connection(DATABASE_FILE)
# my_cursor = my_connect.cursor()


#if __name__ == '__main__':
    #print("_______________TEST START:________________")
    #set_raw_pruefung_data(2000, 3000)
    #print(set_raw_pruefung_data)
    #print(print_pruefungen_in_modul(1000, 1200))
    #print(' ')
    #print(internal_pruefungen_in_modul(1000, 1200))

    #print(get_dozent_name(2000))
    #(notenberechnung(99,100))
    #print(db.get_modul_by_id(my_connect, 9980))
    #print(db.get_all_pruefungsleistung_by_student(my_connect, 1000))
    #print(get_pruefung_data(2000))
    #print(best_note(1200))
    #print("test")
    #print(worst_note(1200))
    #print(get_mean(1200))
    #print(get_median(1200))

    #print("\n funktioniert\n")
    #print(db.get_dozent_by_id(my_connect, 2000))
    #print(app.abmeldung())
    #test = app.getPruefungsleistungenByStudent(2000)
   # print (test)
    #print("_______________TEST ENDE:________________")

