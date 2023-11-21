class Atleta:   
    def __init__(self, nome, cognome, età, peso, t_min):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.peso = peso
        self.t_min = t_min
    

    def iscrizione(self) :
        if(self.t_min <= 5) : 
            return True
        else : 
            print(self.nome + " " + self.cognome + " non puoi parteciapare perchè il tempo è maggiore di 5, tempo minimo atleta: " + str(self.t_min) + "\n") 
            return False   
     
        


#t_min = tempo di corsa per gareggiare 5 per Kilometro
#inserimento alteti
Atleti = [] #array atleti
partecipanti = [] # partecipanti gara
Lorenzo = Atleta ("Lorenzo", "Bastianelli", 17, 70, 5)
Enrico = Atleta ("Enrico", "Fiore", 18, 65, 7)
Gino = Atleta ("Gino", "Rossi", 19, 80, 3)
Pippo = Atleta ("Pippo", "Baudo", 20, 85, 8)
Poldo = Atleta ("Poldo", "Bianchi", 21, 85, 4)
Atleti.append(Lorenzo) 
Atleti.append(Enrico)
Atleti.append(Gino)
Atleti.append(Pippo)
Atleti.append(Poldo)
for i in Atleti : 
    if i.iscrizione():
        partecipanti.append(i)