import random

class Board():
    def __init__(self,szam,oszlop,sor,nev,ar,alapfizu,tulajdonos,tipus,szint,jelzalog):
        self.szam = szam
        self.oszlop = oszlop
        self.sor = sor
        self.nev = nev
        self.ar = ar
        self.alapfizu = alapfizu
        self.tulaj = tulajdonos
        self.tipus = tipus
        self.szint = szint
        self.jelzalog = jelzalog
    def korfolytatas(self,player,item):
        if item.szam == player.hely:
            print(item.nev, " mezőn landoltál")
            penzellenorzes()
            html()
            if item.ar == 0:
                kategoria(player,item)
            elif item.tulaj!=player.nev and item.tulaj!="":
                print("Ez a terület az ellenfeledé fizetned kell!!")
                fizetes(player,item)
                mitcsinal(player,item)
            else:
                mitcsinal(player,item)
    def holvan(self,player,item):
        if item.szam == player.hely:
            print(item.nev, " mezőn állsz. Ára:",item.ar," Galleon")
            return

class Szerencse():
    def __init__(self,leiras,kategoria):
        self.leiras = leiras
        self.kategoria = kategoria

class Jatekosok():
    def __init__(self,sorszam,nev,haz,penz,teruletei,hely,borton):
        self.sorszam = sorszam
        self.nev = nev
        self.haz = haz
        self.penz = int(penz)
        self.teruletei = []
        self.hely = int(hely)
        self.borton = borton
    def dobas(self,player):
        a = random.randint(1,6)
        b = random.randint(1,6)
        print("Dobásod:", a,b)
        player.hely += a+b
        if player.hely>40:
            player.hely += -40
            player.penz += 20000
            print("Mivel átlépted a start mezőt kapsz 20000 Galleon-t")
        for jatekosok in jatekos:
            if jatekosok.hely==player.hely and jatekosok.sorszam!=player.sorszam:
                print("Már áll itt egy másik játékos. Így te kiütöd őt")
                jatekosok.hely=1
        return

board = []

def beol():
    f=open("board.txt", "r", encoding="UTF-8")
    f.readline().strip()

    while True:
        sor = f.readline().strip()
        if not sor:
            break
        else:
            a = sor.split(",")
            obj = Board(int(a[0]),int(a[1]),int(a[2]),a[3],int(a[4]),int(a[5]),"",a[6],0,0)
            board.append(obj)

szerencsekartyak = []

def beolszerencse():
    f=open("szerencsekartyak.txt", "r", encoding="UTF-8")
    f.readline().strip()

    while True:
        sor = f.readline().strip()
        if not sor:
            break
        else:
            a = sor.split(",")
            obj = Szerencse(a[0],a[1],)
            szerencsekartyak.append(obj)

jatekos = []

def jatekosok():
    jatekosszam = int(input("Hány játékos van (max.:2)? Játékosok száma:"))
    while jatekosszam>2:
        jatekosszam = int(input("Hány játékos van (max.:2)? Játékosok száma:"))

    if jatekosszam!=1:
        a = 0
        for i in range(0,jatekosszam):
            a+=1
            nev = input("Mi legyen a/az " + str(a) +". játékos neve?")
            haz = ""
            while haz!="Mardekár" and haz!="Griffendél" and haz!="Hugrabug" and haz!="Hollóhát":
                haz = input("Melyik házban szeretnél lenni (Mardekár, Griffendél, Hollóhát, Hugrabug)?")
            obj = Jatekosok(a,nev,haz,100000,"",1,0)
            jatekos.append(obj)
    else:
        nev = input("Mi legyen a neved?")
        haz = ""
        while haz!="Mardekár" and haz!="Griffendél" and haz!="Hugrabug" and haz!="Hollóhát":
            haz = input("Melyik házban szeretnél lenni (Mardekár, Griffendél, Hollóhát, Hugrabug)?")
        obj = Jatekosok(1,nev,haz,100000,"",1,0)
        jatekos.append(obj)
        hazak = ["Mardekár","Griffendél","Hugrabug","Hollóhát"]
        a = random.randint(0,3)
        print("Mi legyen a neved?gep")
        print("Melyik házban szeretnél lenni (Mardekár, Griffendél, Hollóhát, Hugrabug)?")
        print(hazak[a])
        obj = Jatekosok(2,"gep",hazak[a],100000,"",1,0)
        jatekos.append(obj)

