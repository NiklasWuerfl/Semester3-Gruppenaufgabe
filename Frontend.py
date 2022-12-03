"""Modul für Frontend

author: Daniela Mayer
date: 02.12.2022
version: 3.0.0
licence: free
"""

import PySimpleGUI as sg
import Backend as be

def login():
    """Implimentierung der Login Seite

    Tests:
        * richtige Logindaten als Dozierender/ Studierender/ Admin eintragen
        * falsche Logindaten eingeben
    """
    sg.theme('TanBlue')

    nutzer = ('Studierender', 'Dozierender', 'Admin')

    login_column = [[sg.Text('Login', font=('any', 12, 'bold'))],
                    [sg.Combo(nutzer, enable_events=True, key='-nutzer-')],
                    [sg.Text('ID: *'), 
                     sg.InputText(key='-id-', do_not_clear=False)],
                    [sg.Text('Passwort: * '), 
                     sg.InputText(key='-passwort-', do_not_clear=False)],
                    [sg.Button('Anmelden', font=('any', 9, 'underline'))]
                     ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0), key='-2-'),              
               sg.Column(login_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]

    login_window = sg.Window('Studierendenverwaltungssystem',
                             layout, size=(500, 500), finalize=True
                             )
    login_window['-C-'].expand(True, True, True)
    login_window['-1-'].expand(True, True, True)
    login_window['-2-'].expand(True, False, True)

    while True:
        event, values= login_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            login_window.close() 
            if values['-nutzer-'] == 'Studierender':
                if be.login_student(values['-id-'], values['-passwort-']) == True:
                   studierende_allgemein(values['-id-'])
                else:
                    sg.popup("Falsche Nutzer-ID oder Passwort")
            elif values['-nutzer-'] == 'Dozierender':
                if be.login_dozent(values['-id-'], values['-passwort-']) == True:
                   dozierende_veranstaltung(values['-id-'])
                else:
                    sg.popup("Falsche Nutzer-ID oder Passwort")
            elif values['-nutzer-'] == 'Admin':
                if be.login_admin(values['-id-'], values['-passwort-']) == True:
                    administration_allgemein()
                else:
                    sg.popup("Falsche Nutzer-ID oder Passwort")
            
    login_window.close()


def erfolgreicher_logout():
    """Seite nach dem Logout

    Tests:
        * Button 'neu Anmelden' drücken
        * Fenster schließen
    """

    sg.theme('TanBlue')

    logout_column = [[sg.Text('Sie haben sich erfolgreich abgemeldet!', font=('any', 15))],
                    [sg.Text('   ')],
                    [sg.Button('neu Anmelden', font=('any', 9, 'underline'))]
                    ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(logout_column, vertical_alignment='center', 
                         justification='right',  k='-C-')]
                         ]

    logout_window = sg.Window('Studierendenverwaltungssystem',
                              layout, size=(500, 500), finalize=True
                              )
    logout_window['-C-'].expand(True, True, True)
    logout_window['-1-'].expand(True, True, True)
    logout_window['-2-'].expand(True, False, True)

    while True:
        event, values = logout_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "neu Anmelden":
            logout_window.close()
            login()

    logout_window.close()


def studierende_allgemein(studi_id: int):
    """Seite für Studierende für die Einsicht der Modulnoten, sowie GPA 

    Args:
        studi_id (int): ID des angemeldeten Studierenden als Interger

    Tests:
        * Zeile in Tabelle anklicken
        * auf 'Passwort ändern' und 'Abmelden'-Button klicken
    """

    sg.theme('TanBlue')

    modul_information_array = be.get_student_module(studi_id)

    headings = ['Modul ID','Modul', 'Cedits', 'Note', 'best.']

    buttons = [[sg.Button('Passwort ändern', font=('any', 9, 'underline')),
                sg.Button('Abmelden', font=('any', 9, 'underline'))]
                ]
    
    layout = [[sg.Text('Herzlich Willkommen!'), 
               sg.Column(buttons, element_justification='right', expand_x=True)],
              [sg.HorizontalSeparator()],
              [sg.Text('Leistungsübersicht', font=('any', 12, 'bold'))],
              [sg.Table(values=modul_information_array, headings=headings, max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='left',
                        num_rows= 10,
                        key= '-table-',
                        row_height=35,
                        enable_events= True)],
              [sg.Text('Gesamt', font=('any', 12, 'bold')), 
               sg.Text('Cedits gesamt' + be.get_credits_erreicht(studi_id)), 
               sg.Text('GPA' + be.get_gpa_by_student(studi_id))]
               ]
          
    studi_window = sg.Window('Studierendenverwaltungssystem',
                             layout, modal=True, size=(500, 500)
                             )

    while True:
        event, values = studi_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            passwort_aendern()
        elif event == "Abmelden":
            studi_window.close()
            erfolgreicher_logout()
        elif event == "-table-":
            selected_row_index = values['-table-'][0]
            modul_information = modul_information_array[selected_row_index]
            studierende_modul(studi_id, modul_information)

    studi_window.close()


