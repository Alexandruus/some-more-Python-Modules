#Python 3.7.4, macOS
#Author: Alexander Eriksson
#Grund från föreläsningsexempel


#importerar math
import math

#Class punkt
class Punkt():
    
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __eq__(self, other):
        return self.__x == other.get_x() and self.__y == other.get_y()

    def __str__(self):
        return "Punkt: (" + str(self.__x) + ", " + str(self.__y) + ")"

#Class Cirkel(ärver från superklassen Punkt, )
class Cirkel(Punkt):

    def __init__(self, radie, x = 0, y = 0):
        Punkt.__init__(self, x, y)
        self.__radie = radie

    def get_radie(self):
        return self.__radie

    def get_area(self):
        return math.pi * (self.__radie ** 2)

    def get_circumference(self):
        return math.pi * 2 * self.__radie

    def __eq__(self, other):
        return self.__radie == other.get_radie() and Punkt.__eq__(self, other)

    def __str__(self):
        return "Cirkel med radien: " + str(self.__radie) + " och x = " + str(self.get_x()) + ", y = " + str(self.get_y())


#Class triangel(ärver från Punkt)
class Triangel(Punkt):
    def __init__(self, side_a, side_b, side_c, x = 0, y =0 ): #Tar emot data och tilldelar sedan self attribut samt gör dem privata
        Punkt.__init__(self, x, y)                            #Anropar Punkts init
        self.__side_a = side_a         
        self.__side_b = side_b
        self.__side_c = side_c
    
    def get_side_a(self):   #Skapar åtkomstmetoder som returnerar sidorna om någon vill ha dem
        return self.__side_a    
    
    def get_side_b(self):           
        return self.__side_b
    
    def get_side_c(self):
        return self.__side_c

    def get_area(self):                                             #Funktion för att beräkna arean
        s = (self.__side_a + self.__side_b + self.__side_c) / 2     # skapar 's' för att kunna använda i herons formula
        return math.sqrt(s * (s - self.__side_a) * (s - self.__side_b) * (s - self.__side_c)) #returnerar värdet av herons formula
                                        
    def get_circumference(self):                                        #Funktion för att beräkna omkrets
        return self.__side_a + self.__side_b + self.__side_c            #Returnerna värdet av omkretsen

    def __eq__(self, other):  #Överskuggning av __eq__ för att jämföra. Funktionen tar emot self och other, för att jämföra interna och externa värden. Returnerar true/false
        return self.__side_a == other.get_side_a() and self.__side_b == other.get_side_b() and self.__side_c == other.get_side_c() and Punkt.__eq__(self, other)

    def __str__(self):      #Överskuggning av __str__ för att formatera utskriften korrekt
        return "Triangel med area: " + str(self.__side_a) + " och x = " + str(self.get_x()) + ", y = " + str(self.get_y())


class Rektangel(Punkt):

    def __init__(self, width, height, x = 0, y =0 ): #Tar emot data och tilldelar self attribut samt gör privata
        Punkt.__init__(self, x, y)                   #Anropar Punkts init
        self.__width = width                      
        self.__height = height

    def get_height(self):           #Skapar attributen så det går att hämta dem senare           
       return self.__height

    def get_width(self):
        return self.__width

    def get_area(self):             #Funktion för att beräkna area
        return (self.__height * self.__width)

    def get_circumference(self):    #Funktion för att beräkna omrkets
        return (self.__width * 2) + (self.__height * 2)

    def __eq__(self, other):        #Överskuggning av __eq__ för att jämföra, returnerar true/false
        return self.__width == other.get_width() and self.__height == other.get_height() and Punkt.__eq__(self, other)

    def __str__(self):              #Överskuggning av __str__ för att formatera utskriften korrekt
        return "Rektangel med bredd: " + str(self.__width) + " och höjd " +str(self.__height) + " och x = " + str(self.get_x()) + ", y = " + str(self.get_y())
