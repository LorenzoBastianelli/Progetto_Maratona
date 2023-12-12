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

    # variabili generali per salvare il dato del singolo maratoneta    
    numeroDisparo = 0    
    Istirato = False
    IsContratto = False
    
    def Sleep(n):
        time.sleep(n)
    
    def GetT_tot(self):
        return self.t_tot
    def GetNome(self):
        return self.nome
    def GetCognome(self):
        return self.cognome
    
    def svolgimento_gara(self,km):
        # il segno // divide per interi invece / è la divisione normale con la virgola
        if(self.Istirato==False):
            if(self.IsContratto == False):
                if(km <= 1):# se è il primo km o meno lo indirizzo direttamente ad una andatura normale
                    n_random = 3
                elif(km % 2 == 0):# ogni 2 km estraggo un numero casuale per l'evento 
                    n_random = random.randint(1,10)#numero casuale da 1 a 10
                    self.numeroDisparo  = n_random
                elif(km % 2 != 0 and km >2):# l'evento successo nel km precedente (pari) continua anche per il km successivo (disparo)
                    n_random = self.numeroDisparo
                if(n_random == 1 and self.Istirato == False): #scatto
                    print(self.nome + " " + self.cognome + " ha fatto uno scatto\n")
                    self.t_tot += self.t_min // 0.7
                    Gara.Sleep(2)
                    self.t_tot += self.t_min
                if(n_random == 2 and self.Istirato == False): #contrattura
                    print(self.nome + " " + self.cognome + " ha ricevuto una cotrattura\n")
                    self.t_tot += self.t_min * 2 
                    self.IsContratto = True
                if(n_random>=3 and n_random<=7 and self.Istirato == False):#andatura normale
                    print(self.nome + " " + self.cognome + " corre spensierato\n")
                    self.t_tot += self.t_min
                if(n_random == 8): # stiramento
                    print(self.nome + " " + self.cognome + " ha ricevuto stiramento\n")
                    self.t_tot += self.t_min * 4
                    self.Istirato = True
                if(n_random == 9 and self.Istirato == False):#ritmo in aumento
                    print(self.nome + " " + self.cognome + " ha aumentato il ritmo\n")
                    self.t_tot += self.t_min // 0.9
                if(n_random == 10 and self.Istirato == False):#stanchezza
                    print(self.nome + " " + self.cognome + " inizia a sentire la stanchezza!\n")
                    self.t_tot += self.t_min * 1.1
            else:
                if(random.randint(1,2)==2): #non ha più la contrattura
                        self.t_tot -= self.t_min
                        print(self.nome + " " + self.cognome + " non ha più la contrattura\n")
                        self.IsContratto = False
        else:
             print(self.nome + " " + self.cognome + " è ancora stirato\n")
             self.t_tot += self.t_min * 4
        Gara.Sleep(1)#da il tempo di un 1 secondo a km



    def run(self):
        print("è partito: " + self.nome + " " +self.cognome )
        for km in range(42):#simulazione di una maratona, ogni km succede qualcosa 
            Gara.svolgimento_gara(self,km+1) 
            print(self.nome + " " + self.cognome +" al chilometro: " + str(km+1) + " di corsa\n")
            #print(self.nome + " " + self.cognome +" tempo: " + str(self.t_tot))




""""
#inserimento alteti
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
"""
def mostraAtleti():
    j=1
    for i  in Atleti:
        print("Partecipante "+ str(j) + ": " + i.GetNome() + " " + i.GetCognome()+ "\n")
        j+=1

#MENU
def Menu():
    nelMenu = True #per entrare e rimanere nel menu
    while(nelMenu == True):
        print("Scegliere una tra le seguenti opzioni: \n1) Inserire atleta\n2) Eliminare atleta\n3) Iniziare gara\n4) Mostra partecipanti\n")
        while(True):
            try:
                scelta = int(input("Inserire il NUMERO dell'opzione: "))
                if scelta in (1, 2, 3,4):# se la scelta è 1 o 2 o 3 o 4 esci dal try catch
                    break
                else:
                    print("ATTENZIONE: bisogna inserire il numero corrispondente alla scelta")
            except ValueError:
                print("ATTENZIONE: bisogna inserire il numero corrispondente alla scelta")
        
        if( scelta == 1): #inserire atleta
            print("Per ISCRIVERE un atleta ci serve: NOME, COGNOME, ETA', PESO, TEMPO MINIMO A KM\n")
            print("Inserire NOME\n")
            nome = str(input("nome: "))
            print("\nInserire COGNOME\n")
            cognome = str(input("cognome: "))
            print("\nInserire ETA'\n")
            età = int(input("età: "))
            print("\nInserire PESO\n")
            peso = int(input("peso: "))
            print("\nInserire TEMPO MINIMO A KM\n")
            t_min = float(input("tempo minimo: "))
            nuovo_atleta = Atleta(nome,cognome,età,peso,t_min)#creazione nella classe Atleta 
            Atleti.append(nuovo_atleta)# aggiunto nell'array
        elif(scelta == 2):# elimina atleta
            mostraAtleti()
            print("Per ELIMINARE un atleta ci serve: NOME, COGNOME\n")
            print("Inserire NOME\n")
            nome = str(input("nome: "))
            print("\nInserire COGNOME\n")
            cognome = str(input("cognome: "))
            nonTrovato =0
            for atleta in Atleti:
                if(atleta.GetNome() == nome and atleta.GetCognome() == cognome):
                    Atleti.remove(atleta)# rimosso atleta dall'array
                    print("\nL'Atleta"+ nome +" "+ cognome+" è stato rimosso con successo\n")
                    break
                else:
                    nonTrovato+=1 # per tenere traccia di quante volte il nome inserito non è stato trovato
            if(nonTrovato == len(Atleti)):# in caso il nome è stato inserito sbagliato
                print("\nAtleta non trovato, provare a reinserire atleta\n")
        elif(scelta == 3):# inizia gara
            #controllo di chi può partecipare
            for i in Atleti : 
                if i.iscrizione():
                    partecipanti.append(i)
            if(len(partecipanti)<2): #controllo che ci siano abbastanza atleti per fare la gara (minimo 2)
                print("Ci sono ancora pochi alteti per iniziare la gara\n")
            else:
                nelMenu = False
        elif(scelta == 4):# mostra partecipanti
            mostraAtleti()


#MAIN
#t_min = tempo di corsa per gareggiare 5 per Kilometro

Atleti = [] #array atleti
partecipanti = [] # partecipanti gara
Menu()
#array in cui salvare risultati
risultati = []
#Partenza gara
for i in partecipanti: 
    corridore = Gara(i.GetNome(),i.GetCognome(),i.t_min,0)
    corridore.start()
    risultati.append(corridore)
#Aspettando che tutti finiscano la gara
for thread  in risultati: 
    thread.join()
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
print("Vincitore maratona: " + nomeVincitore + " "+ cognomeVincitore +" con un tempo di: " + str(tempoVincente))      

#ATTENZIONE!!!
#prendere il risultato in minuti [non in secondi]