def studierende_modul(studi_id: int, modul_info):
    """ Informationen über Veranstaltungen eines Moduls mit Noten und Punkten

    Args:
        studi_id (int): ID des angemeldeten Studierenden als Integer
        modul_info (array): alle Informationen über das Modul in einem Array

    Test:
        * 'zurück'-Button klicken
        *
    """

    sg.theme('TanBlue')

    modul_name = modul_info[1]
    modul_Note = str(modul_info[3])
    modulinhalt = be.print_pruefungen_in_modul(studi_id, modul_info[0])

    headings = ['Veranstalungs ID','Veranstaltung', 'P. g.', 'P. e.', 'Note']

    layout = [[sg.Text(modul_name)],
              [sg.Table(values=modulinhalt, headings=headings, max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='left',
                        num_rows= 5,
                        key= '-table-',
                        row_height=35,
                        enable_events= True)],
              [sg.Text("Note " + modul_Note)],
              [sg.Button('zurück', font=('any', 9, 'underline'))]
              ]
          
    studi_modul_window = sg.Window('Studierendenverwaltungssystem',
                                   layout, modal=True, size=(500, 500)
                                   )
    
    while True:
        event, values = studi_modul_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            break
    
    studi_modul_window.close()


def passwort_aendern():
    """Seite zum ändern des Passwortes

    Tests:
        * Daten korrekt eingeben
        * Daten nicht korrekt eingeben
    """

    sg.theme('TanBlue')

    layout = [[sg.Text('Passwort ändern', font=('any', 12, 'bold'))],
              [sg.Text('Username *'),
               sg.InputText(key='-name-', do_not_clear=False)],
              [sg.Text('Passwort *'),
               sg.InputText(key='-passwort-', do_not_clear=False)],
              [sg.Text('neues Passwort *'),
               sg.InputText(key='-neuesPasswort-', do_not_clear=False)],
              [sg.Text('Passwort wiederholen *'), 
               sg.InputText(key='-wiPasswort-', do_not_clear=False)],
              [sg.Button('Ändern')]
               ]

    passwort_window = sg.Window('Studierendenverwaltungssystem',
                                layout, modal=True, size=(500, 500)
                                )
    
    while True:
        event, values = passwort_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Ändern":
            aenderungs_daten= values['-name-'], values['-passwort-'],
            values['-neuesPasswort-'], values['-wiPasswort-']
            break

    passwort_window.close()


def dozierende_veranstaltung():
    """Alle Veranstaltungen eines Dozenten können eingesehen werden

    Tests: 
    * auf Zeile mit einer Veranstaltung klicken
    * auf 'Passwort ändern' und 'Abmelden'-Button klicken
    """

    sg.theme('TanBlue')

    veranstaltung_array = [[239847, 'Statistik', 'BWL'],
                           [837945, 'Mathe', 'Informatik']
                           ]
    
    headings = ['Veranstaltungs ID', 'Veranstaltungsname', 'Kurs']

    buttons = [[sg.Button('Passwort ändern', font=('any', 9, 'underline')),
                sg.Button('Abmelden', font=('any', 9, 'underline'))]
                ]

    layout = [[sg.Text('Herzlich Willkommen!'),
               sg.Column(buttons, element_justification='right', expand_x=True)],
              [sg.HorizontalSeparator()],
              [sg.Text('Veranstaltungen', font=('any', 12, 'bold')),
               sg.Button('neue Veranstaltungsnoten eintragen', font=('any', 9, 'underline'))],
              [sg.Table(values=veranstaltung_array, headings=headings, max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='left',
                        num_rows= 5,
                        key= '-table-',
                        row_height=35,
                        enable_events= True)]
                        ]
          
    veran_window = sg.Window('Studierendenverwaltungssystem',
                             layout, modal=True, size=(500, 500)
                             )

    while True:
        event, values = veran_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            passwort_aendern()
        elif event == "Abmelden":
            veran_window.close()
            erfolgreicher_logout()
        elif event == "neue Veranstaltungsnoten eintragen":
            veranstaltungsnoten_eintragen()
        elif event== "-table-":
            selected_row_index= values['-Table-'][0]
            veranstaltungs_information= veranstaltung_array[selected_row_index]
            veranstaltung_kurs(veranstaltungs_information)

    veran_window.close()


