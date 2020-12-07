#Python 3.7.4, macOS
#Author: Alexander Eriksson, 19940902-5971
#Grund från föreläsningsexempel

import geometri

def main():
    print("GeoTest: \n")
    p1 = geometri.Punkt(3, 4)
    p2 = geometri.Punkt(5, 2)
    print(str(p1))
    print(p2)
    print(p1 == p2, "\n")

    #Testa Cirkel-klassen
    c1 = geometri.Cirkel(7, 3, 4)
    c2 = geometri.Cirkel(11, 5, 2)
    c3 = geometri.Cirkel(7, 3, 4)
    print("Cirkeln area =", c1.get_area())
    print("Cirkeln omkrets =", c1.get_circumference())
    print(c1 == c2)
    print(c1)
    print(c3)
    print(c1 == c3, "\n")

    #Testa Triangel-klassen
    triangel1 = geometri.Triangel(14, 7, 14, 0, 0 ) #Skickar in värden till Triangel
    triangel2 = geometri.Triangel(8, 4, 8, 0, 0 )
    triangel3 = geometri.Triangel(14, 7, 14, 0, 0 )
    print("Triangelns area =", triangel1.get_area()) #Testar funktionen som beräknar area
    print("Triangelns omkrets=", triangel1.get_circumference()) #Testar funktionen som beräknar omkrets
    print(triangel1 == triangel2)   #Jämför de triangel 1 och 2, testar nya överskuggning av __eq__
    print(triangel1)                #Printar triangel 1, testa nya överskuggnign av __str__
    print(triangel2)                #Printar triangel 2
    print(triangel3)                #Printar triangel 3
    print(triangel1 == triangel3, "\n") #Kontrollerar att triangel 1 == triangel 2

    #Testa Rektangel-klassen
    rektangel1 = geometri.Rektangel(5, 5, 0, 0) #Skickar in värdet till Rektangel
    rektangel2 = geometri.Rektangel(8, 4, 3, 5) 
    rektangel3 = geometri.Rektangel(5, 5, 0, 0)
    print("Rektangels area =", rektangel1.get_area())   #Testar funktionen som beräknar area
    print("Rektangels omkrets=", rektangel1.get_circumference())    #Testar funktionen som beräknar omkrets
    print(rektangel1 == rektangel2) #Testar nya överskuggning av __eq__
    print(rektangel1)               #Testar nya överskuggning av __str_
    print(rektangel2)
    print(rektangel3)
    print(rektangel1 == rektangel3, "\n")

    
    


if __name__ == "__main__":
    main()
