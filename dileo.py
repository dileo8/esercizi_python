lista1 = [("antipasti", (8,7,9), "junior"), ("primi", (7,8,8), "junior"), ("secondi", (9,9,8), "junior"), ("dessert", (8,8,9), "junior")]
lista2 = [("antipasti", (7,7,8), "senior"), ("primi", (8,9,7), "senior"), ("secondi", (7,8,7), "senior"), ("dessert", (9,8,8), "senior")]
lista3 = [("antipasti", (9,8,8), "junior"), ("primi", (8,7,9), "junior"), ("secondi", (8,8,8), "junior"), ("dessert", (7,9,8), "junior")]

dizionario = {
    "mario rossi": lista1,
    "luigi bianchi": lista2,
    "giulia verdi": lista3
}

#es2 fatto
def aggiungiChef():
    dizionario["cristian di leo"] = [("antipasti", (8,8,8), "junior"), ("primi", (6,8,9), "junior"), ("secondi", (7,9,8), "junior"), ("dessert", (8,8,9), "junior")]
    print(dizionario)

#es3
def aggiungiPiatto():
    for chiave, lista in dizionario.items():
        print(lista)
        for piatto, *voti, categoria in lista:
            categoria = str(input("Inserire categoria: "))
            for voto1, voto2, voto3 in voti:
                voto1 = int(input("Inserire primo voto: "))
                voto2 = int(input("Inserire secondo voto: "))
                voto3 = int(input("Inserire terzo voto: "))
        lista.append("piatti unici", (voto1,voto2,voto3), categoria)
    print(dizionario)
    


#es 4 fatto
def stampaChef():
    while True:
        nome = str(input("Inserire nome e cognome dello chef: "))
        if nome not in dizionario.keys():
            print("Errore, nome dello chef non presente!")
        else:
            for chiave, lista in dizionario.items():
                if nome == chiave:
                    print("nome e cognome: ", chiave)
                    for piatto, *voti, categoria in lista:
                        print("categoria: ", categoria)
                        print("PUNTEGGI ANTIPASTI = ")
                        for cretivita, gusto, presentazione in voti:
                            print("creativià: ", cretivita)
                            print("gusto: ", gusto)
                            print("presentazione", presentazione)
                            print()
            break

#es5 fatto
def stampaPiatto():
    while True:
        nuovaCategoria = str(input("Inserire cateogira del piatto da stampare: "))
        if nuovaCategoria == "senior" or nuovaCategoria == "junior":
            break
        else:
            print("Errore, categoria non presente!")
    
    print("DATI DELLA CATEGORIA: ", nuovaCategoria)
    for chiave, lista in dizionario.items():
        for piatto, *voti, categoria in lista:
            if categoria == nuovaCategoria:
                print("nome e cognome", chiave)
                print("piatto: ", piatto)
                for cretivita, gusto, presentazione in voti:
                            print("creativià: ", cretivita)
                            print("gusto: ", gusto)
                            print("presentazione", presentazione)
                            print()

#es6 
def punteggioTotaleMax():
    nomeMax = []
    vettoreVoti = []
    i = 0
    while True:
        categoriaPiatto= str(input("Inserire categoria piatto: "))
        for chiave, lista in dizionario.items():
            for piatto, *voti, categoria in lista:
                if categoriaPiatto == piatto:
                    i+=1
        if i>=1:
            break
        else:
            print("errore")
    while True:
        nuovaCategoria = str(input("Inserire categoria "))
        for chiave, lista in dizionario.items():
            for piatto, *voti, categoria in lista:
                if nuovaCategoria == categoria:
                    i+=1
        if i>=1:
            break
        else:
            print("errore")

    for chiave, lista in dizionario.items():
        for piatto, *voti, categoria in lista:
            if piatto == categoriaPiatto and categoria == nuovaCategoria:
                vettoreVoti.append(voti)
    
    massimo = max(vettoreVoti)

    for chiave, lista in dizionario.items():
        for piatto, *voti, categoria in lista:
            if piatto == categoriaPiatto and categoria == nuovaCategoria:
                if voti == massimo:
                    nomeMax.append(chiave)
    
    print("Punteggio massimo: ", massimo)
    print("Chef con voti più alti: ", nomeMax)

def media():
    vettoreVoti = []
    somma1 = 0
    somma2 = 0
    i = 0
    conta = 0
    e = 0
    categoriaPiatto= str(input("Inserire categoria piatto: "))
    nuovaCategoria = str(input("Inserire categoria "))

    for chiave, lista in dizionario.items():
        for piatto, *voti, categoria in lista:
            if piatto == categoriaPiatto and categoria == nuovaCategoria:
                vettoreVoti.append(voti)





aggiungiChef()
aggiungiPiatto()
stampaChef()
stampaPiatto()
punteggioTotaleMax()
media()




            