def korismetles():
    html()
    while True:
        for player in jatekos:
                penzellenorzes()
                kor(player)
                html()

def kor(player):
    print("\n",player.sorszam,". játékos jön")
    print("Jelenleg ennyi pénzed van: ",player.penz, " Galleon")
    if player.borton==1:
        azkaban(player)
    else:
        if player.nev=="gep":
            print("Nyomj egy ENTER-t a dobáshoz")
            player.dobas(player)
            for item in board:
                item.korfolytatas(player,item)
        else:
            dob = input("Nyomj egy ENTER-t a dobáshoz")
            while dob!="":
                dob = input("Nyomj egy ENTER-t a dobáshoz")
            if dob =="":
                player.dobas(player)
                for item in board:
                    item.korfolytatas(player,item)

def penzellenorzes():
    for player in jatekos:
        if player.penz<=0:
            print(player.penz, " Galleonod van ezzel csődbe mész ha nincs területed amit jelzálogba adhatsz")
            for item in board:
                if player.hely==item.szam:
                    break
            jelzalog(player,item)
    return

def kategoria(player,item):
    if item.tipus=="kvidiccs":
        kvidiccs()
        penzellenorzes()
        mitcsinal(player,item)
    elif item.tipus=="ház":
        hazak(player,item)
        penzellenorzes()
        mitcsinal(player,item)
    elif item.tipus=="szerencse":
        szerencsekartya(player)
        mitcsinal(player,item)
    elif item.tipus=="hoppanálás":
        hoppanalas(player)
        penzellenorzes()
        html()
        mitcsinal(player,item)
    elif item.tipus=="iránybörtön":
        dementorok(player)
        html()
    elif item.tipus=="börtön":
        mitcsinal(player,item)
        html()
    elif item.tipus=="seprű":
        sepru(player)
        html()
    elif item.tipus=="merengő":
        merengo(player)
        penzellenorzes()
        mitcsinal(player,item)
    elif item.tipus=="sárkány":
        sarkany(player,item)
        penzellenorzes()
        mitcsinal(player,item)
    elif item.tipus=="troll":
        troll(player,item)
        penzellenorzes()
        mitcsinal(player,item)
    elif item.tipus=="start":
        mitcsinal(player,item)

def troll(player,item):
    print("Dobj 8-nál többet hogy megmenekülj a torlltól!!")
    if player.nev=="gep":
        print("Nyomj egy ENTER-t a dobáshoz")
        dob=""
    else:
        dob = input("Nyomj egy ENTER-t a dobáshoz")
        while dob!="":
            dob = input("Nyomj egy ENTER-t a dobáshoz")
    if dob =="":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print("Dobásod:", a,b)
        dobottösszeg = a+b
        if dobottösszeg>8:
            print("Sikerült megmenekülnöd a troll elől")
            return
        else:
            print("A troll legyőzött és ellopott tőled", item.alapfizu,"Galleon-t")
            player.penz += -(item.alapfizu)
            print(player.penz)
            return

def sarkany(player,item):
    print("Dobj 10-nél többet hogy megmenekülj a sárkánytól!!")
    for i in range(0,3):
        if player.nev=="gep":
            print("Nyomj egy ENTER-t a dobáshoz")
            dob = ""
        else:
            dob = input("Nyomj egy ENTER-t a dobáshoz")
            while dob!="":
                dob = input("Nyomj egy ENTER-t a dobáshoz")
        if dob =="":
            a = random.randint(1,6)
            b = random.randint(1,6)
            print("Dobásod:", a,b)
            dobottösszeg = a+b
            if dobottösszeg>10:
                print("Sikerült megmenekülnöd a sárkány elől")
                break
            else:
                if i==2:
                    print("Nem sikerült megmenekülnöd. A sárkány legyőzött a kórházi költségek pedig ",item.alapfizu,"Galleon-ba fog kerülni")
                    player.penz += -item.alapfizu
                    return
                else:
                    print("Nem sikerült ",i+1,".-ra/re megmenekülnöd. Dobj újra!")
    return

