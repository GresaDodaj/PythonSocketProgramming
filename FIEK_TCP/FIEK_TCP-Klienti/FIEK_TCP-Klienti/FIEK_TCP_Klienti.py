import socket
import sys


def getHostPort():
    host = 'localhost'
    serverPort = '11000'
    inputCorrect = False
    while not inputCorrect:
        try:
            host = input("Hosti: ")
            serverPort = int(input("Porti: "))
            inputCorrect = True
        except Exception:
            print("Formati i gabuar i portit!\nShenoni perseri")
            continue

    return (host,int(serverPort))





print ("Zgjedhni njeren nga metodat: \n 1.IPADDR\n"
+" 2. PORTNR\n 3. ZANORE\n    (Shebmull ZANORE FIEK Inxhinieri Kompjuterike)\n 4. PRINTO\n    (Shebmull PRINTO    FIEK Inxhinieri Kompjuterike    )\n 5. HOST\n 6. TIME\n "
+'7. LOJA\n 8. FIBONACCI\n    (Shembull FIBONACCI 10)\n 9. KONVERTO\n    Nga Komanda KONVERTO mund te zgjidhni'
+'njeren nga OPSIONET ne vazhdim:\n    -CelsiusToKelvin\n    -CelsiusToFahrenheit\n'
+'    -KelvinToFahrenheit\n    -KelvinToCelsius\n    -FahrenheitToCelsius\n    -FahrenheitToKelvin\n'
+'    -PoundToKilogram\n    -KilogramToPound \n    (Shembull: KONVERTO CelsiusToKelvin 10)\n'
+' 10.VITBRISHTE \n   (Shembull VITBRISHTE 2000)\n 11.DECIMALTOBINAR\n    (Shembull DECIMALTOBINAR 7)\n ---Per te mbyllur programin shtypni quit \n ---Per te nderruar Hostin apo Portin shtypni HostPort')



def Main():
    serverPorti=('localhost',11000)
    while True:
        metodaZgjedhur=input(">>Zgjedhja juaj: ")
        metodaZgjedhurE = metodaZgjedhur.encode("UTF-8")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if(metodaZgjedhur=="quit"):
         s.close()
         break
        else:
            if(metodaZgjedhur==""):
             continue
            if metodaZgjedhur=="HostPort":
             s.close()
             serverPorti=getHostPort()
             continue
  
            try:
                if metodaZgjedhur=="HostPort":
                    s.close()
                    serverPorti=getHostPort()
                s.connect((serverPorti))
                s.send (metodaZgjedhurE)
                pergj = s.recv(128); #BUFFER SIZE =128BYTES
                pergjD = pergj.decode ("UTF-8")
                print (pergjD)
                s.close()  
            except Exception:
                    print("Gabim ne lidhje, shenoni emrin e Hosti-t dhe Portin perkates")
                    serverPorti=getHostPort()
                   

         

Main();
