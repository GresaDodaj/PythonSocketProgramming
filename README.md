# PythonSocketProgramming

# Metodat built-in dhe ato te definuara

## Metodat built-in

Ne aplikacionin e zhvilluar do te shihni disa nga funksionet kryesore ne socket API:
accept- eshte perdorur  ne anen e serverit per te pranuar  lidhjet (konektimet) e klienteve
bind-    eshte perdorur  ne anen e serverit per te specifikuar IP adresen dhe portin e protokolit.
close- perdoret edhe ne anen e serverit edhe ne ate te klientit per te perfunduar komunikimin 
connect- eshte perdorur  ne anen e klientit per t’u lidhur me nje aplikacion( ne kete rast me server).
listen- eshte perdorur ne anen e serverit dhe vetem ne aplikacionin e zhvilluar ne TCP ku si argument eshte backlog qe specifikon maksimumin e lidhjeve ne server, vlera minimale eshte 0, ne kete rast eshte perdorur si vlere maksimale 5.
recv- eshte perdorur ne server dhe ne klient per te pranuar te dhenat apo mesazhet hyrese ky funksion eshte zbatuar ne aplikacionin e zhvilluar ne TCP kurse ne UDP per te njejtin qellim eshte perdorur funksioni recvfrom. Parameter i ketij funksioni eshte buffer size.
send- eshte perdorur ne server dhe ne klient per te derguar te dhena dhe mesazhe  (output), ky funksion eshte perdorur ne aplikacionin e zhvilluar ne TCP kurse ne UDP per te njejtin qellim eshte perodrur funksioni sendto.
socket- per te krijuar nje socket.
gethostname()- kthen emrin e host-it te makines ku ekzekutohet.

## Metodat e definuara 


Ne server gjithashtu jane definuar disa metoda  per qellime te caktuara te cilat kthejne pergjigjie te klienti varesisht nga kerkesa e tij.Validimi i ketyre kerkesave eshte bere ne anen e serverit kurse ne anen e klientit jane specifikuar metodat ekzistuese dhe me shembuj eshte ilustruar menyra e thirrjes se atyre funksioneve nese funksioni thirret ne menyre te gabuar atehere serveri do te ktheje pergjigjie te klienti per gabimin e bere ne thirrjen e metodes.
IPADDR()- percakton dhe kthen IP adresen e klientit ne formen dhejtore.
PORTNR()- percakton dhe kthen portin e klientit.
ZANORE()- ka parameter nje tekst te derguar nga klienti dhe serveri kthen si pergjigje numrin e zanoreve te perdorura ne ate tekst.
PRINTO()- kthen te njejten  fjali te derguar nga klienti por pa hapesira ne fillim dhe ne fund.
HOST()- kerkon emrin e hostit dhe e kthen pergjigjen te klienti.Ne rast se nuk gjendet emri i hostit tregohet me mesazh se emri i hostit nuk mund te percaktohej.
TIME()- percakton daten dhe kohen aktuale ne server dhe e kthen pergjigje te klienti te formatuar qe te jete e lexueshme per klientin  (dita.muaji.viti ora:minutat:sekondat)
LOJA()- kthen 20 numra random nga rangu [1,99]
FIBONACCI()- gjen numrin FIBONACCI si rezultat i parametrit te dhene hyres.
KONVERTO()- ben konvertimin  e madhesive fizike varesisht nga opsioni i zgjedhur:
CelsiusToKelvin, CelsiusToFahrenheit, 
KelvinToFahrenheit KelvinToCelsius
FahrenheitToCelsius FahrenheitToKelvin
PoundToKilogram KilogramToPound.

Gjithashtu edhe 2 metodat shtese:
vitBrishte()- kthen pergjigjie nese viti i dhene nga klienti si parameter hyres i metodes eshte apo jo vit i brishte.
DecToBin()- kthen konvertimin e numrit te dhene decimal nga ana e klientit ne numer binar.