def veranstaltung_kurs(veran_info):
    """Jeder der teilnehmenden Studierenden wird in einer Tabelle mit seiner Note aufgeführt

    Args:
        veran_info (Array): Informationen über die Veranstaltung im Array gespeichert

    Tests:
    * Funktion von 'zurück'-Button testen
    *
    """

    sg.theme('TanBlue')

    veranstaltung_name = veran_info[1]
    kurs_info = [[9823057, 'nach1', 'Vor1', 2.6],
                 [2739474, 'nach2', 'Vor2', 1.8]]

    headings = ['Matrikelnummer','Nachname', 'Vorname', 'Note']

    layout = [[sg.Text(veranstaltung_name)],
              [sg.Table(values=kurs_info, headings=headings, max_col_width=35,
                        auto_size_columns=True,
                        display_row_numbers=False,
                        justification='left',
                        num_rows= 5,
                        key= '-table-',
                        row_height=35,
                        enable_events= True)],
              [sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    verankurs_window = sg.Window('Studierendenverwaltungssystem',
                                 layout, modal=True, size=(500, 500)
                                 )
    
    while True:
        event, values = verankurs_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            break
    
    verankurs_window.close()


def veranstaltungsnoten_eintragen():
    """Dozenten können hier die Noten ihrer Studierenden eintragen

    Tests:
    * Daten korrekt in die Eingabefelder eintragen
    * Daten inkorrekt in die Eingabefelder eintragen
    """

    sg.theme('TanBlue')

    layout = [[sg.Text('Veranstaltungsnoten eintragen', font=('any', 12, 'bold'))],
              [sg.Text('Veranstaltungs Id:'), 
               sg.InputText(key= '-veran_id-', do_not_clear=True)],
              [sg.Text('Studierenden ID:'), 
               sg.InputText(key='-studi_id-', do_not_clear=False)],
              [sg.Text('Punkte gesamt'), 
               sg.InputText(key= '-punkte_gesamt-', do_not_clear=True),
               sg.Text('Punkte erreicht'), 
               sg.InputText(key= '-punkte_erreicht-', do_not_clear=False)], 
              [sg.Button('OK', font=('any', 9, 'underline'))]
               ]
          
    veran_noten_window = sg.Window('Studierendenverwaltungssystem',
                                   layout, modal=True, size=(500, 500)
                                   )

    while True:
        event, values = veran_noten_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_pruefungsleistung(values['-studi_id-'], values['-veran_id-'],
                                        values['-punkte_gesamt-'], values['-punkte_erreicht-']
                                        )

    veran_noten_window.close()


def administration_allgemein():
    """ Sollen Studierende, Dozierende, Studiengangsleitung, Veranstaltungen 
        oder Module bearbeitet, neu angelet oder gelöscht werden

    Tests:
    * Buttons für Studierende, Dozierende, Kurse, Veranstaltungen und Module ausprobieren
    * auf 'Passwort ändern' und 'Abmelden'-Button klicken 
    """

    sg.theme('TanBlue')

    buttons = [[sg.Button('Passwort ändern', font=('any', 9, 'underline')), 
                sg.Button('Abmelden', font=('any', 9, 'underline'))]
                ]

    admin_column = [[sg.Text('Was möchten Sie bearbeiten/ anlegen oder löschen?')],
                    [sg.Button('Studierende', font=('any', 9, 'underline'), size=(15, 3)),
                     sg.Button('Dozierende', font=('any', 9, 'underline'), size=(15, 3)),
                     sg.Button('Admin', font=('any', 9, 'underline'), size=(15, 3))],
                    [sg.Button('Kurse', font=('any', 9, 'underline'), size=(15, 3)),
                     sg.Button('Veranstaltung', font=('any', 9, 'underline'), size=(15, 3)),
                     sg.Button('Modul', font=('any', 9, 'underline'), size=(15, 3))]
                     ]

    layout = [[sg.Text('Herzlich Willkommen!'), 
               sg.Column(buttons, element_justification='right', expand_x=True)],
              [sg.HorizontalSeparator()],
              [sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(admin_column, vertical_alignment='center', k='-C-')]
               ]
          
    admin_window = sg.Window('Studierendenverwaltungssystem',
                             layout, modal=True, size=(500, 500), finalize=True
                             )
    admin_window['-C-'].expand(True, True, True)
    admin_window['-1-'].expand(True, True, True)
    admin_window['-2-'].expand(True, False, True)

    while True:
        event, values = admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            passwort_aendern()
        elif event == "Abmelden":
            admin_window.close()
            erfolgreicher_logout()
        elif event == 'Studierende':
            studi_admin()
        elif event == 'Dozierende':
            doz_admin()
        elif event == 'Admin':
            admin_admin()
        elif event == 'Kurse':
            kurs_admin()
        elif event == 'Veranstaltung':
            veranstaltung_admin()
        elif event == 'Modul':
            modul_admin()

    admin_window.close()

    
def studi_admin():
    """Einen Studierenden bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Studierenden neu anlegen anklicken
    * Studierenden ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    studi_admin_column = [[sg.Text('Studierenden Administration'),
                           sg.Button('neuen Studierenden anlegen', font=('any', 9, 'underline'))],
                          [sg.Text('Studierenden ID:'),
                           sg.InputText(key= '-studi_id-', do_not_clear=False, size=(20, 2)),
                           sg.Button('bearbeiten', font=('any', 9, 'underline')),
                           sg.Button('löschen', font=('any', 9, 'underline'))],
                          [sg.Button('zurück', font=('any', 9, 'underline'))]
                           ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(studi_admin_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]
          
    studi_admin_window = sg.Window('Studierendenverwaltungssystem',
                                   layout, modal=True, size=(500, 500), finalize=True
                                   )
    studi_admin_window['-C-'].expand(True, True, True)
    studi_admin_window['-1-'].expand(True, True, True)
    studi_admin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values = studi_admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            studi_admin_window.close()
        elif event == 'neuen Studierenden anlegen':
            studi_anlegen()
        elif event == 'bearbeiten':
            studi_bearbeiten(values['-studi_id-'])
        elif event == 'löschen': 
            sg.popup(be.delete_student(values['-studi_id_']))
    
    studi_admin_window.close()


def doz_admin():
    """Einen Dozierenden bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Dozierenden neu anlegen anklicken
    * Dozierenden ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    doz_admin_column = [[sg.Text('Dozierenden Administration'),
                         sg.Button('neuen Dozierenden anlegen', font=('any', 9, 'underline'))],
                        [sg.Text('Dozierenden ID:'),
                         sg.InputText(key= '-dozierenden_id-', do_not_clear=False, size=(20, 2)),
                         sg.Button('bearbeiten', font=('any', 9, 'underline')),
                         sg.Button('löschen', font=('any', 9, 'underline'))],
                        [sg.Button('zurück', font=('any', 9, 'underline'))]
                         ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(doz_admin_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]
          
    doz_admin_window = sg.Window('Studierendenverwaltungssystem', 
                                 layout, modal=True, size=(500, 500), finalize=True
                                 )
    doz_admin_window['-C-'].expand(True, True, True)
    doz_admin_window['-1-'].expand(True, True, True)
    doz_admin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values = doz_admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            doz_admin_window.close()
        elif event == 'neuen Dozierenden anlegen':
            doz_anlegen()
        elif event == 'bearbeiten':
            doz_bearbeiten(values['-dozierenden_id-'])
        elif event == 'löschen':
            sg.popup(be.delete_dozent(values['-dozierenden_id-']))
    
    doz_admin_window.close()


def admin_admin():
    """
    """

    sg.theme('TanBlue')

    doz_admin_column = [[sg.Text('Admin Administration'),
                         sg.Button('neuen Administrator anlegen', font=('any', 9, 'underline'))],
                        [sg.Text('Admin ID:'),
                         sg.InputText(key= '-admin_id-', do_not_clear=False, size=(20, 2)),
                         sg.Button('bearbeiten', font=('any', 9, 'underline')),
                         sg.Button('löschen', font=('any', 9, 'underline'))],
                        [sg.Button('zurück', font=('any', 9, 'underline'))]
                         ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(doz_admin_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]
          
    admin_admin_window = sg.Window('Studierendenverwaltungssystem', 
                                   layout, modal=True, size=(500, 500), finalize=True
                                   )
    admin_admin_window['-C-'].expand(True, True, True)
    admin_admin_window['-1-'].expand(True, True, True)
    admin_admin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values = admin_admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            admin_admin_window.close()
        elif event == 'neuen Administrator anlegen':
            admin_anlegen()
        elif event == 'bearbeiten':
            admin_bearbeiten(values['-admin_id-'])
        elif event == 'löschen':
            sg.popup(be.delete_admin(values['-admin_id-']))
    
    admin_admin_window.close()


def kurs_admin():
    """Einen Kurs bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Kurs neu anlegen anklicken
    * Kurs ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    kurs_admin_column = [[sg.Text('Kurs Administration'), 
                          sg.Button('neuen Kurs anlegen', font=('any', 9, 'underline'))],
                         [sg.Text('Kurs ID:'), 
                          sg.InputText(key= '-kurs_id-', do_not_clear=False, size=(20, 2)), 
                          sg.Button('bearbeiten', font=('any', 9, 'underline')), 
                          sg.Button('löschen', font=('any', 9, 'underline'))],
                         [sg.Button('zurück', font=('any', 9, 'underline'))]
                          ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(kurs_admin_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]
          
    kurs_admin_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500), finalize=True
                                  )
    kurs_admin_window['-C-'].expand(True, True, True)
    kurs_admin_window['-1-'].expand(True, True, True)
    kurs_admin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values = kurs_admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            kurs_admin_window.close()
        elif event == 'neuen Kurs anlegen':
            kurs_anlegen()
        elif event == 'bearbeiten':
            kurs_bearbeiten(values['-kurs_id-'])
        elif event == 'löschen':
            sg.popup(be.delete_kurs['-kurs_id-'])
    
    kurs_admin_window.close()


def veranstaltung_admin():
    """Eine Veranstaltung bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Veranstaltung neu anlegen anklicken
    * Veranstaltung ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    veran_admin_column = [[sg.Text('Veranstaltung Administration'), 
                           sg.Button('neuen Veranstaltung anlegen', font=('any', 9, 'underline'))],
                          [sg.Text('Veranstaltung ID:'), 
                           sg.InputText(key= '-veranstaltung_id-', do_not_clear=False, size=(20, 2)), 
                           sg.Button('bearbeiten', font=('any', 9, 'underline')), 
                           sg.Button('löschen', font=('any', 9, 'underline'))],
                          [sg.Button('zurück', font=('any', 9, 'underline'))]
                           ]
          

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(veran_admin_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]
          
    veran_admin_window = sg.Window('Studierendenverwaltungssystem',
                                   layout, modal=True, size=(500, 500), finalize=True
                                   )
    veran_admin_window['-C-'].expand(True, True, True)
    veran_admin_window['-1-'].expand(True, True, True)
    veran_admin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values= veran_admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            veran_admin_window.close()
        elif event == 'neuen Veranstaltung anlegen':
            veranstaltung_anlegen()
        elif event == 'bearbeiten':
            veranstaltung_bearbeiten(values['-veranstaltung_id-'])
        elif event == 'löschen':
            sg.popup(be.delete_veranstaltung(values['-veranstaltung_id-']))
    
    veran_admin_window.close()


def modul_admin():
    """Einen Modul bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Modul neu anlegen anklicken
    * Modul ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    modul_admin_column = [[sg.Text('Modul Administration'), 
                           sg.Button('neuen Modul anlegen', font=('any', 9, 'underline'))],
                          [sg.Text('Modul ID:'), 
                           sg.InputText(key= '-modul_id-', do_not_clear=False, size=(20, 2)), 
                           sg.Button('bearbeiten', font=('any', 9, 'underline')), 
                           sg.Button('löschen', font=('any', 9, 'underline'))],
                          [sg.Button('zurück', font=('any', 9, 'underline'))]
                           ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(modul_admin_column, vertical_alignment='center', 
                         justification='center',  k='-C-')]
                         ]
          
    modul_admin_window = sg.Window('Studierendenverwaltungssystem', 
                                   layout, modal=True, size=(500, 500), finalize=True
                                   )
    modul_admin_window['-C-'].expand(True, True, True)
    modul_admin_window['-1-'].expand(True, True, True)
    modul_admin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values = modul_admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            modul_admin_window.close()
        elif event == 'neuen Modul anlegen':
            modul_anlegen()
        elif event == 'bearbeiten':
            modul_bearbeiten(values['-modul_id-'])
        elif event == 'löschen':
            sg.popup(be.delete_modul(values['-modul_id-']))
    
    modul_admin_window.close()


def studi_anlegen():
    """Einen neuen Studierenden anlegen

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    studi_anlegen_column = [[sg.Text('Studierende anlegen', font=('any', 12, 'bold'))],
                            [sg.Text('Studierenden ID: '),
                             sg.InputText(key='-studi_id-', do_not_clear=False)],
                            [sg.Text('Nachname: '),
                             sg.InputText(key= '-nachname-', do_not_clear=False)],
                            [sg.Text('Vorname: '),
                             sg.InputText(key= '-vorname-', do_not_clear=False)],
                            [sg.Text('Kurs ID: '),
                             sg.InputText(key= '-kurs_id-', do_not_clear=False)],
                            [sg.Text('Username: '),
                             sg.InputText(key= '-username-', do_not_clear=False)],
                            [sg.Text('Passwort: '),
                             sg.InputText(key= '-passwort-', do_not_clear=False)],
                            [sg.Button('OK', font=('any', 9, 'underline')),
                             sg.Button('zurück', font=('any', 9, 'underline'))]
                             ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))],
              [sg.Text('', pad=(0, 0), key='-2-'),
               sg.Column(studi_anlegen_column, vertical_alignment='center',
                         justification='center', k='-C-')]
              ]
          
    studi_anle_window = sg.Window('Studierendenverwaltungssystem', 
                                  layout, modal=True, size=(500, 500), finalize=True
                                  )
    studi_anle_window['-C-'].expand(True, True, True)
    studi_anle_window['-1-'].expand(True, True, True)
    studi_anle_window['-2-'].expand(True, False, True)

    while True:
        event, values = studi_anle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_student(values['-studi_id-'], values['-vorname-'], 
                              values['-nachname-'], values['-kurs_id-'], 
                              values['-username-'], values['-passwort']
                              )
        elif event == 'zurück':
            break

    studi_anle_window.close()


def doz_anlegen():
    """Ein neuer Dozierender angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    doz_anlegen_column = [[sg.Text('Dozierenden anlegen', font=('any', 12, 'bold'))],
                          [sg.Text('Dozierenden ID: '),
                           sg.InputText(key='-dozierenden_id-', do_not_clear=False)],
                          [sg.Text('Nachname: '),
                           sg.InputText(key= '-nachname-', do_not_clear=False)],
                          [sg.Text('Vorname: '),
                           sg.InputText(key= '-vorname-', do_not_clear=False)],
                          [sg.Text('Username: '),
                           sg.InputText(key= '-username-', do_not_clear=False)],
                          [sg.Text('Passwort: '),
                           sg.InputText(key= '-passwort-', do_not_clear=False)],
                          [sg.Button('OK', font=('any', 9, 'underline')),
                           sg.Button('zurück', font=('any', 9, 'underline'))]
                           ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))],
              [sg.Text('', pad=(0, 0), key='-2-'),
               sg.Column(doz_anlegen_column, vertical_alignment='center',
                         justification='center', k='-C-')]
              ]
          
    doz_anle_window = sg.Window('Studierendenverwaltungssystem',
                                layout, modal=True, size=(500, 500), finalize=True
                                )
    doz_anle_window['-C-'].expand(True, True, True)
    doz_anle_window['-1-'].expand(True, True, True)
    doz_anle_window['-2-'].expand(True, False, True)

    while True:
        event, values= doz_anle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_dozent(values['-dozierenden_id-'], values['-vorname-'], 
                             values['-nachname-'], values['-username-'],
                             values['-passwort']
                             )
        elif event == 'zurück':
            break

    doz_anle_window.close()


def admin_anlegen():
    """Einen neuen Administrator anlegen

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    admin_anlegen_column = [[sg.Text('Administrator anlegen', font=('any', 12, 'bold'))],
                            [sg.Text('Admin ID: '),
                             sg.InputText(key='-admin_id-', do_not_clear=False)],
                            [sg.Text('Nachname: '),
                             sg.InputText(key= '-nachname-', do_not_clear=False)],
                            [sg.Text('Vorname: '),
                             sg.InputText(key= '-vorname-', do_not_clear=False)],
                            [sg.Text('Username: '),
                             sg.InputText(key= '-username-', do_not_clear=False)],
                            [sg.Text('Passwort: '),
                             sg.InputText(key= '-passwort-', do_not_clear=False)],
                            [sg.Button('OK', font=('any', 9, 'underline')),
                             sg.Button('zurück', font=('any', 9, 'underline'))]
                             ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))],
              [sg.Text('', pad=(0, 0), key='-2-'),
               sg.Column(admin_anlegen_column, vertical_alignment='center',
                         justification='center', k='-C-')]
              ]
          
    admin_anle_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500), finalize=True
                                  )
    admin_anle_window['-C-'].expand(True, True, True)
    admin_anle_window['-1-'].expand(True, True, True)
    admin_anle_window['-2-'].expand(True, False, True)

    while True:
        event, values = admin_anle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_admin(values['-admin_id-'], values['-vorname-'], 
                            values['-nachname-'], values['-username-'],
                            values['-passwort']
                            )
        elif event == 'zurück':
            break

    admin_anle_window.close()


