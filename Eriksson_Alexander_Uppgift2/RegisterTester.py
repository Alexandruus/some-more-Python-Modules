#Alexander Eriksson, 19940902-5971
#WEBPROG Uppgift 2
#macOS

#importerar filen cashregister

import cashregister

def main():
    #testa sweReg
    sweReg = cashregister.CashRegister( 'SweReg', 18 ) #Skickar in namn och skattesats
    sweReg.addItem('Laptop', 800)                       #I funktionen addItem, lägger till namn och pris
    sweReg.addItem('Kalkylator', 20)
    sweReg.addItem('Kamera', 300)
    sweReg.addItem('Mobiltelefon', 20000)
    print(sweReg)                                   #Printar resultat
    sweReg.clear()                             #Anropar funktionen för att nollställa
    print("Dagens kassaregister är nu åsterställd")
    print("")
    
    #testa norReg
    norReg = cashregister.CashRegister('norReg', 20 )   #Skickar in namn och skattesats
    norReg.addItem('Cooler', 150)                       #I funktionen addItem, lägger till namn och pris
    norReg.addItem('Graphics card', 600)
    norReg.addItem('RAM', 300)
    norReg.addItem('Adapter', 70)
    print(norReg)                                       #Printar resultat
    norReg.clear()                                  #Anropar funktionen för att nollställa
    print("Dagens kassaregister är nu åsterställd")
    print("")

    #testa denReg
    denReg = cashregister.CashRegister('denReg', 22 )   #Skickar in namn och skattesats
    denReg.addItem('Computer' , 1500)                   #I funktionen addItem, lägger till namn och pris
    denReg.addItem('Television', 700)
    denReg.addItem('Smartphone', 500)
    denReg.addItem('Cinema', 3000)
    print(denReg)                                        #Printar resultat
    denReg.clear()                                  #Anropar funktionen för att nollställa
    print("Dagens kassaregister är nu åsterställd")
    print("")

    #testa finReg
    finReg = cashregister.CashRegister('finReg', 24 )   #Skickar in namn och skattesats
    finReg.addItem('Samsung', 700)                      #I funktionen addItem, lägger till namn och pris
    finReg.addItem('Iphone' , 1000)
    finReg.addItem('Huawei' , 250)
    finReg.addItem('Sony' , 400)
    print(finReg)                                       #Printar resultat
    finReg.clear()                                  #Anropar funktionen för att nollställa
    print("Dagens kassaregister är nu åsterställd")
    print("")


main()