def dementorok(player):
    print("A dementorok elkaptak és elvisznek téged az Azkabanba")
    player.hely = 11
    player.borton = 1

def azkaban(player):
    print("Börtönben vagy")
    if player.bortonkartya>0:
        if player.nev=="gep":
            print("Van ingyen szabadulhatsz a börtönből kártyád. Felszeretnéd használni?")
            valasz = random.randint(1,2)
            if valasz=="1":
                felhasznaljae=="Igen"
            elif valasz=="2":
                felhasznaljae=="Nem"
        else:
            felhasznaljae = input("Van ingyen szabadulhatsz a börtönből kártyád. Felszeretnéd használni?")
            while felhasznaljae!="Igen" and felhasznaljae!="Nem" and felhasznaljae!="igen" and felhasznaljae!="nem":
                felhasznaljae = input("Van ingyen szabadulhatsz a börtönből kártyád. Felszeretnéd használni?")
        if felhasznaljae=="Igen" or felhasznaljae=="igen":
            if player.nev=="gep":
                print("Nyomj egy ENTER-t a dobáshoz")
                dob = ""
            else:
                dob = input("Nyomj egy ENTER-t a dobáshoz")
                while dob!="":
                    dob = input("Nyomj egy ENTER-t a dobáshoz")
            if dob =="":
                player.dobas(player)
                for item in board:
                    item.korfolytatas(player,item)
    print("Börtönben vagy. Dobj dupla számot és ingyen kikerülsz")
    if player.nev=="gep":
        print("Nyomj egy ENTER-t a dobáshoz")
        dob = ""
    else:
        dob = input("Nyomj egy ENTER-t a dobáshoz")
        while dob!="":
            dob = input("Nyomj egy ENTER-t a dobáshoz")
    if dob =="":
        a = random.randint(1,6)
        b = random.randint(1,6)
        print("Dobásod:", a,b)
        if a==b:
            print("Kiszabadultál a börtönből fizetés nélkül")
            player.hely +=a+b
            player.borton = 0
        else:
            print("Fizetned kell a kijutásért 2000 Galleon-t")
            player.penz += -2000
            player.borton = 0

def kvidiccs():
    print("Ezen a mezőn az ellenfeled/ellenfeleid ellen fogsz játszani. Ha 3 kör alatt te dobsz többet akkor te nyersz ha nem akkor te fizetsz")
    dobas = 0
    masikdobas = 0
    nyertes = 1
    for jatekosok in jatekos:
        print(jatekosok.nev,"játékos dob")
        for i in range(0,3):
            if jatekosok.nev=="gep":
                print("Nyomj egy ENTER-t a dobáshoz")
                dob=""
            else:
                dob = input("Nyomj egy ENTER-t a dobáshoz")
                while dob!="":
                    dob = input("Nyomj egy ENTER-t a dobáshoz")
            if dob =="" and jatekosok.sorszam==1:
                a = random.randint(1,6)
                b = random.randint(1,6)
                print("Dobásod:", a,b)
                dobas += a+b
                print("Eddigi összesített dobásod:",dobas)
            elif dob == "":
                a = random.randint(1,6)
                b = random.randint(1,6)
                print("Dobásod:", a,b)
                masikdobas += a+b
                print("Eddigi összesített dobásod:",masikdobas)
        if masikdobas>dobas:
            dobas = masikdobas
            masikdobas = 0
            nyertes = jatekosok.sorszam
        elif masikdobas<dobas:
            masikdobas = 0
    jatekosszam = 0
    for jatekosok in jatekos:
        jatekosszam += 1
    for jatekosok in jatekos:
        if nyertes==jatekosok.sorszam:
            print("A nyertes:",jatekosok.nev," játékos")
            print("Ezért mindenki fizet 1000 Galleon-t neki")
            jatekosok.penz += 1000*jatekosszam-1
        else:
            jatekosok.penz += -1000
    return

def hazak(player,item):
    if player.haz in item.nev:
        print("Mivel a saját házadra léptél ezért kapsz 2000 Galleont")
        player.penz += 2000
    else:
        print("Mivel nem a saját házadra léptél ezért fizetned kell 1000 Galleont")
        player.penz += -1000
    return