def kurs_anlegen():
    """Ein neuer Kurs angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    kurs_anlegen_column = [[sg.Text('Kurs anlegen', font=('any', 12, 'bold'))],
                           [sg.Text('Kurs ID: *'),
                            sg.InputText(key='-kurs_id-', do_not_clear=False)],
                           [sg.Text('Kurs Name: *'),
                            sg.InputText(key= '-kurs_name-', do_not_clear=False)],
                           [sg.Text('Dozierenden ID: *'),
                            sg.InputText(key= '-dozierenden_id-', do_not_clear=False)],
                           [sg.Button('OK', font=('any', 9, 'underline')),
                            sg.Button('zurück', font=('any', 9, 'underline'))]
                            ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))],
              [sg.Text('', pad=(0, 0), key='-2-'),
               sg.Column(kurs_anlegen_column, vertical_alignment='center',
                         justification='center', k='-C-')]
              ]
          
    kurs_anle_window = sg.Window('Studierendenverwaltungssystem', 
                                 layout, modal=True, size=(500, 500), finalize=True
                                 )
    kurs_anle_window['-C-'].expand(True, True, True)
    kurs_anle_window['-1-'].expand(True, True, True)
    kurs_anle_window['-2-'].expand(True, False, True)

    while True:
        event, values = kurs_anle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_kurs(values['-kurs_id-'], 
                           values['-kurs_name-'], values['-dozierenden_id-']
                           )
        elif event == 'zurück':
            break

    kurs_anle_window.close()


def veranstaltung_anlegen():
    """Eine neue Veranstaltung angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    veranstaltung_anlegen_column = [[sg.Text('Veranstaltung anlegen', font=('any', 12, 'bold'))],
                                    [sg.Text('Veranstaltung ID: *'),
                                     sg.InputText(key='-veranstaltung_id-', do_not_clear=False)],
                                    [sg.Text('Veranstaltungsname: *'),
                                     sg.InputText(key= '-veranstaltungsname-', do_not_clear=False)],
                                    [sg.Text('Dozierenden ID: *'),
                                     sg.InputText(key= '-dozierenden_id-', do_not_clear=False)],
                                    [sg.Text('Modul ID: *'),
                                     sg.InputText(key= '-modul_id-', do_not_clear=False)],
                                    [sg.Button('OK', font=('any', 9, 'underline')),
                                     sg.Button('zurück', font=('any', 9, 'underline'))]
                                     ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))],
              [sg.Text('', pad=(0, 0), key='-2-'),
               sg.Column(veranstaltung_anlegen_column, vertical_alignment='center',
                         justification='center', k='-C-')]
                         ]
          
    veran_anle_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500), finalize=True
                                  )
    veran_anle_window['-C-'].expand(True, True, True)
    veran_anle_window['-1-'].expand(True, True, True)
    veran_anle_window['-2-'].expand(True, False, True)

    while True:
        event, values = veran_anle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_veranstaltung(values['-veranstaltung_id-'], values['-veranstaltungsname-'], 
                                    values['-dozierenden_id-'], values['-modul_id-']
                                    )
        elif event == 'zurück':
            break

    veran_anle_window.close()


