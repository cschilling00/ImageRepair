# ImageRepair
# Entwicklung einer Applikation zur Erkennung und Bearbeitung fehlerhafter Bilder
_Studienarbeit_
<table>
<tr><th>Autorin</th><td>Elvira Kraft (3653393)</td></tr>
<tr><th>Autorin</th><td>Cassandra Schilling (5919209)</td></tr>
<tr><th>Betreuer</th><td>M.Sc. Jonas Fritzsch, DHBW Stuttgart</td></tr>
<tr><th>Studiengang/Kurs</th><td>Informatik/ TINF19D</td></tr>
<tr><th>Titel der Arbeit</th><td>Entwicklung einer Applikation zur Erkennung und Bearbeitung fehlerhafter Bilder</td></tr>
<tr><th>Anlass</th><td>Studienarbeit, 3. Studienjahr</td></tr>
<tr><th>Bearbeitungszeitraum</th><td>26.09.2021 - 10.06.2022</td></tr>
<tr><th>Abgabedatum</th><td>10.06.2022</td></tr>
</table>

## Kurzbeschreibung
> Nach der erfolgreichen Datenrettung von defekten Datenträgern stellt man häufig fest, dass die
Daten irreparabel beschädigt sind. Grund dafür sind häufig Speichersektoren, die durch einen Defekt
oder eine schlechte Verbindung nicht mehr auslesbar sind. Besonders bei Bildern ist dies durch eine
Veränderung an deren Struktur oder Farbe zu erkennen.
> 
> In dieser Arbeit soll eine Anwendung entwickelt werden, die eine größere Menge solcher Bilder einliest, analysiert und die als korrupt erkannten Bereiche entfernt.
> 
> Der Entwicklung der Anwendung ging eine ausführliche Untersuchung verschiedener Bibliotheken zur Bildverarbeitung sowie einer geeigneten Programmiersprache voraus. Die Bibliothek OpenCV verfügt über ein großes Set an Features und ist in den Sprachen Java, C++ und Python anwendbar. Als Sprache wurde Python ausgewählt.
> 
> Es wurden verschiedene Algorithmen zur Segmentierung und Textanalyse näher untersucht, auf deren Grundlage die Anwendung entwickelt wurde.
> 
> Die Anwendung erkennt Graubereiche und gestreifte Bereiche sowie andere einfarbige Bereiche. 

## Veröffentlichung
Der im Rahmen der Studienarbeit geschriebene Quelltext wurde in diesem GitHub Repository veröffentlicht.

Zur Dokumentation des Codes wurde auch der schriftliche Teil der Studienarbeit hier hochgeladen.

**Inhalt dieses Repository:**
1) Schriftliche Ausarbeitung als PDF
2) Ordner "Beispielbilder", der beschädigte Beispielbilder enthält
3) Quellcode zur Anwendung ImageRepair
4) Ordner "dist", der eine .exe Datei enthält


## Code lokal starten

1) Python und Pip installieren
    1) Python 3.10 [herunterladen](https://www.python.org/downloads/) und installieren (beinhaltet pip)
2) Alle benötigten Module installieren (Numpy, OpenCV, PyQt5)
3) im Projektordner das Terminal öffnen und den Befehl 'python ./Gui.py' eingeben


## Nutzung der Anwendung

1) dist Ordner herunterladen und entpacken
2) Gui.exe Datei öffnen
3) Pfad für Quellordner (z.B. Beispielordner aus dem Repository) und Zielordner eingeben (Pfad darf keine Umlaute oder Sonderzeichen enthalten!)
4) Auf den Startknopf drücken

## Kontakt
E-Mail: [Email Kraft](elvirakraft@yahoo.de), [Email Schilling](cassandras00@aol.com)
