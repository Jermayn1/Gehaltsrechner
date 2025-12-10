from berechnungen.lohnsteuer import finde_lohnsteuerlast
from berechnungen.kirchensteuer import berechne_kirchensteuer
from berechnungen.kinderfreibetrag import berechne_kinderfreibetrag

bruttogehalt = 6501
ist_privat_versichert = False
bundesland = "Bayern"
steuerklasse = 1
hat_kinder = True
anzahl_kinder = 3


lst = finde_lohnsteuerlast(bruttogehalt, steuerklasse)
print(lst)
kirchst = berechne_kirchensteuer(lst, bundesland)
print(kirchst)


kinderfreibetrag = berechne_kinderfreibetrag(anzahl_kinder)
print(kinderfreibetrag)
# 0 Kinder = 0
# 1 Kind = 284,5
# 2 Kinder = 569
# 3 Kinder = 853,5
