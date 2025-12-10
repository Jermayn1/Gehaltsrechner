# https://www.bundesgesundheitsministerium.de/themen/pflege/online-ratgeber-pflege/die-pflegeversicherung/finanzierung.html

# Formel und Sätze (Stand 2025)
# Allgemeiner Satz (mit Kindern): 3,6 % des Bruttoeinkommens (Arbeitnehmeranteil 1,8 %, Arbeitgeberanteil 1,8 %).
# Kinderlose (ab 23 Jahren): 4,2 % des Bruttoeinkommens (3,6 % + 0,6 % Zuschlag).
# Abschlag für Kinder: Für das 2. bis 5. Kind unter 25 Jahren gibt es einen Abschlag vom Arbeitnehmeranteil.
# Arbeitgeberanteil: Zahlt 1,8 % (in Sachsen 1,3 %), unabhängig von der Kinderzahl.

# 3,6% Allg. Satz (ohne Kinder)
ALLGEMEINERSATZ = 0.036 # Allgemeiner Beitragssatz (ohne Kinder): 3,6 % des Bruttolohns, wovon der Arbeitnehmer 1,8 % zahlt. 


def ermittel_pflegeversicherungssatz(anzahl_kinder, alter, bundesland):
    satz = ALLGEMEINERSATZ
    # Fall Sachsen 🥲 machen wir später
    if bundesland == "Sachsen":
        return 0
    # Alle anderen Bundesländer
    else:
        # Bereinigung vom Satz durch Kinder
        if anzahl_kinder > 0:
            match anzahl_kinder:
                case 1:
                    satz = 0.036 # Lebenslang
                case 2:
                    satz = 0.035 # 3,35 % (Arbeitnehmer-Anteil: 1,55 %)
                case 3:
                    satz = 0.031 # 3,10 % (Arbeitnehmer-Anteil: 1,3 %) 
                case 4:
                    satz = 0.0285 # 2,85 % (Arbeitnehmer-Anteil: 1,05 %)
                case _: # wie default (ab und mehr als 5 Kinder)
                    satz = 0.026 #2,60 % (Arbeitnehmer-Anteil: 0,8 %)
        
        # Zuschlag ab 23 Jahren und keine Kinder
        if anzahl_kinder <= 0 and alter >= 23:
            satz += 0.006 # 0,6% Kinderlosenzuschalg
            
            
    return satz
        
            

# Berechnung Pflegeversicherung
def berechne_pflegeversicherungsbeitrag(bruttoeinkommen, anzahl_kinder, alter, bundesland):
    # Formel: Bruttoeinkommen x Beitragssatz = Pflegeversicherungsbeitrag
    return bruttoeinkommen * ermittel_pflegeversicherungssatz(anzahl_kinder, alter, bundesland)