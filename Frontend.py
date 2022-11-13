"""Modul für Frontend

author: Daniela Mayer
date: 27.10.2022
version: 1.0.0
licence: free
"""

import PySimpleGUI as sg

def AnmeldeSeite():
    """Implimentierung der Login Seite

    Tests:
        *
        *
    """
    
    layout = [[sg.Text('Login', font=('any', 12, 'bold'))],
          [sg.Text('Username: *'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort: *'), sg.InputText(key='-passwort-', do_not_clear=False)],
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



def main():
    """Seite für Studierende für die Einsicht der Modulnoten, sowie GPA 

    Tests:
        *
        *
    """

    modul_information_array=[
        [87392345, 'Programmierung', 5.0, 1.6, True],
        [72934982, 'Mathe 1', 5.0, 2.5, True]]

    headings=['Modul ID','Modul', 'Cedits', 'Note', 'best.']
    
    layout = [[sg.Text('Herzlich Willkommen!'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Leistungsübersicht', font=('any', 12, 'bold'))],
          [sg.Table(values=modul_information_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='left',
                    num_rows= 10,
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
            PasswortAendernSeite()
        elif event == "Abmelden":
            Studi_window.close()
            ErfolgreicherLogout()
        elif event== "-Table-":
            selected_row_index= values['-Table-'][0]
            Modul_information= modul_information_array[selected_row_index]
            StudierendenAnsichtModul(Modul_information)

    Studi_window.close()



def StudierendenAnsichtModul(Modul_info):
    """ Informationen über Veranstaltungen eines Moduls mit Noten und Punkten

    Args:
        Modul_info (_type_): _description_

    Test:
        *
        *
    """

    Modul_name= Modul_info[1]
    Modul_Note= str(Modul_info[3])
    Modulinhalt=[[9823057, 'Java', 60, 45, 2.6],
                [2739474, 'Python', 60, 55, 1.8]]

    headings=['Veranstalungs ID','Veranstaltung', 'P. g.', 'P. e.', 'Note']

    layout = [[sg.Text(Modul_name)],
            [sg.Table(values=Modulinhalt, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)],
            [sg.Text(Modul_name + ", Note " + Modul_Note)],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            window.close()
    
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
          [sg.Text('Passwort wiederholen *'), sg.InputText(key='-wiPasswort-', do_not_clear=False)],
          [sg.Button('Ändern')]]

    Passwort_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Passwort_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Ändern":
            ÄnderungsDaten= values['-name-'], values['-passwort-'], values['-neuesPasswort-'], values['-wiPasswort-']
            Passwort_window.close()

    Passwort_window.close()


def PasswortAendernSeiteFalse():
    """Seite zum ändern des Passwortes

    Tests:
        *
        *
    """

    layout = [[sg.Text('Passwort ändern', font=('any', 12, 'bold'))],
          [sg.Text('Eine der Angaben ist nicht korrekt. Versuchen Sie es noch einmal!', text_color='red')],
          [sg.Text('Username *'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort *'), sg.InputText(key='-passwort-', do_not_clear=False)],
          [sg.Text('neues Passwort *'), sg.InputText(key='-neuesPasswort-', do_not_clear=False)],
          [sg.Text('Passwort wiederholen *'), sg.InputText(key='-wiPasswort-', do_not_clear=False)],
          [sg.Button('Ändern')]]

    Passwort_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Passwort_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Ändern":
            ÄnderungsDaten= values['-name-'], values['-passwort-'], values['-neuesPasswort-'], values['-wiPasswort-']
            Passwort_window.close()

    Passwort_window.close()


def DozierendenVeranstaltungsansicht():
    """Alle Veranstaltungen eines Dozenten können eingesehen werden

    Tests: 
    *
    *
    """

    Veranstaltung_array=[[239847, 'Statistik', 'BWL'],
                    [837945, 'Mathe', 'Informatik']]
    
    headings=['Veranstaltungs ID', 'Veranstaltungsname', 'Kurs']

    layout = [[sg.Text('Herzlich Willkommen'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Veranstaltungen', font=('any', 12, 'bold')), sg.Button('neue Veranstaltungsnoten eintragen', font=('any', 9, 'underline'))],
          [sg.Table(values=Veranstaltung_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)]
          ]
          
    Veran_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Veran_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            PasswortAendernSeite
        elif event == "Abmelden":
            Veran_window.close()
            ErfolgreicherLogout
        elif event == "neue Veranstaltungsnoten eintragen":
            VeranstaltungsnotenEintragenDoz()
        elif event== "-Table-":
            selected_row_index= values['-Table-'][0]
            Veranstaltungs_information= Veranstaltung_array[selected_row_index]
            VeranstaltungKursAnsicht(Veranstaltungs_information)

    Veran_window.close()


def VeranstaltungKursAnsicht(info):
    """Jeder der teilnehmenden Studierenden wird in einer Tabelle mit seiner Note aufgeführt

    Args:
        info (Array): Informationen über die Veranstaltung

    Tests:
    *
    *
    """

    Veranstaltung_name= info[1]
    Kurs_info=[[9823057, 'nach1', 'Vor1', 2.6],
                [2739474, 'nach2', 'Vor2', 1.8]]

    headings=['Matrikelnummer','Nachname', 'Vorname', 'Note']

    layout = [[sg.Text(Veranstaltung_name)],
            [sg.Table(values=Kurs_info, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='left',
                    num_rows= 5,
                    key= '-Table-',
                    row_height=35,
                    enable_events= True)],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    Verankurs_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Verankurs_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Verankurs_window.close()
    
    Verankurs_window.close()



def VeranstaltungsnotenEintragenDoz():
    """Dozenten können hier die Noten ihrer Studierenden eintragen

    Tests:
    *
    *
    """
    
 
    Bestanden= (True, False)
    Prüfungsinfo_Veranstaltung_Array= []

    layout = [[sg.Text('Veranstaltungsnoten eintragen', font=('any', 12, 'bold'))],
          [sg.Text('Veranstaltungs Id:'), sg.InputText(key= '-Veran_id-', do_not_clear=True)],
          [sg.Text('Matrikelnummer:'), sg.InputText(key='-Matrikelnummer-', do_not_clear=False)],
          [sg.Text('Punkte gesamt'), sg.InputText(key= '-Punkte_gesamt-', do_not_clear=True), sg.Text('Punkte erreicht'), sg.InputText(key= '-Punkte_erreicht-', do_not_clear=False)], 
          [sg.Text('Note'), sg.InputText(key= '-Note-', do_not_clear=False)],
          [sg.Text('Bestanden'), sg.Combo(Bestanden, enable_events=True, key='-Bestanden-')],
          [sg.Button('OK', font=('any', 9, 'underline'))]]
          
    VeranNoten_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= VeranNoten_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            Prüfungsinfo_Veranstaltung= values['-Veran_id-'], values['-Matrikelnummer-'], values['-Versuch-'], 
            values['-Punkte_gesamt-'], values['-Punkte_erreicht-'], values['-Note-'], values['-Bestanden-']
            Prüfungsinfo_Veranstaltung_Array.append(Prüfungsinfo_Veranstaltung)

    VeranNoten_window.close()



def AdministrationAllgemein():
    """Erste Seite des Administrators
    * sollen Studierende, Dozierende, Studiengangsleitung, Veranstaltungen oder Module bearbeitet, neu angelet oder gelöscht werden

    Tests:
    *
    * 
    """

    layout = [[sg.Text('Administration'), sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))],
          [sg.Text('Was möchten Sie bearbeiten/ anlegen oder löschen?')],
          [sg.Button('Studierende', font=('any', 9, 'underline')), sg.Button('Dozierende', font=('any', 9, 'underline')), sg.Button('Kurse', font=('any', 9, 'underline'))],
          [sg.Button('Veranstaltung', font=('any', 9, 'underline')), sg.Button('Modul', font=('any', 9, 'underline'))]]
          
    Admin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Admin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            PasswortAendernSeite()
        elif event == "Abmelden":
            Admin_window.close()
            ErfolgreicherLogout()
        elif event == 'Studierende':
            StudiAdmin()
        elif event == 'Dozierende':
            DozAdmin()
        elif event == 'Kurse':
            KursAdmin()
        elif event == 'Veranstaltung':
            VeranstaltungAdmin()
        elif event == 'Modul':
            ModulAdmin()

    Admin_window.close()

def StudiAdmin():
    """Einen Studierenden bearbeiten/ anlegen oder löschen

    Tests:
    *
    *
    """

    layout = [[sg.Text('Studierenden Administration'), sg.Button('neuen Studierenden anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Matrikelnummer:'), sg.InputText(key= '-Matrikelnummer-', do_not_clear=False), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    Studiadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Studiadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Studiadmin_window.close()
        elif event == 'neuen Studierenden anlegen':
            Studianlegen()
        elif event == 'bearbeiten':
            Studibearbeiten(values['-Matrikelnummer-'])
        elif event == 'löschen':
            break
    
    Studiadmin_window.close()


def DozAdmin():
    """Einen Dozierenden bearbeiten/ anlegen oder löschen

    Tests:
    *
    *
    """

    layout = [[sg.Text('Dozierenden Administration'), sg.Button('neuen Dozierenden anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Dozierenden ID:'), sg.InputText(key= '-dozierenden_id-', do_not_clear=False), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    Dozadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Dozadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Dozadmin_window.close()
        elif event == 'neuen Dozierenden anlegen':
            Dozanlegen()
        elif event == 'bearbeiten':
            Dozbearbeiten(values['-dozierenden_id-'])
        elif event == 'löschen':
            break
    
    Dozadmin_window.close()



def KursAdmin():
    """Einen Studierenden bearbeiten/ anlegen oder löschen

    Tests:
    *
    *
    """

    layout = [[sg.Text('Kurs Administration'), sg.Button('neuen Kurs anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Kurs ID:'), sg.InputText(key= '-kurs_id-', do_not_clear=False), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    Kursadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Kursadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Kursadmin_window.close()
        elif event == 'neuen Kurs anlegen':
            Kursanlegen()
        elif event == 'bearbeiten':
            Kursbearbeiten(values['-kurs_id-'])
        elif event == 'löschen':
            break
    
    Kursadmin_window.close()



def VeranstaltungAdmin():
    """Einen Studierenden bearbeiten/ anlegen oder löschen

    Tests:
    *
    *
    """

    layout = [[sg.Text('Veranstaltung Administration'), sg.Button('neuen Veranstaltung anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Veranstaltung ID:'), sg.InputText(key= '-veranstaltung_id-', do_not_clear=False), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    Veranadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Veranadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Veranadmin_window.close()
        elif event == 'neuen Veranstaltung anlegen':
            Veranstaltunganlegen()
        elif event == 'bearbeiten':
            Veranstaltungbearbeiten(values['-veranstaltung_id-'])
        elif event == 'löschen':
            break
    
    Veranadmin_window.close()



def ModulAdmin():
    """Einen Studierenden bearbeiten/ anlegen oder löschen

    Tests:
    *
    *
    """

    layout = [[sg.Text('Modul Administration'), sg.Button('neuen Modul anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Modul ID:'), sg.InputText(key= '-modul_id-', do_not_clear=False), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    Moduladmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)
    
    while True:
        event, values= Moduladmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Moduladmin_window.close()
        elif event == 'neuen Modul anlegen':
            Modulanlegen()
        elif event == 'bearbeiten':
            Modulbearbeiten(values['-modul_id-'])
        elif event == 'löschen':
            break
    
    Moduladmin_window.close()



def Studianlegen():
    """Einen neuen Studierenden anlegen

    Tests:
    *
    *
    """
    
    Studierenden_Info_Array= []

    layout = [[sg.Text('Studierende anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Matrikelnummer: *'), sg.InputText(key='-Matrikelnummer-', do_not_clear=False)],
          [sg.Text('Nachname: *'), sg.InputText(key= '-Nachname-', do_not_clear=False)], 
          [sg.Text('Vorname: *'), sg.InputText(key= '-Vorname-', do_not_clear=False)],
          [sg.Text('Kurs ID: *'), sg.InputText(key= '-Kurs_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Studianle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Studianle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            StudierendenInfo= values['-Matrikelnummer-'], values['-Nachname-'], 
            values['-Vorname-'], values['-Kurs_id-']
            Studierenden_Info_Array.append(StudierendenInfo)
        elif event == 'zurück':
            break

    Studianle_window.close()


def Dozanlegen():
    """Ein neuer Dozierender angelegt

    Tests:
    *
    *
    """

    Dozierenden_Info_Array= []

    layout = [[sg.Text('Dozierenden anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Dozierenden ID: *'), sg.InputText(key='-dozierenden_id-', do_not_clear=False)],
          [sg.Text('Nachname: *'), sg.InputText(key= '-Nachname-', do_not_clear=False)], 
          [sg.Text('Vorname: *'), sg.InputText(key= '-Vorname-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Dozanle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Dozanle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            DozierendenInfo= values['-dozierenden_id-'], values['-Nachname-'], 
            values['-Vorname-']
            Dozierenden_Info_Array.append(DozierendenInfo)
        elif event == 'zurück':
            break

    Dozanle_window.close()



def Kursanlegen():
    """Ein neuer Kurs angelegt

    Tests:
    *
    *
    """

    Kurs_Info_Array= []

    layout = [[sg.Text('Kurs anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Kurs ID: *'), sg.InputText(key='-kurs_id-', do_not_clear=False)],
          [sg.Text('Kurs Name: *'), sg.InputText(key= '-kurs_name-', do_not_clear=False)], 
          [sg.Text('Dozierenden ID: *'), sg.InputText(key= '-dozierenden_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Kursanle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Kursanle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            KursInfo= values['-kurs_id-'], values['-kurs_name-'], 
            values['-dozierenden_id-']
            Kurs_Info_Array.append(KursInfo)
        elif event == 'zurück':
            break

    Kursanle_window.close()



def Veranstaltunganlegen():
    """Eine neue Veranstaltung angelegt

    Tests:
    *
    *
    """

    Veran_Info_Array= []

    layout = [[sg.Text('Veranstaltung anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Veranstaltung ID: *'), sg.InputText(key='-Veranstaltung_id-', do_not_clear=False)],
          [sg.Text('Veranstaltungsname: *'), sg.InputText(key= '-veranstaltungsname-', do_not_clear=False)], 
          [sg.Text('Dozierenden ID: *'), sg.InputText(key= '-dozierenden_id-', do_not_clear=False)],
          [sg.Text('Modul ID: *'), sg.InputText(key= '-modul_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Verananle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Verananle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            VeranInfo= values['-Veranstaltung_id-'], values['-veranstaltungsname-'], 
            values['-dozierenden_id-'], values['-modul_id-']
            Veran_Info_Array.append(VeranInfo)
        elif event == 'zurück':
            break

    Verananle_window.close()



def Modulanlegen():
    """Ein neues Modul angelegt

    Tests:
    *
    *
    """

    Modul_Info_Array= []

    layout = [[sg.Text('Modul anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Modul ID: *'), sg.InputText(key='-modul_id-', do_not_clear=False)],
          [sg.Text('Modulname: *'), sg.InputText(key= '-modulname-', do_not_clear=False)], 
          [sg.Text('Kurs ID: *'), sg.InputText(key= '-kurs_id-', do_not_clear=False)],
          [sg.Text('Credits: *'), sg.InputText(key= '-credits-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Modulanle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True)

    while True:
        event, values= Modulanle_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            ModulInfo= values['-modul_id-'], values['-modulname-'], 
            values['-kurs_id-'], values['-credits-']
            Modul_Info_Array.append(ModulInfo)
        elif event == 'zurück':
            break

    Modulanle_window.close()



def Studibearbeiten(Matrikelnummer: int):
    """Informationen über einen Studierenden können verändert werden 

    Args:
        Matrikelnummer (int): _description_

    Tests:
    *
    *
    """

    Studi_Array=[2983642, 'Vorname', 'Nachname', 238404]


def Dozbearbeiten(Dozierenden_id: int):
    """Informationen über einen Dozendierenden können verändert werden 

    Args:
        Dozierenden_id (int): _description_

    Tests:
    *
    *
    """


def Kursbearbeiten(Kurs_id :int):
    """Informationen über einen Kurs können verändert werden 

    Args:
        Kurs_id (int): _description_

    Tests:
    *
    *
    """


def Veranstaltungbearbeiten(Veran_id: int):
    """Informationen über eine Veranstaltung können verändert werden 

    Args:
        Veran_id (int): _description_

    Tests:
    *
    *
    """



def Modulbearbeiten(Modul_id: int):
    """Die Informationen eines Moduls können verändert werden

    Args:
        Modul_id (int): _description_

    Tests:
    *
    *
    """


if __name__ == "__main__":
    main()


