"""test api-aufruf"""

import requests as r
import json

def get_student_name(student_id: int) -> list:
    """
    Methode zum Erhalt des Namens des Students

    :param student_id:
    :return: name: String in Form: "Nachname, Vorname"

    Tests:
    * ungültige Student_id eingeben
    *
    """

    url = "http://localhost:5000"

    querystring = url + f"/getPruefungsleistungenByStudent/{student_id}"

    response = r.get(querystring) #.content.decode('UTF-8')
    student_values = response.json()
    # student_values = list(response)
    print(response)
    print(student_values)
    # student_values = response.replace("[","").replace("\n","").replace("]","").replace(" ","").split(",")
    # student_values[0] = int(student_values[0])
    # student_values[1] = student_values[1].replace('"',"")
    # student_values[2] = student_values[2].replace('"',"")
    # student_values[3] = int(student_values[3])
    # student_values[4] = student_values[4].replace('"',"")
    # student_values[5] = student_values[5].replace('"',"")

    return student_values