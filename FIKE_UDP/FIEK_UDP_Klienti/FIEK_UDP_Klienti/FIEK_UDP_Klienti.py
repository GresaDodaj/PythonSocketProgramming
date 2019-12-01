
import socket
import sys
def getHostPort():
    serverName = 'localhost' #host='127.0.0.1'
    serverPort = 11000 
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
+' 10.VITBRISHTE \n   (Shembull VITBRISHTE 2000)\n 11.DECIMALTOBINAR\n    (Shembull DECIMALTOBINAR 7)\n ---Per te mbyllur programin shtypni quit\n ---Per te nderruar Hostin apo Portin shtypni HostPort')


#clientSocket.bind((host,serverPort))


def Main():
    serverPorti=('localhost',11000)
    while True:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        metodaZgjedhur=input("Zgjedhja juaj: ")
        if (metodaZgjedhur=="quit"):
             clientSocket.close()
             break
        if(metodaZgjedhur==""):
                 continue   
        if metodaZgjedhur=="HostPort":
                 clientSocket.close()
                 serverPorti=getHostPort()
                 continue
        try:
          clientSocket.sendto(metodaZgjedhur.encode('UTF-8'),(serverPorti))
          modifiedData,addr = clientSocket.recvfrom(128)
          print (modifiedData.decode('UTF-8'))
        except Exception:
                print("Gabim ne lidhje, shenoni emrin e Hosti-t dhe Portin perkates")
                serverPorti=getHostPort()

Main()

