
import socket
from datetime import datetime
from _thread import *
from random import randint
from _thread import * 
import sys

#UPHOST='localhost'
UDPPort = 11000
UDPSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
   UDPSocket.bind(('',UDPPort))
except socket.error:
    print("Lidhja nuk arriti te krijohet")
    sys.exit()
print('Serveri u startua ne localhost:'+str(UDPPort))
print('Serveri eshte i gatshem te pranoje kerkesa')

#FUNKSIONET
def IPADDR():
     return addr[0] ; 

def TIME():
     return 'Current time is: '+str(datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

def PORTNR():
     return 'Port number is: '+str(addr[1])

def HOST():
    try:
        return 'Emri i host-it eshte: '+str(socket.gethostname())
    except socket.error as e:
       return 'Host name not found.'

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

def vitBrishte(vitii):
    if vitii % 400 == 0:
        return "Vit i brishte "
    if vitii % 100 == 0:
        return "Vit jo i brishte "
    if vitii % 4 == 0:
        return "Vit i brishte "
    else:
        return "Vit jo i brishte"

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
           return ( temp*2.20462),
        else:
            return "Invalid Operation"

def DecToBin(decimal):
    numri = int(decimal)
    binar = ""
    while numri != 0:
      rest = numri % 2
      binar = str(rest) + binar
      numri = numri // 2
    return ("Binary:  %s" % binar)

def kerkesa (pergjKlientit):
    pergjKlientit = pergjKlientit.split (" ", 1)
   
    if (pergjKlientit[0] == "IPADDR"):
        pergj = IPADDR();
        fjala = pergj;
        fjala2 = "Pergjigja: " + str(fjala);
        UDPSocket.sendto (fjala2.encode('UTF-8'),addr);
       
    elif (pergjKlientit[0] == "PORTNR"):
        port= PORTNR();
        data="Port number is "+str(port);
        UDPSocket.sendto(data.encode('UTF-8'),addr)
        
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
            return ("Kerkesa nuk eshte bere si duhet")

    elif (pergjKlientit[0] == "KONVERTO"):
        try:
            operacioni=pergjKlientit[1].split(" ",1)
            stringu = int(operacioni[1])
            return str(KONVERTO(operacioni,stringu))
        except Exception:
             return ("Komanda e dhene nuk eshte ne rregull")

    elif (pergjKlientit[0] == 'VITBRISHTE'):
            try:
                return vitBrishte(int(pergjKlientit[1]));
            except Exception:
                return ("Gabim ne input, Shembull: VITBRISHTE 2000")
    elif (pergjKlientit[0]=='DECIMALTOBINAR'):
            try:
                return str(DecToBin(pergjKlientit[1]))
            except Exception:
                return ("Komanda e dhene nuk eshte ne rregull")
    else:
        return 'Gabim ne input!'

while True:
        data,addr=UDPSocket.recvfrom(128)
        try:
             var1=str(kerkesa(data.decode('UTF8')))
        except socket.error:
            break
        UDPSocket.sendto(var1.encode('UTF-8'),addr)
 
  