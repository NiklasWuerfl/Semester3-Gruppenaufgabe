Emanuel Forderer, Daniela Mayer, Emma Müller, Niklas Würfl

# Anleitung zum Programmstart

    1) Installation von Modulen 
        * Flask
        * PySimpleGui
        * sqllite3
    
    2) Start des Programms
        * app.py starten
        * Frondend.py starten

# Vorhandene Nutzer
    In unserem System gibt es drei verschiedene Arten von Nutzern (Student, Dozent, Admin). Vor dem Login muss die 
    jeweilige Rolle ausgewählt werden und dann die jeweiligen Logindaten eingegeben werden.

    Zugangsdaten:
        1) Student ID: 1000
              Vorname: Max
             Nachname: Mustermann
             Passwort: passwort

        2) Dozent ID: 120
             Vorname: Sebastian
            Nachname: Fichtner
            Passwort: FICHTNERsebastian

        3) Admin ID: 99
            Vorname: Power
           Nachname: Admin
           Passwort: AdminPW

# Weitere Informationen

    1) Es kann zwischendurch zu längeren Ladezeiten kommen. In diesem Fall ist nichts zu sehen. 
       Das Programm nicht abgestürzt, sondern läd im Hintergrund.

    2) Es kam zu einem Fehler in einer Funktion für die Datenabfrage. Daher können die Daten für Dozenten nicht visualisiert werden. 
       Derzeit sind Platzhalterdaten eingesetzt um die Funktionalität zu veranschaulichen. Diese sind allerdings für alle Dozenten gleich und hängen nicht mit der Datenbank zusammen.

    3) Die Dateninkosistenzen können auftreten, weil verschiedene Entitäten zusammenhängen. Beim Löschen hat die Funktion DELETE CASCADE nicht funktioniert, 
       daher können Fremdschlüssel auf nichtmehr existete oder veraltete Primärschlüssel verweisen.

    

# Semester3-Gruppenaufgabe
Noten werden gespeichert und ausgewertet

TO DO:
- gleiche variablenbennenung über module
- PEP 8 Richtlinien
- Test je 2 pro Funktion
- notwendige Imports, ...
- Anleitung zum starten
- Dateninkonsistenzen: CASCADE in SQL-Befehle einbauen
- optional: mögliche Erweiterungen für Programm

-> PEP 8 Richtlinien: https://legacy.python.org/dev/peps/pep-0008/#function-and-method-arguments