def modul_anlegen():
    """Ein neues Modul angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    modul_anlegen_column = [[sg.Text('Modul anlegen', font=('any', 12, 'bold'))],
                            [sg.Text('Modul ID: *'),
                             sg.InputText(key='-modul_id-', do_not_clear=False)],
                            [sg.Text('Modulname: *'),
                             sg.InputText(key= '-modulname-', do_not_clear=False)],
                            [sg.Text('Kurs ID: *'),
                             sg.InputText(key= '-kurs_id-', do_not_clear=False)],
                            [sg.Text('Credits: *'),
                             sg.InputText(key= '-credits-', do_not_clear=False)],
                            [sg.Button('OK', font=('any', 9, 'underline')),
                             sg.Button('zurück', font=('any', 9, 'underline'))]
                             ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))],
              [sg.Text('', pad=(0,0), key='-2-'),
               sg.Column(modul_anlegen_column, vertical_alignment='center',
                         justification='center',  k='-C-')]
                         ]

    modul_anle_window = sg.Window('Studierendenverwaltungssystem', 
                                  layout, modal=True, size=(500, 500), finalize=True
                                  )
    modul_anle_window['-C-'].expand(True, True, True)
    modul_anle_window['-1-'].expand(True, True, True)
    modul_anle_window['-2-'].expand(True, False, True)

    while True:
        event, values = modul_anle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.create_modul(values['-modul_id-'], values['-modulname-'], 
                            values['-kurs_id-'], values['-credits-']
                            )
        elif event == 'zurück':
            break

    modul_anle_window.close()


def studi_bearbeiten(studi_id: int):
    """Informationen über einen Studierenden können verändert werden 

    Args:
        studi_id (int): ID eines Studierende als Integer

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
    
    studi_help = be.get_student(studi_id)
    studi = studi_help[0]


    layout = [[sg.Text('Studierenden bearbeiten', font=('any', 12, 'bold'))],
              [sg.Text('Studierenden ID:'), sg.Text(studi[0]), 
               sg.InputText(key='-studi_id-', do_not_clear=False)],
              [sg.Text('Vorname:'), sg.Text(studi[1]),
               sg.InputText(key= '-vorname-', do_not_clear=False)], 
              [sg.Text('Nachname:'), sg.Text(studi[2]), 
               sg.InputText(key= '-nachname-', do_not_clear=False)],
              [sg.Text('Kurs ID:'), sg.Text(studi[3]), 
               sg.InputText(key= '-kurs_id-', do_not_clear=False)],
              [sg.Text('Username:'), sg.Text(studi[4]), 
               sg.InputText(key= '-username-', do_not_clear=False)],
              [sg.Text('Passwort:'), sg.Text(studi[5]), 
               sg.InputText(key= '-passwort-', do_not_clear=False)],
              [sg.Button('OK', font=('any', 9, 'underline')), 
               sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    studi_bear_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500)
                                  )

    while True:
        event, values = studi_bear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.change_student(studi[0], values['-studi_id-'], values['-vorname-'], 
                              values['-nachname-'], values['-kurs_id-'], 
                              values['-username'], values['-passwort']
                              )
        elif event == 'zurück':
            break

    studi_bear_window.close()


