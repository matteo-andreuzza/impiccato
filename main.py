parola = input("inserisci la parola ")
parola_list = list(parola)
imp = 0;
print("debug" +  str(parola_list))
lun = len(parola_list)
parola_vuota =[lun]
print("debug" +  str(parola_list))

cond = True;
def mostra():
    print(parola_vuota)
def incrementa(a):
    for i in range(lun):
        print("parola list" + parola_list[i])
        if parola_list[i] == a:
            parola_vuota[i] = a
        else:
            pass
def impiccato():
    print("disegna impiccato")
    imp = imp + 1
while cond:
    lettera = input("inserisci una lettera ")
    if(lettera in parola):
        incrementa(lettera)
        
        mostra()
    else:
        impiccato()

    
    