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

    window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            AnmeldeDaten= values['-name-'], values['-passwort-']

    window.close()



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

    window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
             AnmeldeDaten= values['-name-'], values['-passwort-']

    window.close()



def ErfolgreicherLogout():
    """Seite nach dem Logout

        Tests:
        *
        *
    """

    layout = [[sg.Text('Sie haben sich erfolgreich abgemeldet!')]]

    window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            break

    window.close()



def StudierendenAnsichtAllgemein():
    """Seite für Studierende für die Einsicht der Modulnoten, sowie GPA 

        Tests:
        *
        *
    """
    information_array=[
    ['Programmierung', 1, 5.0, 120, 100, 1.6, True],
    ['Mathe 1', 1, 5.0, 120, 75, 2.5, True]]

    headings=['Modul', 'Versuch', 'Cedits', 'P. g.', 'P. e.', 'Note', 'best.']
    
    layout = [[sg.Text('Herzlich Willkommen!'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Leistungsübersicht', font=('any', 12, 'bold'))],
          [sg.Table(values=information_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35)],
          [sg.Text('Gesamt', font=('any', 12, 'bold')), sg.Text('Cedits gesamt'), sg.Text('GPA')]]
          
    window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            break
        elif event == "Abmelden":
            break

    window.close()


