# Immer für ein Kind
KINDERFREIBETRAG_PRO_JAHR = 3414 # Jahr 2026 https://www.vlh.de/wissen-service/steuer-abc/wie-funktioniert-das-mit-dem-kinderfreibetrag.html#c2006
KINDERFREIBETRAG_PRO_MONAT = KINDERFREIBETRAG_PRO_JAHR / 12

def berechne_kinderfreibetrag(anzahl_kinder):
    # Betrag pro Kind * Anzahl der Kinder = Kinderfreibetrag
    return KINDERFREIBETRAG_PRO_MONAT * anzahl_kinder