def sepru(player):
    print("Előre repülsz 3-mat")
    player.hely += 3
    for item in board:
        item.korfolytatas(player,item)

def hoppanalas(player):
    if player.hely==13:
        player.hely=29
        print("Elhoppanáltál a másik hoppanálás mezőre")
        return
    else:
        player.hely=13
        print("Elhoppanáltál a másik hoppanálás mezőre")
        return
    """for item in board:
        if player.hely==item.szam:
            for mezo in board:
                if mezo.nev=="Hoppanálás" and mezo.szam!=item.szam:
                    player.hely = mezo.szam
                    print("Elhoppanáltál egy másik hoppanálás mezőre")
                    return"""

def merengo(player):
    szerencsevagynem = random.randint(1,2)
    if szerencsevagynem==1:
        print("Belenézel a merengőbe és egy boldog emléket látsz. Ez boldogsággal tölt el téged.")
        if player.nev=="gep":
            print("Nyomj egy ENTERT hogy begyűjtsd a nyereményt")
            megkap=""
        else:
            megkap = input("Nyomj egy ENTERT hogy begyűjtsd a nyereményt")
            while megkap!="":
                megkap = input("Nyomj egy ENTERT hogy begyűjtsd a nyereményt")
        print("+15000 Galleon")
        player.penz += 15000
    else:
        print("Belenézel a merengőbe és elborzadsz mivel egy ember kivégzésének emlékét látod")
        if player.nev=="gep":
            print("Nyomj egy ENTERT hogy begyűjtsd a veszteséget")
            elveszt=""
        else:
            elveszt = input("Nyomj egy ENTERT hogy begyűjtsd a veszteséget")
            while elveszt!="":
                elveszt = input("Nyomj egy ENTERT hogy begyűjtsd a veszteséget")
        print("-15000 Galleon")
        player.penz += -15000

def szerencsekartya(player):
    if player.nev=="gep":
        print("Nyomj egy ENTERT a húzáshoz")
        huzas = ""
    else:
        huzas = input("Nyomj egy ENTERT a húzáshoz")
        while huzas!="":
            huzas = input("Nyomj egy ENTERT a húzáshoz")
    if huzas=="":
        melyiklegyen = random.randint(1,len(szerencsekartyak))
        print(szerencsekartyak[melyiklegyen-1].leiras)
        if szerencsekartyak[melyiklegyen-1].kategoria=="szabadsag":
            player.borton += 1
            return
        elif szerencsekartyak[melyiklegyen-1].kategoria=="lepj":
            for item in board:
                if item.nev == "Rejtély- és Misztériumügyi Főosztály":
                    player.hely = item.szam
        elif szerencsekartyak[melyiklegyen-1].kategoria=="penz":
            player.penz += 10000
        elif szerencsekartyak[melyiklegyen-1].kategoria=="gringotts":
            player.penz += 5000
        elif szerencsekartyak[melyiklegyen-1].kategoria=="hazra":
            for item in board:
                if player.haz in item.nev:
                    player.hely = item.szam

def fizetes(player,item):
    print(item.alapfizu," Galleont kell fizetned")
    player.penz += -item.alapfizu
    print(player.penz, " Galleonod maradt")
    return

def mitcsinal(player,item):
    if player.nev=="gep":
        valasz = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,4,4,4,4,4,5]
        valaszszam = random.randint(0,20)
        print("Mit szeretnél csinálni? Válasz:")
        if valasz[valaszszam]==1:
            print("terület vásárlás")
            mitcsinal="terület vásárlás"
        elif valasz[valaszszam]==2:
            print("terület fejlesztés")
            mitcsinal="terület fejlesztés"
        elif valasz[valaszszam]==3:
            print("jelzálog")
            mitcsinal="jelzálog"
        elif valasz[valaszszam]==4:
            print("kör vége")
            mitcsinal="kör vége"
        else:
            print("feladom")
            mitcsinal="feladom"
    else:
        mitcsinal = ""
    while mitcsinal!="terület vásárlás" and mitcsinal!="terület fejlesztés" and mitcsinal!="jelzálog" and mitcsinal!="kör vége" and mitcsinal!="feladom":
        mitcsinal = input("Mit szeretnél csinálni (Lehetősége: terület vásárlás, terület fejlesztés, jelzálog, kör vége, feladom)? Válasz:")

    if mitcsinal=="terület vásárlás":
        teruletvasarlas(player,item)
    elif mitcsinal=="terület fejlesztés":
        teruletfejlesztes(player,item)
    elif mitcsinal=="jelzálog":
        jelzalog(player,item)
    elif mitcsinal=="kör vége":
        print("Vége a körödnek")
    elif mitcsinal=="feladom":
        jatekvege(player)

