"""Modul für Frontend

author: Daniela Mayer
date: 27.10.2022
version: 1.0.0
licence: free
"""

import PySimpleGUI as sg

def LoginSeite():
    """Implimentierung der Login Seite

    Tests:
        *
        *
    """
    
    layout = [[sg.Text('Login', font=('any', 12, 'bold'))],
          [sg.Text('Username:'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort:'), sg.InputText(key='-passwort-', do_not_clear=False)],
          [sg.Button('Anmelden')]]

    Login_window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= Login_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            AnmeldeDaten= values['-name-'], values['-passwort-']

    Login_window.close()



def FalseLoginSeite():
    """Implimentierung der Seite nach falschem einloggen

    Tests:
        *
        *
    """
    
    layout = [[sg.Text('Login', font=('any', 12, 'bold'))],
        [sg.Text('Username oder Passwort falsch', text_color= 'red')],
        [sg.Text('Username:'), sg.InputText(key='-name-', do_not_clear=False)],
        [sg.Text('Passwort:'), sg.InputText(key='-passwort-', do_not_clear=False)],
        [sg.Button('Anmelden')],
        [sg.Text('Falls Sie das Passwort vergessen haben, wenden Sie sich an den Administrator!')]]

    FalseLogin_window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= FalseLogin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
             AnmeldeDaten= values['-name-'], values['-passwort-']

    FalseLogin_window.close()



def ErfolgreicherLogout():
    """Seite nach dem Logout

    Tests:
        *
        *
    """

    layout = [[sg.Text('Sie haben sich erfolgreich abgemeldet!')]]

    Logout_window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= Logout_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            break

    Logout_window.close()



def StudierendenAnsichtAllgemein():
    """Seite für Studierende für die Einsicht der Modulnoten, sowie GPA 

    Tests:
        *
        *
    """
    modul_information_array=[
        ['Programmierung', 1, 5.0, 120, 100, 1.6, True],
        ['Mathe 1', 1, 5.0, 120, 75, 2.5, True]]

    headings=['Modul', 'Versuch', 'Cedits', 'P. g.', 'P. e.', 'Note', 'best.']
    
    layout = [[sg.Text('Herzlich Willkommen!'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Leistungsübersicht', font=('any', 12, 'bold'))],
          [sg.Table(values=modul_information_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)],
          [sg.Text('Gesamt', font=('any', 12, 'bold')), sg.Text('Cedits gesamt'), sg.Text('GPA')]]
          
    Studi_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Studi_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            PasswortAendernSeite
        elif event == "Abmelden":
            Studi_window.close()
            ErfolgreicherLogout
        elif event== "-Table-":
            Studi_window.close()
            print(values['-Table-'][0])
            selected_row_index= values['-Table-'][0]
            Modul_information= modul_information_array[selected_row_index]
            StudierendenAnsichtModul(Modul_information)

    Studi_window.close()



def StudierendenAnsichtModul(Modul_info, Nutzer: str):
    """ Informationen über Veranstaltungen eines Moduls mit Noten und Punkten

    Args:
        Modul_info (_type_): _description_
        Nutzer (str): _description_

    Test:
        *
        *
    """

    Modul_name= Modul_info[0]
    Modul_pg= str(Modul_info[3])
    Modul_pe= str(Modul_info[4])
    Modul_Note= str(Modul_info[5])
    Modulinhalt=[['Java', 1, 5.0, 60, 45, 2.6, True],
    ['Python', 1, 5.0, 60, 55, 1.8, True]]

    headings=['Veranstaltung', 'Versuch', 'Cedits', 'P. g.', 'P. e.', 'Note', 'best.']

    layout = [[sg.Text(Modul_name)],
            [sg.Table(values=Modulinhalt, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)],
            [sg.Text(Modul_name +": P. g. " + Modul_pg + ", P.e. " + Modul_pe + ", Note " + Modul_Note)],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    window=sg.Window('Studierendenverwaltungssystem', layout)
    
    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            if Nutzer== "Studi":
                window.close()
                StudierendenAnsichtAllgemein()
    
    window.close()



def PasswortAendernSeite():
    """Seite zum ändern des Passwortes

    Tests:
        *
        *
    """

    layout = [[sg.Text('Passwort ändern', font=('any', 12, 'bold'))],
          [sg.Text('Username *'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort *'), sg.InputText(key='-passwort-', do_not_clear=False)],
          [sg.Text('neues Passwort *'), sg.InputText(key='-neuesPasswort-', do_not_clear=False)],
          [sg.Text('Psswort wiederholen *'), sg.InputText(key='-wiPasswort-', do_not_clear=False)],
          [sg.Button('Ändern')]]

    Passwort_window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= Passwort_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Ändern":
            ÄnderungsDaten= values['-name-'], values['-passwort-'], values['-neuesPasswort-'], values['-wiPasswort-']
            Passwort_window.close()

    Passwort_window.close()


def VeranstaltungsnotenEintragenDoz():
    """Dozenten können hier die Noten ihrer Studierenden eintragen

    Tests:
    *
    *
    """
    
    Anzahl_Versuche= ('1', '2') 
    Bestanden= (True, False)
    Prüfungsinfo_Veranstaltung_Array= []

    layout = [[sg.Text('Herzlich Willkommen'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Veranstaltungsnoten eintragen', font=('any', 12, 'bold'))],
          [sg.Text('Veranstaltungs Id:'), sg.InputText(key= '-Veran_id-', do_not_clear=True)],
          [sg.Text('Matrikelnummer:'), sg.InputText(key='-Matrikelnummer-', do_not_clear=False)],
          [sg.Text('Versuch:'), sg.Combo(Anzahl_Versuche, enable_events=True, key='-Versuch-')],
          [sg.Text('Punkte gesamt'), sg.InputText(key= '-Punkte_gesamt-', do_not_clear=True), sg.Text('Punkte erreicht'), sg.InputText(key= '-Punkte_erreicht-', do_not_clear=False)], 
          [sg.Text('Note'), sg.InputText(key= '-Note-', do_not_clear=False)],
          [sg.Text('Bestanden'), sg.Combo(Bestanden, enable_events=True, key='-Bestanden-')],
          [sg.Button('OK')]]
          
    VeranNoten_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= VeranNoten_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            PasswortAendernSeite
        elif event == "Abmelden":
            VeranNoten_window.close()
            ErfolgreicherLogout
        elif event == "OK":
            Prüfungsinfo_Veranstaltung= values['-Veran_id-'], values['-Matrikelnummer-'], values['-Versuch-'], 
            values['-Punkte_gesamt-'], values['-Punkte_erreicht-'], values['-Note-'], values['-Bestanden-']
            Prüfungsinfo_Veranstaltung_Array.append(Prüfungsinfo_Veranstaltung)

    VeranNoten_window.close()



def AdministationAllgemein():
    """Erste Seite des Administrators
    * sollen Studierende, Dozierende, Studiengangsleitung, Veranstaltungen oder Module bearbeitet, neu angelet oder gelöscht werden

    Tests:
    *
    * 
    """

    layout = [[sg.Text('Administration'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Was möchten Sie bearbeiten/ anlegen oder löschen?')],
          [sg.Button('Studierende', font=('any', 9, 'underline')), sg.Button('Dozierende', font=('any', 9, 'underline')), sg.Button('Studiengangsleitung', font=('any', 9, 'underline'))],
          [sg.Button('Veranstaltung', font=('any', 9, 'underline')), sg.Button('Modul', font=('any', 9, 'underline'))]]
          
    Admin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            PasswortAendernSeite
        elif event == "Abmelden":
            Admin_window.close()
            ErfolgreicherLogout
        elif event == 'Studierende':
            break
        elif event == 'Dozierende':
            break
        elif event == 'Studiengangsleitung':
            break
        elif event == 'Veranstaltung':
            break
        elif event == 'Modul':
            break

    Admin_window.close()


