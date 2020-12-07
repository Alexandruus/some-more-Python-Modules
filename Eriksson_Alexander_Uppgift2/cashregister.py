#Alexander Eriksson, 199409025971
#WEBPROG, Uppgift 2
#macOS
#Har samarbetat med kurskamrat Björn Malmborg i vissa moment

class CashRegister():
    
    def __init__(self, name, taxRate):                        #Skickar med taxRate då vi behöver den datan från testfilen
        self.__name = name
        self.__taxRate = taxRate                        #Skapar variablen för taxRate
        self.__addItem = []                             #Skapar en lista där vi kan lagra produkter
        self.__productSold = 0                          #Skapar de olika variablerna och sätter dem till 0
        self.__income = 0                               
        self.__taxPart = 0

                 
    def get_name(self):                              #Skapar åtkomstmetoder
       return self.__name

    def get_taxRate(self):                          
        return self.__taxRate
    
    def addItem (self, product, price):                 #Skapar en funktion för att hantera försäljning
        self.__productSold += 1                          #Lägger till +1 i productSold när en produkts säljs 
        self.__income += price                          #Lägger till "price" i income
        self.__addItem.append(product)                  #Lägger till själva produkten i vår lista över sålda produkte
    
    def get_productSold(self):
        return self.__productSold
    
    def get_income(self):
        return self.__income

    def get_taxPart(self):
        return self.__income * ( self.__taxRate / 100 )

    
    def clear(self):                                #Skapar en funktion för att återställa våra variabler
        self.__productSold = 0
        self.__income = 0
        self.__taxPart = 0
        self.__totalProducts = 0
        self.__addItem = []

        return self.__productSold, self.__income, self.__taxPart, self.__addItem  #Returnernar variablerna, fast nu återställda
    
    def __str__(self):                              #Överskuggning av __str__ för vår utskrift
        return self.__name + " har " + str(self.__taxRate) + " % i skattesats och har sålt " + str(self.__productSold) + (' stycken produkter.\n') + 'Total inkomst för dagen är ' + str(self.__income) + ' euro.' + '\nAndelen skatt som ska betalas är: ' + str(self.get_taxPart()) +' euro.' + "\nDe sålda produkterna är: \n" + ("\n".join(self.__addItem))
