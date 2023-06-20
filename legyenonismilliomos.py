import random

class Txt:
    def __init__(self,szam,kerdes,A,B,C,D,megoldas,tema):
        self.szam = szam
        self.kerdes = kerdes
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.megoldas = megoldas
        self.tema = tema
    def __str__(self):
        return f"{self.kerdes}{self.A}{self.B}{self.C}{self.D}{self.megoldas}{self.tema}"
    
    def kiiras(self):
        print(f"    A: {self.A}, B: {self.B} \n    C: {self.C}, D: {self.D}\n")
    
    def felezettA(self):
        print(f"    A: {self.A}, B: - \n    C: -, D: {self.D}\n")
    
    def felezettB(self):
        print(f"    A: -, B: {self.B} \n    C: -, D: {self.D}\n")
    
    def felezettC(self):
        print(f"    A: -, B: {self.B} \n    C: {self.C}, D: -\n")
    
    def felezettD(self):
        print(f"    A: -, B: - \n    C: {self.C}, D: {self.D}\n")

def kezdes(kerdesek):
    print("Üdvözöllek a Legyen ön is milliomos játékban!!")
    nev = input("Mi a neved? Neved:")
    print(f"\nSzia, {nev}!")
    k1(kerdesek, nev)

def segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon):
    svalasz= input("Melyik segítséget szeretnéd? (felezés,közönség,telefonos segítség)\nVálasz:")
    svalasz.capitalize()
    if svalasz=="felezés" and felező==1:
        felező=0
        if item.megoldas=="A":
            print(kerdes[index])
            item.felezettA()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)   
        elif item.megoldas=="B":
            print(kerdes[index])
            item.felezettB()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)        
        elif item.megoldas=="C":
            print(kerdes[index])
            item.felezettC()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
        elif item.megoldas=="D":
            print(kerdes[index])
            item.felezettD()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)                  
    elif svalasz=="felezés" and felező==0:
        print("Nincs több feleződ")
        uvalasz=input("Szeretnél másik segítséget? (kisbetűvel írd)")
        if uvalasz=="igen":
            segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező)
        else:
            feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif svalasz=="közönség" and közönseg==1:
        list1 = [1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,2]
        indexk = random.randint(0,len(list1))
        közönseg=0
        if item.megoldas=="A":
            if list1[indexk]==1:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: A (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)  
           
            else:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: D (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)           
        elif item.megoldas=="B":
            if list1[indexk]==1:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: B (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)        
            else:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: A (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)  
        elif item.megoldas=="C":
            if list1[indexk]==1:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: C (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)  

            else:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: D (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)  

        elif item.megoldas=="D":
            if list1[indexk]==1:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: D (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)  

            else:
                print(kerdes[index])
                item.kiiras()
                print("A közönség szerint a megoldás: C (lehet hamis a megoldásuk)")
                jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
                if jvalasz==item.megoldas:
                    print(f"\nGratulálok {nev}, helyes a válasz!!!")
                    print(f"Nyertél: {jnyeremeny}Ft-ot")
                    nyeremeny=jnyeremeny
                    jnyeremeny+=5000
                    print("\nJön a következő kérdés!")
                    a+=1
                    feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
                else:
                    vege(item, nyeremeny)  
    elif svalasz=="közönség" and közönseg==0:
        print("Nincs több segítséged a közönségtől")
        kvalasz=input("Szeretnél másik segítséget?")
        if kvalasz=="igen":
            segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező)
        else:
            feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    if svalasz=="telefonos segítség" and telefon==1:
        telefon=0
        list2 = [1,1,2]
        anya = random.randint(0,len(list2))
        if anya==1:
            apa= random.randint(0,len(list2))
            if apa==1:
                Bözsi = 2
            else:
                Bözsi = 1
        else:
            apa = 1
            Bözsi = 1
                   
        tvalasz= input("Kit szeretnél hívni? \nAnyukád \nApukád \nBözsi \nVálasz (Anyát,Apát vagy Bözsit legyen a válasz kérlek):")
        if tvalasz=="Anyát" and anya==1:
            print(kerdes[index])
            item.kiiras()
            print(f"Anyukád szerint a megoldás {item.megoldas} (lehet hamis a megoldása)")
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
        elif tvalasz=="Anyát" and anya==2:
            print(kerdes[index])
            item.kiiras()
            print("Anyukád szerint a megoldás B (lehet hamis a megoldása)")
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
        elif tvalasz=="Apát" and apa==1:
            print(kerdes[index])
            item.kiiras()
            print(f"Apukád szerint a megoldás {item.megoldas} (lehet hamis a megoldása)")
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
        elif tvalasz=="Apát" and apa==2:
            print(kerdes[index])
            item.kiiras()
            print("Apukád szerint a megoldás C (lehet hamis a megoldása)")
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
        if tvalasz=="Bözsit" and Bözsi==1:
            print(kerdes[index])
            item.kiiras()
            print(f"Bözsi szerint a megoldás {item.megoldas} (lehet hamis a megoldása)")
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
        elif tvalasz=="Bözsit" and Bözsi==2:
            print(kerdes[index])
            item.kiiras()
            print("Bözsi szerint a megoldás A (lehet hamis a megoldása)")
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D)\nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            else:
                vege(item, nyeremeny)  
    elif svalasz=="telefonos segítség" and telefon==0:
        print("Nincs több telefonos segítséged")
        uvalasz=input("Szeretnél másik segítséget? (kisbetűvel írd)")
        if uvalasz=="igen":
            segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező)
        else:
            feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif svalasz!="felezés" and svalasz!="közönség" and svalasz!="telefonos segítség":
        print("elírtad a lehetőségek:felezés,közönség,telefonos segítség")
        uvalasz=input("Szeretnél segítséget használni? (kisbetűvel írd)")
        if uvalasz=="igen":
            segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon)
        else:
            feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)

def feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):
    if a==1:
        k1(kerdesek, nev)
    elif a==2:
        k2(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==3:
        k3(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==4:
        k4(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==5:
        k5(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==6:
        k6(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==7:
        k7(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==8:
        k8(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==9:
        k9(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==10:
        k10(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==11:
        k11(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==12:
        k12(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==13:
        k13(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==14:
        k14(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
    elif a==15:
        k15(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)

def eliras(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon):
    print("elírtad a lehetőségek:felezés,közönség,telefonos segítség")
    uvalasz=input("Szeretnél segítséget használni? (kisbetűvel írd)")
    if uvalasz=="igen":
        segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon)
    else:
        feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)

def vege(item, nyeremeny):
    print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
    print(f"\nNyereményed {nyeremeny}Ft")

def k1(kerdesek, nev):

    a = 1
    nyeremeny = 0
    jnyeremeny = 5000
    felező = 1
    közönseg = 1
    telefon = 1
    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon)
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k2(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=10000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k3(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=25000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k4(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=50000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k5(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=100000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k6(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=100000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k7(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=200000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k8(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=300000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k9(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=700000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k10(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=1500000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k11(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=2000000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break 

def k12(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=5000000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k13(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=10000000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break
    
def k14(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálok {nev}, helyes a válasz!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot")
                nyeremeny=jnyeremeny
                jnyeremeny+=20000000
                print("\nJön a következő kérdés!")
                a+=1
                feladatv(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon)
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def k15(kerdesek, jnyeremeny, nev, nyeremeny, a, felező, közönseg, telefon):

    kerdes = []

    print(f"Most az {a}. kérdés jön")
    print(f"Ez a kérdés {jnyeremeny}Ft-ért megy \n")
    print(f"{a}. kérdés")

    for item in kerdesek:
        if item.szam==a:
            kerdes.append(item.kerdes)

    index= random.randint(0,len(kerdes))
    print(kerdes[index])

    for item in kerdesek:
        if item.kerdes==kerdes[index]:
            item.kiiras()
            jvalasz= input(f"Melyik megoldást szeretné megjelölni {nev}? (A, B, C vagy D) \n(Ha nem tudod és van még segítséged írd be hogy segítség) \nVálasz:")
            jvalasz.capitalize()
            if jvalasz==item.megoldas:
                print(f"\nGratulálooooooook {nev}, ez is helyes!!!!!!")
                print(f"{nev} megnyerte a játékot!!!!!")
                print(f"Nyertél: {jnyeremeny}Ft-ot!!!!!!")
                nyeremeny=jnyeremeny
            elif jvalasz=="segítség":
               segitseg(kerdesek, jnyeremeny, nev, nyeremeny, a, item, kerdes, index, felező, közönseg, telefon) 
            else:
                print(f"\nMegoldás:{item.megoldas} \nSajnálom ez nem sikerült :'(")
                print(f"\nNyereményed {nyeremeny}Ft")
                break

def main():
    kerdesek=[]
    f=open("kerdes.txt", encoding="UTF-8")
    while True:
        sor = f.readline().strip()
        if not sor:

            break
        else:
            x = sor.split(";")
            idk=Txt(int(x[0]), x[1], x[2], x[3], x[4], x[5], x[6], x[7])
            kerdesek.append(idk)
    kezdes(kerdesek)

main()
