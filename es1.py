dati = (
            ("milano", [("gennaio", 8), ("febbraio", 10), ("marzo", 9), ("aprile", 11), 
                        ("maggio", 11), ("giugno", 11), ("luglio", 11), ("agosto", 0), 
                        ("settembre", 11), ("ottobre", 11), ("novembre", 11), ("dicembre", 11)]),
            ("como", [("gennaio", 10), ("febbraio", 6), ("marzo", 9), ("aprile", 12), 
                        ("maggio", 8), ("giugno", 0), ("luglio", 7), ("agosto", 10), 
                        ("settembre", 8), ("ottobre", 13), ("novembre", 7), ("dicembre", 11)]),
            ("monza", [("gennaio", 8), ("febbraio", 12), ("marzo", 1), ("aprile", 10), 
                        ("maggio", 11), ("giugno", 9), ("luglio", 8), ("agosto", 7), 
                        ("settembre", 10), ("ottobre", 11), ("novembre", 4), ("dicembre", 0)])
        )

nome = print(input("Inserisci nome della città: "))

def media_dati(nome):
    max = 0
    min = 100
    somma = 0
    i = 0

    for citta, meseDato in dati:
        if citta == nome:
            for mese, dato in meseDato:
                somma = somma + dato
                i+=1
    
    for citta, *meseDato in dati:
        if citta == nome:
            for mese, dato in meseDato:
                if dato > max:
                    max = dato
                    meseMax = mese
            
                elif dato < min:
                    min = dato
                    meseMin = mese
                
    media = somma/i
    return (media, (max, meseMax), (min, meseMin))
    
print(media_dati(nome))
    
        
        
        
    