def doz_bearbeiten(dozierenden_id: int):
    """Informationen über einen Dozendierenden können verändert werden 

    Args:
        Dozierenden_id (int): ID eines Dozierenden als Integer

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
    
    doz_help = be.get_dozent(dozierenden_id)
    doz= doz_help[0]

    layout = [[sg.Text('Dozierenden bearbeiten', font=('any', 12, 'bold'))],
              [sg.Text('Dozierenden ID:'), sg.Text(doz[0]), 
               sg.InputText(key='-doz_id-', do_not_clear=False)],
              [sg.Text('Nachname:'), sg.Text(doz[1]), 
               sg.InputText(key= '-nachname-', do_not_clear=False)], 
              [sg.Text('Vorname:'), sg.Text(doz[2]), 
               sg.InputText(key= '-vorname-', do_not_clear=False)],
              [sg.Text('Username:'), sg.Text(doz[3]), 
               sg.InputText(key= '-username-', do_not_clear=False)],
              [sg.Text('Passwort:'), sg.Text(doz[4]), 
               sg.InputText(key= '-passwort-', do_not_clear=False)],
              [sg.Button('OK', font=('any', 9, 'underline')), 
               sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    doz_bear_window = sg.Window('Studierendenverwaltungssystem',
                                layout, modal=True, size=(500, 500)
                                )

    while True:
        event, values = doz_bear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.change_dozent(doz[0], values['-doz_id-'], 
                             values['-vorname-'], values['-nachname-'], 
                             values['-username'], values['-passwort']
                             )
        elif event == 'zurück':
            break

    doz_bear_window.close()


def admin_bearbeiten(admin_id: int):
    """Informationen über einen Administrator können verändert werden 

    Args:
        admin_id (int): Id des Administrators der 
                        bearbeitet werden soll in Integer

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
    
    admin_help = be.get_admin(admin_id)
    admin = admin_help[0]

    layout = [[sg.Text('Dozierenden bearbeiten', font=('any', 12, 'bold'))],
              [sg.Text('Dozierenden ID:'), sg.Text(admin[0]), 
               sg.InputText(key='-doz_id-', do_not_clear=False)],
              [sg.Text('Nachname:'), sg.Text(admin[1]), 
               sg.InputText(key= '-nachname-', do_not_clear=False)], 
              [sg.Text('Vorname:'), sg.Text(admin[2]), 
               sg.InputText(key= '-vorname-', do_not_clear=False)],
              [sg.Text('Username:'), sg.Text(admin[3]), 
               sg.InputText(key= '-username-', do_not_clear=False)],
              [sg.Text('Passwort:'), sg.Text(admin[4]), 
               sg.InputText(key= '-passwort-', do_not_clear=False)],
              [sg.Button('OK', font=('any', 9, 'underline')), 
               sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    admin_bear_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500)
                                  )

    while True:
        event, values = admin_bear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.change_admin(admin[0], values['-admin_id-'], 
                            values['-vorname-'], values['-nachname-'], 
                            values['-username'], values['-passwort']
                            )
        elif event == 'zurück':
            break

    admin_bear_window.close()