def teruletvasarlas(player,item):
    if item.tulaj=="" and item.ar!=0:
        item.holvan(player,item)
        if player.nev=="gep":
            lehetosegek = [1,1,1,1,1,1,1,2]
            valasz = random.randint(1,8)
            print("Biztosan meg szeretnéd venni?")
            if lehetosegek[valasz]==1:
                print("Igen")
                megveszi="Igen"
            else:
                print("Nem")
                megveszi="Nem"
        else:
            megveszi = input("Biztosan meg szeretnéd venni?")
            while megveszi!="Igen" and megveszi!="igen" and megveszi!="Nem" and megveszi!="nem":
                megveszi = input("Biztosan meg szeretnéd venni?")
        if megveszi=="Igen" or megveszi=="igen":
            ell = player.penz-item.ar
            if ell>0:
                player.penz += -item.ar
                print("Mostmár tied a",item.nev,"terület")
                player.teruletei.append(item.nev)
                item.tulaj = player.nev
                print(item.tulaj,*player.teruletei,player.penz)
                mitcsinal(player,item)
            else:
                print("Nincs elég pénzed a területre")
                mitcsinal(player,item)
        else:
            mitcsinal(player,item)       
    else:
        print("A terület amin állsz nem megvásárolható")
        mitcsinal(player,item)

def teruletfejlesztes(player,item):
    szintek = [0,1,2,3,4]
    szorzo = [30,40,50,70,80]
    if player.teruletei!=[]:
        print("Ezek a területeid: ",*player.teruletei)
        if player.nev=="gep":
            print("Melyik területed szeretnéd fejleszteni?")
            szeretnee = random.randint(1,2)
            if szeretnee==1:
                melyikterulet = random.randint(0,len(player.teruletei))
                fejlesztendoterulet = player.teruletei[melyikterulet-1]
                print(fejlesztendoterulet)
            else:
                fejlesztendoterulet="Mégse"
                print("Mégse")
        else:
            fejlesztendoterulet = input("Melyik területed szeretnéd fejleszteni?")
            while fejlesztendoterulet!="Mégse" and fejlesztendoterulet!="mégse" and fejlesztendoterulet not in player.teruletei:
                fejlesztendoterulet = input("Nem megfelelő területet adtál meg! Melyik területed szeretnéd fejleszteni?")
        if fejlesztendoterulet=="Mégse" or fejlesztendoterulet=="mégse":
            mitcsinal(player,item)
        else:
            for mezo in board:
                if mezo.nev == fejlesztendoterulet and mezo.nev in player.teruletei:
                    print(mezo.nev,"terület jelenlegi szintje:",mezo.szint)
                    for szam in szintek:
                        if szam==mezo.szint:
                            fejlesztesar = mezo.ar/100*szorzo[szam]
                            print("A fejlesztés",fejlesztesar,"Galleonba fog kerülni")
                            if player.nev=="gep":
                                szamok = [1,1,1,1,2]
                                index = random.randint(1,5)
                                if szamok[index]==1:
                                    print("Biztos fejleszteni szeretnéd?")
                                    biztosebenne="Igen"
                                    print("Igen")
                                else:
                                    print("Biztos fejleszteni szeretnéd?")
                                    biztosebenne = "Nem"
                                    print("Nem")
                            else:
                                biztosebenne = input("Biztos fejleszteni szeretnéd?")
                                while biztosebenne!="Igen" and biztosebenne!="igen" and biztosebenne!="Nem" and biztosebenne!="nem":
                                    biztosebenne = input("Biztos fejleszteni szeretnéd?")
                            if biztosebenne=="Igen" or biztosebenne=="igen":
                                ell = player.penz-fejlesztesar
                                if ell>0:
                                    mezo.szint += 1
                                    player.penz += -fejlesztesar
                                    mezo.alapfizu = mezo.alapfizu*szorzo[szam]/20
                                    print("Sikeresen fejlesztetted a területet")
                                    mitcsinal(player,item)
                                    break
                                else:
                                    print("Nincs elég pénzed a fejlesztésre")
                                    mitcsinal(player,item)
                            else:
                                mitcsinal(player,item)
    else:
        print("Nincs fejleszthető területed")
        mitcsinal(player,item)

