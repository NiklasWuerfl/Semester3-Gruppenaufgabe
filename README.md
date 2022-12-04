Emanuel Forderer, Daniela Mayer, Emma Müller, Niklas Würfl

# Anleitung zum Programmstart

    1) Installation von Modulen 
        * Flask
        * PySimpleGui
        * sqllite3
    
    2) Start des Programms
        * app.py ausführen
        * Frondend.py ausführen

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

    Die gesamten Beispieldaten, die in der Datenbank hinterlegt sind, können in "Database_setup.txt" eingesehen werden.
    Eine Veranstaltung kann als Vorlesungs-Veranstaltung interpretiert werden. Die zusammenhängenden Fremdschlüssel und sonstige Beziehungen können in der Datei "database.py" eingesehen werden.

# Weitere Informationen

    1) Es kann zwischendurch, besonders nach dem Studenten-Login zu längeren Ladezeiten kommen. In diesem Fall ist nichts zu sehen. 
       Das Programm nicht abgestürzt, sondern lädt im Hintergrund.

    2) Die Dateninkosistenzen können auftreten, weil verschiedene Entitäten zusammenhängen. Beim Löschen hat die Funktion DELETE CASCADE nicht funktioniert, 
       daher können Fremdschlüssel auf nichtmehr existete oder veraltete Primärschlüssel verweisen.

    3) Bei der Studenten-Ansicht und der Dozenten-Ansicht können Details zu den Daten bei Klick auf die Zeilen angezeigt werden.

    
# Mögliche Erweiterungen:
    Aus Zeitmangel und weil wir im Laufe des Projektes ein Gruppenmitglied verloren haben, konnten wir nicht alle unsere Ideen umsetzen.
    Daher haben wir folgende Ideen wie unser Projekt noch weiter optimiert werden könnte:
        * Passwortverschlüsselung
        * User-Tracking und Zugriffsicherung
        * Schnittstellenverbesserung und Performance-Verbesserung
        * Exception-Handling: es ist nicht komfortabel, dass das Programm bei einer Exception vollständig abstürzt
        * GUI Optimierung, Fenster-vergrößerung, intuitiveres Handling