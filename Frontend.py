"""Modul für Frontend

author: Daniela Mayer
date: 13.11.2022
version: 2.0.0
licence: free
"""

import PySimpleGUI as sg
import Student_be as sb

def Login():
    """Implimentierung der Login Seite

    Tests:
        * richtige Logindaten als Dozierender/ Studierender/ Admin eintragen
        * falsche Logindaten eingeben
    """
    sg.theme('TanBlue')

    Nutzer= ('Studierender', 'Dozierender', 'Admin')

    LoginColumn = [[sg.Text('Login', font=('any', 12, 'bold'))],
          [sg.Combo(Nutzer, enable_events=True, key='-nutzer-')],
          [sg.Text('ID: *'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort: * '), sg.InputText(key='-passwort-', do_not_clear=False)],
          [sg.Button('Anmelden', font=('any', 9, 'underline'))]]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(LoginColumn, vertical_alignment='center', justification='center',  k='-C-')]]

    Login_window=sg.Window('Studierendenverwaltungssystem', layout, size=(500, 500), finalize=True)
    Login_window['-C-'].expand(True, True, True)
    Login_window['-1-'].expand(True, True, True)
    Login_window['-2-'].expand(True, False, True)

    while True:
        event, values= Login_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Anmelden":
            Login_window.close()
            AnmeldeDaten= values['-name-'], values['-passwort-']
            if values['-nutzer-']== 'Studierender':
                StudierendeAllgemein()
            elif values['-nutzer-'] == 'Dozierender':
                DozierendenVeranstaltungsansicht()
            elif values['-nutzer-']== 'Admin':
                AdministrationAllgemein()
            
    Login_window.close()