def jelzalog(player,item):
    if player.penz>0:
        if player.teruletei!=[]:
            print("Ezek a területeid: ",*player.teruletei)
            if player.nev=="gep":
                print("Melyik területed szeretnéd jelzálogba tenni?")
                szeretnee = random.randint(1,2)
                if szeretnee==1:
                    melyikterulet = random.randint(0,len(player.teruletei))
                    jelzalograadando = player.teruletei[melyikterulet-1]
                    print(jelzalograadando)
                else:
                    jelzalograadando="Mégse"
                    print("Mégse")
            else:
                jelzalograadando = input("Melyik területed szeretnéd jelzálogba tenni?")
                while jelzalograadando not in player.teruletei and jelzalograadando!="Mégse" and jelzalograadando!="mégse":
                    jelzalograadando = input("Nem megfelelő területet adtál meg! Melyik területed szeretnéd jelzálogba tenni?")
            for mezo in board:
                if jelzalograadando==mezo.nev and jelzalograadando in player.teruletei and mezo.jelzalog!=1:
                    jelzalogertek = (mezo.ar*(mezo.szint+1))/10
                    print(jelzalogertek,"Galleon jelzálogot fogsz kapni")
                    biztosebenne = input("Biztos jelzálogba szeretnéd tenni?")
                    if biztosebenne=="Igen":
                        mezo.jelzalog = 1
                        player.penz += jelzalogertek
                        print("Sikeresen jelzálogba raktad. Jelenlegi pézed:",player.penz," Galleon")
                        mitcsinal(player,item)
                    else:
                        mitcsinal(player,item)
                elif mezo.jelzalog==1 and jelzalograadando in player.teruletei:
                    print("Ez a terület már jelzálog alatt van")
                    mitcsinal(player,item)
                elif jelzalograadando=="Mégse" or jelzalograadando=="mégse":
                    return
        else:
            print("Nincs területed")
            mitcsinal(player,item)
    else:
        a=0
        b=0
        if player.teruletei==[]:
            print("Nincs jelzálogba adható területed")
            jatekvege(player)
        else:
            while player.penz<0:
                for terulet in player.teruletei:
                    a += 1
                    if terulet.jelzalog==1:
                        b+=1
                    if a==b:
                        print("Ennyi pénzed van most:",player.penz, " Galleon")
                        jatekvege(player)
                    elif terulet.jelzalog==0:
                        jelzalogertek = (mezo.ar*(mezo.szint+1))/10
                        mezo.jelzalog = 1
                        player.penz += jelzalogertek
        if player.penz>0:
            kor(player)

def jatekvege(player):
    print("Vége a játéknak")
    for jatekosok in jatekos:
        if jatekosok.nev!=player.nev:
            print(jatekosok.nev," nyert!!")
    exit() 

