//Alexander Eriksson, 19940902-5971
//WEBPROG, Uppgift 4
//macOS
//För for-loopen i validateBic() samarbetade jag med kurskamrat Björn Malmborg

function validateEmail() {                                      //Funktion för att validera email-input
    var universitet = document.getElementById("universitet");       //anropar id från dokument
    var epost = document.getElementById("epost");
    var epostValue = epost.value.toLowerCase();                     //hämtar epost/universitet value och gör till lowercase
    var universitetValue = universitet.options[universitet.selectedIndex].value.toLowerCase();

    var check = new RegExp( "@" + universitetValue + ".se$");       //skapar en ny RegExp som innehåller ett pattern
    var found = check.test(epostValue);                             //kontroll av input i epost gentemot min RegExp

    if (found == true){                                             //om kontrollen == true                                 
        epost.setCustomValidity("");
        }
    else{
        epost.setCustomValidity("Fyll i rätt format tack");
        }
}

function validateBic(){                                         //Funktion för att validera bic-input
    var bic = document.getElementById("bic");                   //anropar id från dokument
    var bicValue = bic.value.toUpperCase();                                   //hämtar value
    var bicControl = bicValue.slice(10);                        //hämtar kontrollsiffran(index 10)
    bicValue = bicValue.slice(0,10);                            /*hämtar fullständigt bic-nummer */ 
                                                                
    /* lista med värden*/ 
    var bicList = {A:10, B:12, C:13, D:14, E:15, F:16, G:17, H:18, I:19, J:20, K:21, L:23, M: 24, N:25, O:26, P:27, Q:28, R:29, S:30, T:31, U:32, V:34, W:35, X:36, Y:37, Z:38, 0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9};
    

    var summa = 0;                              /*Sätter summa till 0*/ 
    for (var i = 0; i <bicValue.length; i++ ){     /*for-loop som går igenom bic-nummer. Sätter i=0, och sålänge i är mindre än längden på bicValue ska den fortsätta loopa*/ 
        summa += bicList[bicValue.charAt(i)] * Math.pow(2, i);  /* hämtar värdet i bicList genom att gå efter chartAt(i) på bicValue, och utför därefter beräkningen för att få fram summa */
    }

    var checkBic = summa % 11;          /*Använder modulo för att se vad resten av summa blir*/ 

    if (checkBic  == bicControl){           /* Kontrollerar om uträknad kontrollsiffra stämmer med inmatad */
        bic.setCustomValidity("");
    }
    else{
        bic.setCustomValidity("Bic-nummer felaktig!");
    }

}