def FalseLogin():
    """Implimentierung der Seite nach falschem einloggen

    Tests:
        * richtige Logindaten als Dozierender/ Studierender/ Admin eintragen
        * falsche Logindaten eingeben
    """
    
    sg.theme('TanBlue')

    Nutzer= ("Studierender", "Dozierender", "Admin")

    FalseLoginColumn = [[sg.Text('Login', font=('any', 12, 'bold'))],
        [sg.Text('ID oder Passwort falsch', text_color= 'red')],
        [sg.Combo(Nutzer, enable_events=True, key='-nutzer-')],
        [sg.Text('ID:'), sg.InputText(key='-name-', do_not_clear=False)],
        [sg.Text('Passwort:'), sg.InputText(key='-passwort-', do_not_clear=False)],
        [sg.Button('Anmelden', font=('any', 9, 'underline'))],
        [sg.Text('Bei vergessenem Passwort, wenden Sie sich an den Administrator!')]]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(FalseLoginColumn, vertical_alignment='center', justification='center',  k='-C-')]]

    FalseLogin_window=sg.Window('Studierendenverwaltungssystem', layout, size=(500, 500), finalize=True)
    FalseLogin_window['-C-'].expand(True, True, True)
    FalseLogin_window['-1-'].expand(True, True, True)
    FalseLogin_window['-2-'].expand(True, False, True)

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
        * 'neu Anmelden' ausprobieren
        * Fenster schließen
    """

    sg.theme('TanBlue')

    LogoutColumn = [[sg.Text('Sie haben sich erfolgreich abgemeldet!', font=('any', 15))],
                [sg.Text('   ')],
                [sg.Button('neu Anmelden', font=('any', 9, 'underline'))]]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(LogoutColumn, vertical_alignment='center', justification='right',  k='-C-')]]

    Logout_window=sg.Window('Studierendenverwaltungssystem', layout, size=(500, 500), finalize=True)
    Logout_window['-C-'].expand(True, True, True)
    Logout_window['-1-'].expand(True, True, True)
    Logout_window['-2-'].expand(True, False, True)

    while True:
        event, values= Logout_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "neu Anmelden":
            Logout_window.close()
            Login() 

    Logout_window.close()

    

def StudierendeAllgemein():
    """Seite für Studierende für die Einsicht der Modulnoten, sowie GPA 

    Tests:
        * Zeile in Tabelle anklicken
        * auf 'Passwort ändern' und 'Abmelden'-Button klicken
    """

    sg.theme('TanBlue')

    modul_information_array=[9308504, 'Programmieren', 5.0, 2.6, True ]

    headings=['Modul ID','Modul', 'Cedits', 'Note', 'best.']

    Buttons= [[sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))]]
    
    layout = [[sg.Text('Herzlich Willkommen!'), sg.Column(Buttons, element_justification='right', expand_x=True)],
            [sg.HorizontalSeparator()],
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
          
    Studi_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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
        * 'zurück'-Button klicken
        *
    """

    sg.theme('TanBlue')

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
            [sg.Text("Note " + Modul_Note)],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]
          
    window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))
    
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
        * Daten korrekt eingeben
        * Daten nicht korrekt eingeben
    """

    sg.theme('TanBlue')

    layout = [[sg.Text('Passwort ändern', font=('any', 12, 'bold'))],
          [sg.Text('Username *'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort *'), sg.InputText(key='-passwort-', do_not_clear=False)],
          [sg.Text('neues Passwort *'), sg.InputText(key='-neuesPasswort-', do_not_clear=False)],
          [sg.Text('Passwort wiederholen *'), sg.InputText(key='-wiPasswort-', do_not_clear=False)],
          [sg.Button('Ändern')]]

    Passwort_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))
    
    while True:
        event, values= Passwort_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Ändern":
            ÄnderungsDaten= values['-name-'], values['-passwort-'], values['-neuesPasswort-'], values['-wiPasswort-']
            Passwort_window.close()

    Passwort_window.close()


def PasswortAendernSeiteFalse():
    """Seite zum ändern des Passwortes nachdem Daten schon einmal falscch eingegeben wurden

    Tests:
        * Daten korrekt eingeben
        * Daten nicht korrekt eingeben
    """

    sg.theme('TanBlue')

    layout = [[sg.Text('Passwort ändern', font=('any', 12, 'bold'))],
          [sg.Text('Eine der Angaben ist nicht korrekt. Versuchen Sie es noch einmal!', text_color='red')],
          [sg.Text('Username *'), sg.InputText(key='-name-', do_not_clear=False)],
          [sg.Text('Passwort *'), sg.InputText(key='-passwort-', do_not_clear=False)],
          [sg.Text('neues Passwort *'), sg.InputText(key='-neuesPasswort-', do_not_clear=False)],
          [sg.Text('Passwort wiederholen *'), sg.InputText(key='-wiPasswort-', do_not_clear=False)],
          [sg.Button('Ändern')]]

    Passwort_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))
    
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
    * auf Zeile mit einer Veranstaltung klicken
    * auf 'Passwort ändern' und 'Abmelden'-Button klicken
    """

    sg.theme('TanBlue')

    Veranstaltung_array=[[239847, 'Statistik', 'BWL'],
                    [837945, 'Mathe', 'Informatik']]
    
    headings=['Veranstaltungs ID', 'Veranstaltungsname', 'Kurs']

    Buttons= [[sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))]]

    layout = [[sg.Text('Herzlich Willkommen!'), sg.Column(Buttons, element_justification='right', expand_x=True)],
            [sg.HorizontalSeparator()],
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
          
    Veran_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

    while True:
        event, values= Veran_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Passwort ändern":
            PasswortAendernSeite()
        elif event == "Abmelden":
            Veran_window.close()
            ErfolgreicherLogout()
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
    * Funktion von 'zurück'-Button testen
    *
    """

    sg.theme('TanBlue')

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
          
    Verankurs_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))
    
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
    * Daten korrekt in die Eingabefelder eintragen
    * Daten inkorrekt in die Eingabefelder eintragen
    """

    sg.theme('TanBlue')
    
    Bestanden= (True, False)
    Prüfungsinfo_Veranstaltung_Array= []

    layout = [[sg.Text('Veranstaltungsnoten eintragen', font=('any', 12, 'bold'))],
          [sg.Text('Veranstaltungs Id:'), sg.InputText(key= '-Veran_id-', do_not_clear=True)],
          [sg.Text('Matrikelnummer:'), sg.InputText(key='-Matrikelnummer-', do_not_clear=False)],
          [sg.Text('Punkte gesamt'), sg.InputText(key= '-Punkte_gesamt-', do_not_clear=True), sg.Text('Punkte erreicht'), sg.InputText(key= '-Punkte_erreicht-', do_not_clear=False)], 
          [sg.Text('Note'), sg.InputText(key= '-Note-', do_not_clear=False)],
          [sg.Text('Bestanden'), sg.Combo(Bestanden, enable_events=True, key='-Bestanden-')],
          [sg.Button('OK', font=('any', 9, 'underline'))]]
          
    VeranNoten_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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
    * Buttons für Studoerende, Dozierende, Kurse, Veranstaltungen und Module ausprobieren
    * auf 'Passwort ändern' und 'Abmelden'-Button klicken 
    """

    sg.theme('TanBlue')

    Buttons= [[sg.Button('Passwort ändern', font=('any', 9, 'underline')), sg.Button('Abmelden', font=('any', 9, 'underline'))]]

    AdminColumn = [
          [sg.Text('Was möchten Sie bearbeiten/ anlegen oder löschen?')],
          [sg.Button('Studierende', font=('any', 9, 'underline'), size=(15, 3)), sg.Button('Dozierende', font=('any', 9, 'underline'), size=(15, 3)), sg.Button('Kurse', font=('any', 9, 'underline'), size=(15, 3))],
          [sg.Button('Veranstaltung', font=('any', 9, 'underline'), size=(15, 3)), sg.Button('Modul', font=('any', 9, 'underline'), size=(15, 3))]]

    layout = [[sg.Text('Herzlich Willkommen!'), sg.Column(Buttons, element_justification='right', expand_x=True)],
            [sg.HorizontalSeparator()],
        [sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(AdminColumn, vertical_alignment='center', k='-C-')]]
          
    Admin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500), finalize=True)
    Admin_window['-C-'].expand(True, True, True)
    Admin_window['-1-'].expand(True, True, True)
    Admin_window['-2-'].expand(True, False, True)

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
    * Button für Studierenden neu anlegen anklicken
    * Studierenden ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    StudiAdminColumn = [[sg.Text('Studierenden Administration'), sg.Button('neuen Studierenden anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Studierenden ID:'), sg.InputText(key= '-studi_id-', do_not_clear=False, size=(20, 2)), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(StudiAdminColumn, vertical_alignment='center', justification='center',  k='-C-')]]
          
    Studiadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500), finalize=True)
    Studiadmin_window['-C-'].expand(True, True, True)
    Studiadmin_window['-1-'].expand(True, True, True)
    Studiadmin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values= Studiadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Studiadmin_window.close()
        elif event == 'neuen Studierenden anlegen':
            StudiAnlegen()
        elif event == 'bearbeiten':
            StudiBearbeiten(values['-studi_id-'])
        elif event == 'löschen':
            StudiLoeschen(values['-studi_id-'])
    
    Studiadmin_window.close()


def DozAdmin():
    """Einen Dozierenden bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Dozierenden neu anlegen anklicken
    * Dozierenden ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    DozAdminColumn = [[sg.Text('Dozierenden Administration'), sg.Button('neuen Dozierenden anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Dozierenden ID:'), sg.InputText(key= '-dozierenden_id-', do_not_clear=False, size=(20, 2)), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(DozAdminColumn, vertical_alignment='center', justification='center',  k='-C-')]]
          
    Dozadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500), finalize=True)
    Dozadmin_window['-C-'].expand(True, True, True)
    Dozadmin_window['-1-'].expand(True, True, True)
    Dozadmin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values= Dozadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Dozadmin_window.close()
        elif event == 'neuen Dozierenden anlegen':
            DozAnlegen()
        elif event == 'bearbeiten':
            DozBearbeiten(values['-dozierenden_id-'])
        elif event == 'löschen':
            break
    
    Dozadmin_window.close()



