#Alexander Eriksson, 19940902-5971
#macOS
#WEBPROGVT18
#2019-10

#Importerar
from bs4 import BeautifulSoup
from lxml import html
import urllib.request
import ssl
import re

def main():  #Våran main-funktion
    url = "https://dsv.su.se/utbildning/alla-utbildningar/kandidatprogram" #url vi ska skrapa

    context = ssl._create_unverified_context() #För att lösa problemet med SSL
    source = urllib.request.urlopen(url, context = context) #Öppnar
    html = source.read()                            #html = läsa url
    tree = BeautifulSoup(html, "html.parser")       #Läser htmlkoden med beautifulsoup

    text_string = ""                                #skapar variabeln där vi ska spara text
    text_string = (textScrape(tree, text_string))   #kör förstasidan genom vår reader


    #letar upp children/fördjupningslänkar i div articleBody
    div_text= tree.find("div", {"class", "articleBody"})
    links = div_text.findChildren("a") #söker efter anchor-taggar
    link_list = []                  #skapar en lista där vi ska lägga länkar
    for link in links:              #for-loop som går igenom och lägger till href i vår lista
        real_link = re.findall(r'href="(.+)"', str(link))
        link_list.append(str(real_link[0]))
    
    tree_list = []
    #för varje link i link_list så anrop funktionen openlink
    for link in link_list:
        tree_list.append(openLink(link))
    #för varje tree i link_list, kör funktionen reader 
    for tree in tree_list:
        text_string = (textScrape(tree, text_string))


    di = (wordCalc(text_string)) #anropa funktionen wordCalc
    results(di)                  #anropa funktioner results
    
def openLink(url):  #Funktion för att öppna länkar och läsa html
    context = ssl._create_unverified_context() 
    source = urllib.request.urlopen(url, context = context)
    html = source.read()
    tree = BeautifulSoup(html, "html.parser")

    return tree         #Return tree

def textScrape(tree, text_string):  #Funktion för att gå igenom träden och returnera text_string
    p_tags = tree.findAll("p")
    h_tags = tree.findAll(re.compile('^h[1-6]$'))

    for tag in h_tags:          #For loop för att gå igenom varje ord i <h> taggar
        text = tag.text.lower()
        text_string = text_string + " " + text

    for tag in p_tags:  #For loop för att gå igenom varje ord i <p> taggar
      text = tag.text.lower()
      text_string = text_string + " " + text
        
    return text_string          #Return text_string med alla ord från for-looparna
    
def wordCalc(text_string):  #Funktion för att sortera bort ord/tecken och sedan räkna frekvens med dict
    #skapar en variabel med ord och tecken som skall tas bort
    bannedWords = ( "i", "och", "att", "det", "som", "en", "på", "är", "av", "för", "med",
                   "till", "den", "har", "de", "inte", "om", "ett", "han"," men", ".", ",","!")

    #använder re för att ta bort ord/tecken och ersätter dem med mellanslag
    pattern = re.compile(r"\b(" + "|".join(bannedWords) + ")\\W", re.I)
    text_string = (pattern.sub(" ",text_string))

    #använder dict för att loopa igenom listan och räkna frekvensen av orden
    di = dict()
    text_list = text_string.split()    
    for word in text_list:        
        if word in di:
            di[word] = di[word] +1
        else:
            di[word] = 1

    return di

def results(di): #Funktion för att skriva ut det mest frekvent använda ordet
    #loopar igenom di för att hitta det ord med högst value(det som var mest frekvent använt)
    largest = 0
    theword = None
    for k,v in di.items():
        if v > largest:
            largest = v
            theword = k
    print("Det vanligast förekommande ordet återfanns", largest, "gånger, och var:", theword)
     
if __name__ == "__main__":      #För att starta programmet
    main()
        