def kurs_bearbeiten(kurs_id :int):
    """Informationen über einen Kurs können verändert werden 

    Args:
        Kurs_id (int): ID eines Kurses als Integer

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
        
    kurs_help = be.get_kurs(kurs_id)
    kurs = kurs_help[0]

    layout = [[sg.Text('Kurs bearbeiten', font=('any', 12, 'bold'))],
              [sg.Text('Kurs ID:'), sg.Text(kurs[0]), 
               sg.InputText(key='-kurs_id-', do_not_clear=False)],
              [sg.Text('Kursname:'), sg.Text(kurs[1]), 
               sg.InputText(key= '-kursname-', do_not_clear=False)], 
              [sg.Text('Dozierenden ID:'), sg.Text(kurs[2]), 
               sg.InputText(key= '-doz_id-', do_not_clear=False)],
              [sg.Button('OK', font=('any', 9, 'underline')), 
               sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    kurs_bear_window = sg.Window('Studierendenverwaltungssystem',
                                 layout, modal=True, size=(500, 500)
                                 )

    while True:
        event, values = kurs_bear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.change_kurs(kurs[0], values['-kurs_id-'], 
                           values['-kursname-'], values['-doz_id-']
                           )
        elif event == 'zurück':
            break

    kurs_bear_window.close()


def veranstaltung_bearbeiten(veran_id: int):
    """Informationen über eine Veranstaltung können verändert werden 

    Args:
        Veran_id (int): ID einer Veranstaltung als Integer

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
        
    veran_help = be.get_veranstaltung(veran_id)
    veran = veran_help[0]

    layout = [[sg.Text('Veranstaltung bearbeiten', font=('any', 12, 'bold'))],
              [sg.Text('Veranstaltungs ID:'), sg.Text(veran[0]), 
               sg.InputText(key='-veran_id-', do_not_clear=False)],
              [sg.Text('Veranstaltungsname:'), sg.Text(veran[1]), 
               sg.InputText(key= '-veranname-', do_not_clear=False)], 
              [sg.Text('Dozierenden ID:'), sg.Text(veran[2]), 
               sg.InputText(key= '-doz_id-', do_not_clear=False)],
              [sg.Text('Modul ID:'), sg.Text(veran[3]), 
               sg.InputText(key= '-modul_id-', do_not_clear=False)],
              [sg.Button('OK', font=('any', 9, 'underline')), 
               sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    veran_bear_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500)
                                  )

    while True:
        event, values = veran_bear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.change_veranstaltung(veran[0], values['-veran_id-'], 
                                    values['-veranname-'], values['-doz_id-'], 
                                    values['-modul_id-']
                                    )
        elif event == 'zurück':
            break

    veran_bear_window.close()