def KursAdmin():
    """Einen Kurs bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Kurs neu anlegen anklicken
    * Kurs ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    KursAdminColumn = [[sg.Text('Kurs Administration'), sg.Button('neuen Kurs anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Kurs ID:'), sg.InputText(key= '-kurs_id-', do_not_clear=False, size=(20, 2)), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(KursAdminColumn, vertical_alignment='center', justification='center',  k='-C-')]]
          
    Kursadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500), finalize=True)
    Kursadmin_window['-C-'].expand(True, True, True)
    Kursadmin_window['-1-'].expand(True, True, True)
    Kursadmin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values= Kursadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Kursadmin_window.close()
        elif event == 'neuen Kurs anlegen':
            KursAnlegen()
        elif event == 'bearbeiten':
            KursBearbeiten(values['-kurs_id-'])
        elif event == 'löschen':
            break
    
    Kursadmin_window.close()



def VeranstaltungAdmin():
    """Eine Veranstaltung bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Veranstaltung neu anlegen anklicken
    * Veranstaltung ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    VeranAdminColumn = [[sg.Text('Veranstaltung Administration'), sg.Button('neuen Veranstaltung anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Veranstaltung ID:'), sg.InputText(key= '-veranstaltung_id-', do_not_clear=False, size=(20, 2)), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(VeranAdminColumn, vertical_alignment='center', justification='center',  k='-C-')]]
          
    Veranadmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500), finalize=True)
    Veranadmin_window['-C-'].expand(True, True, True)
    Veranadmin_window['-1-'].expand(True, True, True)
    Veranadmin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values= Veranadmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Veranadmin_window.close()
        elif event == 'neuen Veranstaltung anlegen':
            VeranstaltungAnlegen()
        elif event == 'bearbeiten':
            VeranstaltungBearbeiten(values['-veranstaltung_id-'])
        elif event == 'löschen':
            break
    
    Veranadmin_window.close()



