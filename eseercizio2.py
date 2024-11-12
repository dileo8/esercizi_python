tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico", 210)),
        ("marzo", ("gas", 110)),
        ("aprile", ("elettrico", 230)),
        ("aprile", ("gas", 140))
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico", 200)),
        ("marzo", ("gas", 100)),
        ("aprile", ("elettrico", 210)),
        ("aprile", ("gas", 120))
    ]),

    ("Como", [
        ("gennaio", ("elettrico", 240)),
        ("gennaio", ("gas", 180)),
        ("febbraio", ("elettrico", 200)),
        ("febbraio", ("gas", 190)),
        ("marzo", ("elettrico", 230)),
        ("marzo", ("gas", 190)),
        ("aprile", ("elettrico", 210)),
        ("aprile", ("gas", 110))
    ]),
)
while True:
    nomeCitta = str(input("inserire il nome della città: "))
    nomeRisorsa = str(input("inserire il nome della risorsa energetica: "))
    if nomeCitta or nomeRisorsa not in tupla_consumi_energetici:
          print("ERRORE NELL'INSERIMENTO")
    else:
          break
    
def analizza_consumi_energetici(tupla_consumi_energetici, nomeCitta, nomeRisorsa):
    #media
    somma = 0
    i = 0
    
    for citta, gruppo1 in tupla_consumi_energetici:
        if citta == nomeCitta:
               for mese, (risorsa, dato) in gruppo1:
                    if risorsa == nomeRisorsa:
                        somma+=dato
                        i+=1
    media = somma/i

    #max
    max_risorsa = 0
    mese_max_risorsa = []

    for citta, gruppo1 in tupla_consumi_energetici:
                if citta == nomeCitta:
                    for mese, (risorsa, dato) in gruppo1:
                        if risorsa == nomeRisorsa:
                              if max_risorsa < dato:
                                    max_risorsa = dato

    for citta, gruppo1 in tupla_consumi_energetici:
            if citta == nomeCitta:
                for mese, (risorsa, dato) in gruppo1:
                    if risorsa == nomeRisorsa:
                            if dato == max_risorsa:
                                mese_max_risorsa.append(mese)

    return (media, (max_risorsa, mese_max_risorsa))

print(analizza_consumi_energetici(tupla_consumi_energetici,nomeCitta, nomeRisorsa))

