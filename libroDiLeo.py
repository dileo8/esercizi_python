class Libro:
    def __init__(self, isbn, titolo, autore, anno):
        self.isbn = isbn
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    def __str__(self):
        return f"ISBN = {self.isbn}\nTitolo = {self.titolo}\nAutore = {self.autore}\nAnno = {self.anno}"
    

class Biblioteca:
    def __init__(self, lista):
        self.lista = lista

    def aggiungi_libro(self, libro):
        self.lista.append(libro)

    def rimuovi_libro(self, isbn1):
        print(f"Rimozione del libro con ISBN {isbn1}")
        for i in self.lista:
            if i.isbn == isbn1:
                self.lista.remove(i)
                print("Rimosso con successo!")

    def elenco_libri(self):
        print("Libri presenti in bibblioteca:")
        for i in self.lista:
            print(i)

    def cerca_libro(self, isbn1):
        print(f"Ricerca del libro con ISBN {isbn1}")
        for i in self.lista:
            if i.isbn == isbn1:
                print(i)
                



libro1 = Libro("aaa", "l'informatica", "dileo", 2007)
libro2 = Libro("bbb", "i sistemi", "bressan", 2009)
libro3 = Libro("ccc", "la storia", "giovenzana", 2011)

biblioteca = Biblioteca([])

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro3)

biblioteca.elenco_libri()
biblioteca.cerca_libro("aaa")
biblioteca.rimuovi_libro("bbb")
biblioteca.elenco_libri()



