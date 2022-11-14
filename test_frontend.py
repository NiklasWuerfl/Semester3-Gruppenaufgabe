"""Modul für Frontend

author: Emma MÜller
date: 11.11.2022
version: 1.0.0
licence: free
"""

import PySimpleGUI as sg
import test_backend as tb

def start():
    """test-seite"""
    
    layout = [[sg.Button('Anmelden')]]

    Login_window=sg.Window('Studierendenverwaltungssystem', layout)

    while True:
        event, values= Login_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            StudierendenAnsichtAllgemein(tb.get_student_name(1000))

    Login_window.close()

def StudierendenAnsichtAllgemein(modul_information_array: list):
    """Seite für Studierende für die Einsicht der Modulnoten, sowie GPA 
    """

    headings=['Student_id','Vorname','Nachname','Kurs_id','Nutzername','Passwort']
    
    layout = [[sg.Text('Herzlich Willkommen!'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Informationsübersicht', font=('any', 12, 'bold'))],
          [sg.Table(values=modul_information_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='left',
                    num_rows=6,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)],
          [sg.Text('Gesamt', font=('any', 12, 'bold')), sg.Text('Cedits gesamt'), sg.Text('GPA')]]
          
    Studi_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event = Studi_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            start()
        elif event == "Abmelden":
            Studi_window.close()
            start()
        elif event== "-Table-":
            start()

    Studi_window.close()

if __name__ == '__main__':
    start()
