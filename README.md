# ImageRepair
# Entwicklung einer Applikation zur Erkennung und Bearbeitung fehlerhafter Bilder
_Studienarbeit_
<table>
<tr><th>Autor</th><td>Elvira Kraft (3653393)</td></tr>
<tr><th>Autor</th><td>Cassandra Schilling (5919209)</td></tr>
<tr><th>Betreuer</th><td>M.Sc. Jonas Fritzsch, DHBW Stuttgart</td></tr>
<tr><th>Studiengang/Kurs</th><td>B. Sc. Informatik TINF19D</td></tr>
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
1) Quellcode zur Studienarbeit.
2) Ordner "Beispiele", der beschädigte Beispielbilder enthält.
3) Studienarbeit als PDF Datei


## Installation

1) Python und Pip installieren
    1) Python 3.6 [herunterladen](https://www.python.org/downloads/) und installieren (beinhaltet pip)
2) Virtual Environment erstellen mit allen in der Datei ``requirements.txt`` genannten Modulen
    1) Das Modul "Virtual Environment" installieren mit ``pip install virtualenv``
    2) Neue virtuelle Umgebung im Projektordner erstellen mit ``virtualenv venv``
    3) Virtuelle Umgebung betreten, indem im Ordner ``venv/Scripts/`` ausgeführt wird: 
        1) Unix (Bash): ``.\activate``
        2) Windows (PowerShell): ``PowerShell.exe -ExecutionPolicy UNRESTRICTED`` und ``.\Activate.ps1``
    4) Module in virtuelle Umgebung installieren mit ``pip install -r requirements.txt``
3) Die Bibliothek ```pafprocess``` kompilieren
    1) Compiler SWIG installieren
        1) Unix: ``sudo apt install swig``
        2) Windows:
            1) SWIG herunterladen und Installieren [Download](http://www.swig.org/download.html)
            2) Visual C++ Build Tools von Microsoft installieren via [Direktlink](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15) oder [Download-Website besuchen](https://visualstudio.microsoft.com/downloads), "Tools für Visual Studio 2017" auswählen und bei "Build Tools für Visual Studio 2017" auf "Herunterladen" drücken
    1) Im Ordner ``tpe/tf_pose/pafprocess`` die Befehle ``swig -python -c++ pafprocess.i`` und ``python setup.py build_ext --inplace`` ausführen.


## Nutzung der Anwendung

1) .exe Datei öffnen
2) Pfad für Quellordner (Beispielordner aus dem Repository) und Zielordner einfügen
3) Auf den Startknopf drücken
4) Profit


## Kontakt
E-Mail: [alexander@melde.net](alexander@melde.net)
E-Mail: [alexander@melde.net](alexander@melde.net)