def main():
    """Einen Modul bearbeiten/ anlegen oder löschen

    Tests:
    * Button für Modul neu anlegen anklicken
    * Modul ID eingeben und bearbeiten/ löschen klicken
    """

    sg.theme('TanBlue')

    ModulAdminColumn = [[sg.Text('Modul Administration'), sg.Button('neuen Modul anlegen', font=('any', 9, 'underline'))],
            [sg.Text('Modul ID:'), sg.InputText(key= '-modul_id-', do_not_clear=False, size=(20, 2)), sg.Button('bearbeiten', font=('any', 9, 'underline')), sg.Button('löschen', font=('any', 9, 'underline'))],
            [sg.Button('zurück', font=('any', 9, 'underline'))]
          ]

    layout = [[sg.Text(key='-1-', font='ANY 1', pad=(0, 0))], 
              [sg.Text('', pad=(0,0),key='-2-'),              
               sg.Column(ModulAdminColumn, vertical_alignment='center', justification='center',  k='-C-')]]
          
    Moduladmin_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500), finalize=True)
    Moduladmin_window['-C-'].expand(True, True, True)
    Moduladmin_window['-1-'].expand(True, True, True)
    Moduladmin_window['-2-'].expand(True, False, True)
    
    while True:
        event, values= Moduladmin_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'zurück':
            Moduladmin_window.close()
        elif event == 'neuen Modul anlegen':
            ModulAnlegen()
        elif event == 'bearbeiten':
            ModulBearbeiten(values['-modul_id-'])
        elif event == 'löschen':
            sg.popup("hallo")
    
    Moduladmin_window.close()



