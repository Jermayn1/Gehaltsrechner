# Hier importieren wir Sachen aus anderen Dateien
from berechnungen.kirchensteuer import berechne_kirchensteuer
from berechnungen.lohnsteuer import finde_lohnsteuerlast
from berechnungen.kinderfreibetrag import berechne_kinderfreibetrag


# Eingabe (lagern wir später auch aus)
alter = 0
bruttogehalt = 0
ist_privat_versichert = False
bundesland = ""
ist_in_kirche = False
steuerklasse = 1
hat_kinder = False
anzahl_kinder = 0



# Eingabe Alter
while True:
    e = int(input("Wie alt sind Sie? "))
    if (e > 0):
        alter = e
        break
    print("Ungültige Eingabe!")

# Eingabe Brutto
while True:
    e = int(input("Bitte geben Sie ihr Bruttogehalt ein: "))
    if isinstance(e, int): # prüft ob es ein integer ist
        if e > 0:
            bruttogehalt = e; # speichert das Gehalt in der variable
            break;
    print("Ungültige Eingabe!")

# Eingabe Versicherung
while True:
    e = bool(input("Sind sie privat versichert? (True/False)"))
    if isinstance(e, bool):
        ist_privat_versichert = e;
        break;
    print("Ungültige Eingabe!")

# Eingabe Bundesland (Hier später noch die Eingabe validieren)
while True:
    e = input("Aus welchen Bundesland kommen Sie?")
    bundesland = e
    break

# Eingabe Kirchenmitglied
while True:
    e = bool(input("Sind Sie in der Kirche? (True/False)"))
    ist_in_kirche = e
    break
    
# Eingabe Steurklasse (Hier auch wieder später validieren)
while True:
    e = int(input("In welcher Steuerklasse sind Sie?"))
    if e > 0 and e < 7:
        steuerklasse = e
        break
    print("Ungültige Eingabe!")
    
# Eingabe Hat Kinder
while True:
    e = bool(input("Hat haben Sie Kinder? (True/False)"))
    hat_kinder = e;
    break
    
# Eingabe Kinder (wenn Kinder vorhanden)
while True and hat_kinder:
    e = int(input("Geben Sie die Anzahl Ihrer Kinder ein:"))
    if e > 0:
        anzahl_kinder = e;
        break;
    print("Ungültige Eingabe!")
    
    
    
# Hier testen

# Berechnung Lohnsteuer
lst = finde_lohnsteuerlast(bruttogehalt, steuerklasse)
print(f"LST: {lst}") # Siehe Chat in Teams wegen Ausgabe mit Print

# Berechnung Kirchensteuer
kst = 0
if ist_in_kirche:
    kst = berechne_kirchensteuer(lst, bundesland)
    
# Berechnung Kinderfreibetrag
kinderfreibetrag = 0
if hat_kinder:
    kinderfreibetrag = berechne_kinderfreibetrag(anzahl_kinder)
    
    
    
kirchensteuer_str = input("askjhdgakshjdgf")
kirchensteuer = False
if (kirchensteuer_str == "ja"): kirchensteuer = True