def html():
    f=open("monopoly.html","w",encoding="UTF-8")
    f.write("<html> <style> td { border:3px solid black;height:70px;} .noborder{border:0}</style><body> <table style='width:100%'>")
    
    for item in board:
        if item.oszlop == 1:
            if item.tipus=="seprű":
                f.write("<td style='background-color:#482311; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="troll":
                f.write("<td style='background-color:#568831; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="ház":
                if "Hollóhát" in item.nev:
                    f.write("<td style='background-color:#154bd7; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Griffendél" in item.nev:
                    f.write("<td style='background-color:#d71515; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Mardekár" in item.nev:
                    f.write("<td style='background-color:#0b4a04; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Hugrabug" in item.nev:
                    f.write("<td style='background-color:#e7bf19; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="szerencse":
                f.write("<td style='background-color:#fcff66; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="börtön":
                f.write("<td style='background-color:#484747; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="sárkány":
                f.write("<td style='background-color:#3a0404; color:white; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="hoppanálás":
                f.write("<td style='background-color:#bcbcbc; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="merengő":
                f.write("<td style='background-color:#1e9eba; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="iránybörtön":
                f.write("<td style='background-color:black; color: white; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="kvidiccs":
                f.write("<td style='background-color:#8357c8; text-align:center'> <h3>" + item.nev + "</h3> \n")
            else:
                f.write("<tr> <td style='background-color:#e6e4e9; text-align:center'> <h3>" + item.nev + "</h3> \n")
            if item.ar!=0:
                f.write(str(item.ar) + " Galleon")
            for player in jatekos:
                if player.hely==item.szam:
                    f.write("👤" + player.nev + "(" + player.haz + ")")
            f.write("</td>")
            if 1<item.sor<11:
                for i in range(0,9):
                    f.write("<td class='noborder'> </td>")
        elif item.oszlop == 11:
            if item.tipus=="seprű":
                f.write("<td style='background-color:#482311; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="troll":
                f.write("<td style='background-color:#568831; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="ház":
                if "Hollóhát" in item.nev:
                    f.write("<td style='background-color:#154bd7; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Griffendél" in item.nev:
                    f.write("<td style='background-color:#d71515; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Mardekár" in item.nev:
                    f.write("<td style='background-color:#0b4a04; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Hugrabug" in item.nev:
                    f.write("<td style='background-color:#e7bf19; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="szerencse":
                f.write("<td style='background-color:#fcff66; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="börtön":
                f.write("<td style='background-color:#484747; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="sárkány":
                f.write("<td style='background-color:#3a0404; color:white; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="hoppanálás":
                f.write("<td style='background-color:#bcbcbc; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="merengő":
                f.write("<td style='background-color:#1e9eba; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="iránybörtön":
                f.write("<td style='background-color:black; color: white; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="kvidiccs":
                f.write("<td style='background-color:#8357c8; text-align:center'> <h3>" + item.nev + "</h3> \n")
            else:
                f.write("<td style='background-color:#e6e4e9; text-align:center'> <h3>" + item.nev + "</h3> \n")
            if item.ar!=0:
                f.write(str(item.ar) + " Galleon")
            for player in jatekos:
                if player.hely==item.szam:
                    f.write("👤" + player.nev + "(" + player.haz + ")")
            f.write("</td> </tr>")
        else:
            if item.tipus=="seprű":
                f.write("<td style='background-color:#482311; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="troll":
                f.write("<td style='background-color:#568831; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="ház":
                if "Hollóhát" in item.nev:
                    f.write("<td style='background-color:#154bd7; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Griffendél" in item.nev:
                    f.write("<td style='background-color:#d71515; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Mardekár" in item.nev:
                    f.write("<td style='background-color:#0b4a04; text-align:center'> <h3>" + item.nev + "</h3> \n")
                elif "Hugrabug" in item.nev:
                    f.write("<td style='background-color:#e7bf19; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="szerencse":
                f.write("<td style='background-color:#fcff66; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="börtön":
                f.write("<td style='background-color:#484747; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="sárkány":
                f.write("<td style='background-color:#3a0404; color:white; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="hoppanálás":
                f.write("<td style='background-color:#bcbcbc; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="merengő":
                f.write("<td style='background-color:#1e9eba; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="iránybörtön":
                f.write("<td style='background-color:black; color: white; text-align:center'> <h3>" + item.nev + "</h3> \n")
            elif item.tipus=="kvidiccs":
                f.write("<td style='background-color:#8357c8; text-align:center'> <h3>" + item.nev + "</h3> \n")
            else:
                f.write("<td style='background-color:#e6e4e9; text-align:center'> <h3>" + item.nev + "</h3> \n")
            if item.ar!=0:
                f.write(str(item.ar) + " Galleon")
            for player in jatekos:
                if player.hely==item.szam:
                    f.write("👤" + player.nev + "(" + player.haz + ")")
            f.write("</td>")

    f.write("</table> </body> </html>")

def main():
    beol()
    beolszerencse()
    jatekosok()
    html()
    korismetles()

main()
