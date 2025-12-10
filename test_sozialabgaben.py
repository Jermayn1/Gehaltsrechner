from berechnungen.sozialabgabe import *

bruttoeinkommen = 2000
anzahl_kinder = 2
alter = 23
bundesland = "NRW"

satz = ermittel_pflegeversicherungssatz(anzahl_kinder, alter, bundesland)
print("Satz:", satz)

pflegeversicherungbeitrag = berechne_pflegeversicherungsbeitrag(bruttoeinkommen, anzahl_kinder, alter, bundesland) / 2
print("Beitrag:", pflegeversicherungbeitrag)