def StudiAnlegen():
    """Einen neuen Studierenden anlegen

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
    
    Studierenden_Info_Array= []

    layout = [[sg.Text('Studierende anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Matrikelnummer: *'), sg.InputText(key='-Matrikelnummer-', do_not_clear=False)],
          [sg.Text('Nachname: *'), sg.InputText(key= '-Nachname-', do_not_clear=False)], 
          [sg.Text('Vorname: *'), sg.InputText(key= '-Vorname-', do_not_clear=False)],
          [sg.Text('Kurs ID: *'), sg.InputText(key= '-Kurs_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Studianle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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


def DozAnlegen():
    """Ein neuer Dozierender angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    Dozierenden_Info_Array= []

    layout = [[sg.Text('Dozierenden anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Dozierenden ID: *'), sg.InputText(key='-dozierenden_id-', do_not_clear=False)],
          [sg.Text('Nachname: *'), sg.InputText(key= '-Nachname-', do_not_clear=False)], 
          [sg.Text('Vorname: *'), sg.InputText(key= '-Vorname-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Dozanle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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



def KursAnlegen():
    """Ein neuer Kurs angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    Kurs_Info_Array= []

    layout = [[sg.Text('Kurs anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Kurs ID: *'), sg.InputText(key='-kurs_id-', do_not_clear=False)],
          [sg.Text('Kurs Name: *'), sg.InputText(key= '-kurs_name-', do_not_clear=False)], 
          [sg.Text('Dozierenden ID: *'), sg.InputText(key= '-dozierenden_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Kursanle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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



def VeranstaltungAnlegen():
    """Eine neue Veranstaltung angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    Veran_Info_Array= []

    layout = [[sg.Text('Veranstaltung anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Veranstaltung ID: *'), sg.InputText(key='-Veranstaltung_id-', do_not_clear=False)],
          [sg.Text('Veranstaltungsname: *'), sg.InputText(key= '-veranstaltungsname-', do_not_clear=False)], 
          [sg.Text('Dozierenden ID: *'), sg.InputText(key= '-dozierenden_id-', do_not_clear=False)],
          [sg.Text('Modul ID: *'), sg.InputText(key= '-modul_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Verananle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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



def ModulAnlegen():
    """Ein neues Modul angelegt

    Tests:
        * Daten korrekt/ inkorrekt in Eingabefelder eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')

    Modul_Info_Array= []

    layout = [[sg.Text('Modul anlegen', font=('any', 12, 'bold'))],
          [sg.Text('Modul ID: *'), sg.InputText(key='-modul_id-', do_not_clear=False)],
          [sg.Text('Modulname: *'), sg.InputText(key= '-modulname-', do_not_clear=False)], 
          [sg.Text('Kurs ID: *'), sg.InputText(key= '-kurs_id-', do_not_clear=False)],
          [sg.Text('Credits: *'), sg.InputText(key= '-credits-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Modulanle_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

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



def StudiBearbeiten(studi_id: int):
    """Informationen über einen Studierenden können verändert werden 

    Args:
        studi_id (int): Studierenden ID

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
    
    Studi= [839287, 'Vor', 'nach', 2384789]

    Studi_Info_Array= []

    layout = [[sg.Text('Studierenden bearbeiten', font=('any', 12, 'bold'))],
          [sg.Text('Studierenden ID:'), sg.Text(Studi[0]), sg.InputText(key='-studi_id-', do_not_clear=False)],
          [sg.Text('Vorname:'), sg.Text(Studi[1]), sg.InputText(key= '-vorname-', do_not_clear=False)], 
          [sg.Text('Nachname:'), sg.Text(Studi[2]), sg.InputText(key= '-nachname-', do_not_clear=False)],
          [sg.Text('Kurs ID:'), sg.Text(Studi[3]), sg.InputText(key= '-kurs_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Studibear_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

    while True:
        event, values= Studibear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            StudiInfo= Studi[0], values['-studi_id-'], values['-vorname-'], 
            values['-nachname-'], values['-kurs_id-']
            Studi_Info_Array.append(StudiInfo)
        elif event == 'zurück':
            break

    Studibear_window.close()



def DozBearbeiten(Dozierenden_id: int):
    """Informationen über einen Dozendierenden können verändert werden 

    Args:
        Dozierenden_id (int): Dozierenden ID

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
    
    Doz= [839287, 'Vor', 'nach']

    Doz_Info_Array= []

    layout = [[sg.Text('Dozierenden bearbeiten', font=('any', 12, 'bold'))],
          [sg.Text('Dozierenden ID:'), sg.Text(Doz[0]), sg.InputText(key='-doz_id-', do_not_clear=False)],
          [sg.Text('Nachname:'), sg.Text(Doz[1]), sg.InputText(key= '-nachname-', do_not_clear=False)], 
          [sg.Text('Vorname:'), sg.Text(Doz[2]), sg.InputText(key= '-vorname-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Dozbear_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

    while True:
        event, values= Dozbear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            DozInfo= Doz[0], values['-doz_id-'], values['-nachname-'], 
            values['-vorname-']
            Doz_Info_Array.append(DozInfo)
        elif event == 'zurück':
            break

    Dozbear_window.close()


def KursBearbeiten(Kurs_id :int):
    """Informationen über einen Kurs können verändert werden 

    Args:
        Kurs_id (int): Kurs ID

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
        
    Kurs= [839287, 'Vor', 'nach', 2384789]

    Kurs_Info_Array= []

    layout = [[sg.Text('Kurs bearbeiten', font=('any', 12, 'bold'))],
          [sg.Text('Kurs ID:'), sg.Text(Kurs[0]), sg.InputText(key='-kurs_id-', do_not_clear=False)],
          [sg.Text('Kursname:'), sg.Text(Kurs[1]), sg.InputText(key= '-kursname-', do_not_clear=False)], 
          [sg.Text('Dozierenden ID:'), sg.Text(Kurs[2]), sg.InputText(key= '-doz_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Kursbear_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

    while True:
        event, values= Kursbear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            KursInfo= Kurs[0], values['-kurs_id-'], values['-kursname-'], 
            values['-doz_id-']
            Kurs_Info_Array.append(KursInfo)
        elif event == 'zurück':
            break

    Kursbear_window.close()


def VeranstaltungBearbeiten(Veran_id: int):
    """Informationen über eine Veranstaltung können verändert werden 

    Args:
        Veran_id (int): Veranstaltung ID

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
        
    Veran= [839287, 'Vor', 'nach', 2384789]

    Veran_Info_Array= []

    layout = [[sg.Text('Veranstaltung bearbeiten', font=('any', 12, 'bold'))],
          [sg.Text('Veranstaltungs ID:'), sg.Text(Veran[0]), sg.InputText(key='-veran_id-', do_not_clear=False)],
          [sg.Text('Veranstaltungsname:'), sg.Text(Veran[1]), sg.InputText(key= '-veranname-', do_not_clear=False)], 
          [sg.Text('Dozierenden ID:'), sg.Text(Veran[2]), sg.InputText(key= '-doz_id-', do_not_clear=False)],
          [sg.Text('Modul ID:'), sg.Text(Veran[3]), sg.InputText(key= '-modul_id-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Veranbear_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

    while True:
        event, values= Veranbear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            VeranInfo= Veran[0], values['-veran_id-'], values['-veranname-'], 
            values['-doz_id-'], values['-modul_id-']
            Veran_Info_Array.append(VeranInfo)
        elif event == 'zurück':
            break

    Veranbear_window.close()



def ModulBearbeiten(Modul_id: int):
    """Die Informationen eines Moduls können verändert werden

    Args:
        Modul_id (int): Modul ID

    Tests:
        * hinter die falsche Information die Änderung in das Inputfeld eintragen
        * 'zurück'-Button anklicken
    """

    sg.theme('TanBlue')
        
    Modul= [839287, 'Vor', 'nach', 2384789]

    Modul_Info_Array= []

    layout = [[sg.Text('Modul bearbeiten', font=('any', 12, 'bold'))],
          [sg.Text('Modul ID:'), sg.Text(Modul[0]), sg.InputText(key='-modul_id-', do_not_clear=False)],
          [sg.Text('Modulname:'), sg.Text(Modul[1]), sg.InputText(key= '-modulname-', do_not_clear=False)], 
          [sg.Text('Kurs ID:'), sg.Text(Modul[2]), sg.InputText(key= '-kurs_id-', do_not_clear=False)],
          [sg.Text('Credits:'), sg.Text(Modul[3]), sg.InputText(key= '-credits-', do_not_clear=False)],
          [sg.Button('OK', font=('any', 9, 'underline')), sg.Button('zurück', font=('any', 9, 'underline'))]]
          
    Modulbear_window=sg.Window('Studierendenverwaltungssystem', layout, modal=True, size=(500, 500))

    while True:
        event, values= Modulbear_window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "OK":
            ModulInfo= Modul[0], values['-modul_id-'], values['-modulname-'], 
            values['-kurs_id-'], values['-credits-']
            Modul_Info_Array.append(ModulInfo)
        elif event == 'zurück':
            break

    Modulbear_window.close()



def StudiLoeschen(studi_id: int):
    """ den Studieren mit der angegebenen ID löschen

    Args:
        studi_id (int): Studierenden ID
    """

    print()



def DozLoeschen(doz_id: int):
    """ den Dozierenden mit angegebenen ID löschen

    Args:
        doz_id (int): Dozierenden ID
    """

    print()



def KursLoescchen(kurs_id: int):
    """den Kurs mit angegebenen ID löschen

    Args:
        kurs_id (int): Kurs ID
    """

    print()



def VeranstaltungLoeschen(veran_id: int):
    """den Veranstaltung mit angegebenen ID löschen

    Args:
        veran_id (int): Veranstaltung ID
    """

    print()



def ModulLoeschen(modul_id: int):
    """den Modul mit angegebenen ID löschen

    Args:
        modul_id (int): Modul ID
    """

    print()

    


if __name__ == "__main__":
    main()


