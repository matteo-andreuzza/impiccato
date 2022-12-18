import sys
import time
import PySimpleGUI as sg
def main():
    global imp
    layout = [[sg.Text('Inserisci parola principale.')],      
        [sg.InputText()],      
        [sg.Submit(), sg.Cancel()]]      
    window = sg.Window('Impiccato', layout)    
    event, values = window.read()    
    window.close()
    text_input = values[0]     
    parola = text_input
    parola_list = list(parola)
    imp = 0;
    print("debug" +  str(parola_list))
    lun = len(parola_list)
    parola_vuota = [""]*lun
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
    imp = 0
    def impiccato():
        if impiccato == 7:
            print("impiccato concluso, fine gioco")
            esc()
        global imp
        print("disegna impiccato")
        imp = imp + 1
        print("stato impiccato: " + str(imp))
        # This is the normal print that comes with simple GUI
        sg.Print('Re-routing the stdout', do_not_reroute_stdout=False)
        # this will now output to the sg display.
        sg.Print("stato impiccato: " + str(imp))
        time.sleep(5)
    def esc():
        print("")
        sc = input("gioco terminato, per iniziare di nuovo schiaccia M, per uscire premi invio  ")
        if sc == "M" or sc == "m":
            main()
        else:        
            sys.exit(0)
    while cond:
        lettera=""
        if parola_vuota == parola_list:
            esc()
            
        layout = [[sg.Text('Inserisci una lettera.')],      
            [sg.InputText()],      
            [sg.Submit(), sg.Cancel()]]      
        window = sg.Window('Impiccato', layout)    
        event, values = window.read()    
        window.close()
        text_input = values[0]     
        lettera = text_input
        if(lettera in parola):
            incrementa(lettera)
            
            mostra()
        else:
            impiccato()
            
main()
    
    