def modul_bearbeiten(modul_id: int):
    """Die Informationen eines Moduls können verändert werden

    Args:
        Modul_id (int): ID eines Moduls als Integer

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
        
    modul_help = be.get_modul(modul_id)
    modul = modul_help[0]

    layout = [[sg.Text('Modul bearbeiten', font=('any', 12, 'bold'))],
              [sg.Text('Modul ID:'), sg.Text(modul[0]), 
               sg.InputText(key='-modul_id-', do_not_clear=False)],
              [sg.Text('Modulname:'), sg.Text(modul[1]), 
               sg.InputText(key= '-modulname-', do_not_clear=False)], 
              [sg.Text('Kurs ID:'), sg.Text(modul[2]), 
               sg.InputText(key= '-kurs_id-', do_not_clear=False)],
              [sg.Text('Credits:'), sg.Text(modul[3]), 
               sg.InputText(key= '-credits-', do_not_clear=False)],
              [sg.Button('OK', font=('any', 9, 'underline')), 
               sg.Button('zurück', font=('any', 9, 'underline'))]
               ]
          
    modul_bear_window = sg.Window('Studierendenverwaltungssystem',
                                  layout, modal=True, size=(500, 500)
                                  )

    while True:
        event, values = modul_bear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            be.change_modul(modul[0], values['-modul_id-'], 
                            values['-modulname-'], values['-credits-'], 
                            values['-kurs_id-']
                            )
        elif event == 'zurück':
            break

    modul_bear_window.close()


if __name__ == "__main__":
    administration_allgemein()


