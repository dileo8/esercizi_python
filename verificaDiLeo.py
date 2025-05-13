class Pagella:
    def __init__(self, lista):
        self.lista = lista

    def __repr__(self):
        for i in range(len(self.lista)):
            print(self.lista[i])

    def media(self):
        somma = 0
        conta = 0
        for i in range(len(self.lista)):
            somma+=self.lista[i]
            conta+=1
        return somma/conta
    
    
    def __getitem__(self,indice):
        return self.lista[indice]
    
    def __eq__(self, pagella):
            conta = 0
            for i in range(len(self.lista)):
                for x in pagella.lista:
                    if self.lista[i] == x:
                        conta = conta+1
            
            if conta == len(self.lista):
                risposta = True
            else:
                risposta = False
            return risposta
    
    def __sub__(self, pagella):
        sottrazione = []
        for a,b in zip(self.lista, pagella):
            sottrazione.append(a-b)
        return pagella(sottrazione)
    


p = Pagella([2,4,6])
p1 = Pagella([2,4,6])
p2 = Pagella([1,2,4])
print("Media = ", p.media())

print(p[1])
print(p.__eq__(p1))
print("sub = ", p1.__sub__(p2))