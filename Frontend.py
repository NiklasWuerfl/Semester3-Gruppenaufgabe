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
            ErfolgreicherLogout
            Studi_window.close()
        elif event== "-Table-":
            print(values['-Table-'][0])
            selected_row_index= values['-Table-'][0]
            Modul_information= modul_information_array[selected_row_index]
            StudierendenAnsichtModul(Modul_information)

    Studi_window.close()



def StudierendenAnsichtModul(Modul_info):
    """einzel Noten der Veranstaltungen eines Moduls und gesamt Noten werden angezeigt

    Args:
        Modul_info (Array): Informationen über Modul

    Tests:
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

    layout = [[sg.Text(Modul_name, font=('any', 12, 'bold'))],
            [sg.Table(values=Modulinhalt, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)],
            [sg.Text(Modul_name +": P. g. " + Modul_pg + ", P.e. " + Modul_pe + ", Note " + Modul_Note)]
          ]
          
    Modul_window=sg.Window('Studierendenverwaltungssystem', layout)
    
    while True:
        event, values= Modul_window.read()
        if event == sg.WIN_CLOSED:
            break
    
    Modul_window.close()



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


