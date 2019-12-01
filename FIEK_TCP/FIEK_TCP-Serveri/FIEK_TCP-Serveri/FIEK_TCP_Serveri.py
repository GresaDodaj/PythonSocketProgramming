import socket
from socket import *
from datetime import datetime
from _thread import *
from random import randint
import sys

host='localhost'
serverPort = 11000
serverSocket = socket(AF_INET, SOCK_STREAM)
try:
    serverSocket.bind((host,serverPort)) 
except socket.error:
    print("Lidhja nuk arriti te krijohet")
    sys.exit()


print('Serveri u startua ne localhost:'+str(serverPort))
serverSocket.listen(5)
print('Serveri eshte gati te pranoje kerkesa...')
input = [serverSocket,]


#Metodat:
def IPADDR():
     return "IP addressa eshte "+ addr[0]                                                  
def TIME():
     return 'Data dhe ora: '+str(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

def PORTNR():
     return 'Port number eshte: '+str(addr[1])

def HOST():
    try:
        return 'Emri i host-it eshte:  '+str(gethostname())
    except socket.error as e:
       return 'HOST NAME NOT FOUND '

def LOJA():
    numbers=[randint(1,99) for p in range(0,20)]
    return numbers

def FIBONACCI(n):
      if n == 0: return 0
      elif n == 1:  return 1
      else: return (FIBONACCI(n-1)+FIBONACCI(n-2))

def ZANORE(string):
    num_zanoreve=0
    for char in string:
        if char in "aeiouyAEIOUY":
           num_zanoreve = num_zanoreve+1
    return 'Numri i zanoreve ne tekst eshte '+str(num_zanoreve)

def PRINTO(string):
    return string.strip()
# ME .strip(' ') i largon whitespaces edhe ne fillim edhe ne fund 
# me .lstrip(' ') veq majtas e me .rstrip(' ') edhe djathas

def vitBrishte(vitii):
    if vitii % 400 == 0:
        return "Ky vit eshte  i brishte "
    if vitii % 100 == 0:
        return "Ky vit nuk eshte brishte "
    if vitii % 4 == 0:
        return "Ky vit eshte brishte "
    else:
        return "Ky vit nuk eshte  i brishte"

def KONVERTO(operacioni,temp):
        print (operacioni)
        if (operacioni[0] =='CelsiusToKelvin'):
           return (temp + 273.15)
        elif (operacioni =='CelsiusToFahrenheit'):
           return(((9 * temp) / 5) + 32)
        elif (operacioni[0] =='KelvinToFahrenheit'):
            return ((9 * (temp+273)) / 5) + 32;
        elif (operacioni[0] =='KelvinToCelsisu'):
            return(temp-273.15)
        elif (operacioni[0] =='FahrenheitToCelsius'):
            return((temp-32)*5/9)
        elif (operacioni[0] =='FahrenheitToKelvin'):
            return( (temp-32)*5/9+273.15)
        elif (operacioni[0] =='PoundToKilogram'):
            return( temp*0.453592)
        elif (operacioni[0] == 'KilogramToPound'):
           return ( temp*2.20462)
        else:
            return "Operacioni nuk eshte ne rregull"

def DecToBin(decimal):
    numri = int(decimal)
    binar = ""
    while numri != 0:
      rest = numri % 2
      binar = str(rest) + binar
      numri = numri // 2
    return ("Binary:  %s" % binar)

def kerkesaKlientit (pergjKlientit):
        pergjKlientit = pergjKlientit.split (" ", 1);
        if (pergjKlientit[0] == "IPADDR"):
            pergj = IPADDR();
            fjala = pergj;
            fjala2 = "Pergjigja: " + str(fjala);
            connectionSocket.send(fjala2.encode("UTF-8"))

        elif (pergjKlientit[0] == "PORTNR"):
            port= PORTNR();
            data=str(port);
            connectionSocket.send(data.encode("UTF-8"))
            
        elif (pergjKlientit[0] == "ZANORE"):
            try:
                return ZANORE(pergjKlientit[1])
            except Exception:
                return("Kerkesa nuk eshte  ne rregull, provoni perseri\n Psh: ZANORE FIEK Inxhinieri Kompjuterike")

        elif (pergjKlientit[0] == "PRINTO"):
             try:
                 return PRINTO(pergjKlientit[1])
             except Exception:
                 return("Kerkesa nuk eshte  ne rregull, provoni perseri\n Psh: PRINTO     FIEK Inxhinieri Kompjuterike  ")

        elif (pergjKlientit[0] == "HOST"):
            return HOST()

        elif (pergjKlientit[0] == "TIME"):
            return TIME()

        elif (pergjKlientit[0] == "LOJA"):
            return LOJA()

        elif (pergjKlientit[0] == "FIBONACCI"):
            try:
              return FIBONACCI(int(pergjKlientit[1]));
            except Exception:
             return ("Kerkesa nuk eshte  ne rregull, provoni perseri\n Psh: FIBONACCI 10")

        elif (pergjKlientit[0] == "KONVERTO"):
            try:
             operacioni=pergjKlientit[1].split(" ",1)
             stringu = int(operacioni[1]);
             return str(KONVERTO(operacioni,stringu))
            except Exception:
             return ("Kerkesa nuk eshte  ne rregull, provoni perseri\n Psh: KONVERTO CelsiusToKelvin 10")

        elif (pergjKlientit[0] == 'VITBRISHTE'):
            try:
                return vitBrishte(int(pergjKlientit[1]));
            except Exception:
                return ("Gabim ne input, Shembull: VITBRISHTE 2000")
        elif (pergjKlientit[0]=='DECIMALTOBINAR'):
            try:
                return str(DecToBin(pergjKlientit[1]))
            except Exception:
                return ("Komanda e dhene nuk eshte ne rregull,provoni perseri\n Psh:  DECIMALTOBINAR 7")
        else:
            return 'Kerkesa e gabuar!'



while True:
   connectionSocket,addr=serverSocket.accept()
   try:
       word=connectionSocket.recv(128)
   except Exception:
       break
   request=word.decode('UTF-8')
   var=str(kerkesaKlientit(request))
   var_1=var.encode('UTF-8')
   connectionSocket.send(var_1)
 

connectionSocket.close()
  
    
    
    



