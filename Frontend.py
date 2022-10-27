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
    
    layout = [[sg.Text('Username:'), sg.InputText()],
          [sg.Text('Passwort:'), sg.InputText()],
          [sg.Button('Anmelden')]]

    window=sg.Window('Login Seite', layout)

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()

def FalseLoginSeite():
    """Implimentierung der Seite nach falschem einloggen

        Tests:
        *
        *
    """
    
    layout = [[sg.Text('Username oder Passwort falsch', text_color= 'red')],
        [sg.Text('Username:'), sg.InputText()],
        [sg.Text('Passwort:'), sg.InputText()],
        [sg.Button('Anmelden')],
        [sg.Text('Falls Sie das Passwort vergessen haben, wenden Sie sich an den Administrator!')]]

    window=sg.Window('Login Seite', layout)

    while True:
        event, values= window.read()
        if event == sg.WIN_CLOSED:
            break

    window.close()
          