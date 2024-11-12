tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

def media_gol_partite(tupla_partite):
    vVoto1 = []
    vVoto2 = []
    i = 0
    for squadra1, squadra2, risultato1, risultato2 in tupla_partite:
        vVoto1.append(risultato1)
        vVoto2.append(risultato2)
        i+=2

    somma = sum(vVoto1)+sum(vVoto2)
    media = somma/i
    print("media totale = ", media)
media_gol_partite(tupla_partite)

squadra = str(input("inserire il nome della squadra: "))

def partita_con_piu_gol(tupla_partite):
    vSomma1 = []
    vSomma2 = []
    i =0
    for squadra1, squadra2, risultato1, risultato2 in tupla_partite:
        if squadra == squadra1:
            vSomma1.append(risultato1)
            i+=1
        elif squadra == squadra2:
            vSomma2.append(risultato2)
            i+=1
    somma1 = sum(vSomma1)
    somma2 = sum(vSomma2)
    sommaTot = somma1+somma2
    media = sommaTot/i
    print(media)
partita_con_piu_gol(tupla_partite)

def partita_con_meno_gol(tupla_partite):
    vSomma1 = []
    vSomma2 = []
    i =0
    for squadra1, squadra2, risultato1, risultato2 in tupla_partite:
        if squadra == squadra1:
            vSomma1.append(risultato1)
            i+=1
        elif squadra == squadra2:
            vSomma2.append(risultato2)
            i+=1
    somma1 = sum(vSomma1)
    somma2 = sum(vSomma2)
    sommaTot = somma1+somma2
    media = sommaTot/i
    print(media)
partita_con_piu_gol(tupla_partite)
        