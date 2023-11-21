from threading import Thread
import time
import random

#Classe statistiche atleta
class Atleta:   
    def __init__(self, nome, cognome, età, peso, t_min):
        self.nome = nome
        self.cognome = cognome
        self.età = età
        self.peso = peso
        self.t_min = t_min
    
    def GetNome(self):
        return self.nome
    def GetCognome(self):
        return self.cognome
    def GetT_min(self):
        return self.t_min
    
    def iscrizione(self) :
        if(self.t_min <= 5) : 
            return True
        else : 
            print(self.nome + " " + self.cognome + " non puoi parteciapare perchè il tempo è maggiore di 5, tempo minimo atleta: " + str(self.t_min) + "\n") 
            return False   
        
    
     
#Classe con Thread
class Gara(Thread):

    def __init__(self,nome,cognome,t_min,t_tot):
        Thread.__init__(self)#creo Thread
        self.nome = nome
        self.t_min = t_min
        self.t_tot = t_tot
        self.cognome = cognome
    
    def Sleep(n):
        time.sleep(n)
    
    def GetT_tot(self):
        return self.t_tot
    def GetNome(self):
        return self.nome
    def GetCognome(self):
        return self.cognome
    
    def svolgimento_gara(self):
        n_random = random.randint(1,10)#numero casuale da 1 a 10
        if(n_random == 1): #scatto
            print(self.nome + " " + self.cognome + " ha fatto uno scatto\n")
            self.t_tot += self.t_min*0.7
            Gara.Sleep(2)
            self.t_tot += self.t_min
        if(n_random == 2): #contrattura
            print(self.nome + " " + self.cognome + " ha ricevuto una cotrattura\n")
            self.t_tot += self.t_min/2
            if(random.randint(1,2)==2):
                self.t_tot += self.t_min
        if(n_random>=3 and n_random<=7):#andatura normale
            print(self.nome + " " + self.cognome + " corre spensierato\n")
            self.t_tot += self.t_min
        if(n_random == 8): # stiramento
            print(self.nome + " " + self.cognome + " ha ricevuto stiramento\n")
            self.t_tot += self.t_min/4
        if(n_random == 9):#ritmo in aumento
            print(self.nome + " " + self.cognome + " ha aumentato il ritmo\n")
            self.t_tot += self.t_min *0.9
        if(n_random == 10):#stanchezza
            print(self.nome + " " + self.cognome + " inizia a sentire la stanchezza!\n")
            self.t_tot += self.t_min /1.1
        Gara.Sleep(1)#da il tempo di un 1 secondo a km



    def run(self):
        print("è partito: " + self.nome + "" +self.cognome )
        for km in range(42):#simulazione di una maratona, ogni km succede qualcosa 
            Gara.svolgimento_gara(self)
            print("siamo al chilometro: " + str(km+1) + " di corsa\n")
        
        
               


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
#controllo di chi può partecipare
for i in Atleti : 
    if i.iscrizione():
        partecipanti.append(i)

#array in cui salvare risultati
risultati = []
#Partenza gara
for i in partecipanti: 
    corridore = Gara(i.GetNome(),i.GetCognome(),i.t_min,0)
    corridore.start()
    risultati.append(corridore)
#    if(i == Poldo):#ultimo a partire e quindi chiude il Thread
#        corridore.join()
corridore.join()
print("------------------------------GARA FINITA------------------------------\n")
#stampa risultati
tempoVincente = 999#numero default
nomeVincitore= ""
cognomeVincitore =""
for corridori in risultati:
    print(corridori.GetNome() + " " + str(corridori.GetT_tot()))#controllo tempo minore
    if(corridori.GetT_tot()< tempoVincente):
     tempoVincente = corridori.GetT_tot()
     nomeVincitore = corridori.GetNome()
     cognomeVincitore = corridori.GetCognome()
     

#stampa vincitore
print("vincitore maratona: " + nomeVincitore + " "+ cognomeVincitore +" con un tempo di: " + str(tempoVincente))      

#ATTENZIONE!!!
#prendere il risultato in minuti [non in secondi]