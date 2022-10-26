"""
    Modul zur Modellierung des Frontends
    Verwaltet welche Programmseiten angezeigt werden und nimmt Nutzerinteraktionen an, die an die REST API weitergegeben werden
    Macht entsprechende Anfragen an API/Backend und zeigt die erhaltenen "Ergebnisse" für den Nutzer an

    mögliche Module:
        * Streamlit
        * Tkinter
        * SimpleGUI
        * Django

    benötigte Funktionen:
        * Anmeldungsfenster
        * einheitliche Startseite? Anzeige der verschiedenen Funktionen auf Grundlage der Rolle
        * Studenten: Übersicht der eigenen Module, Noten und Credits
        * Dozenten: Übersicht der Kurse und Vorlesungen (Durchschnitte?)
        * Admin: Organisationsstruktur der angelegten User?
        generell: API Kommunikation

    außerdem könnten wir hier ein EasterEgg einbauen -> Kreativitätspunkte

    author:
    date: 26.10.2022
    version: 1.0.0
    licence: free (open source)
"""
import PySimpleGUI as psg
