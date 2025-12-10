def ermittel_kirchensteuersatz(bundesland):
    if bundesland == "Bayern":
        return 0.08;
    return 0.09;


# Formel zur Berechnung
# KSt = ESt/LSt × 8 % oder 9 %
def berechne_kirchensteuer(lohnsteuer, bundesland):
    kirchensteuersatz = ermittel_kirchensteuersatz(bundesland)
    return lohnsteuer * kirchensteuersatz