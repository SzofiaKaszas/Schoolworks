class Filmek():
    def __init__(self,sor):
        s=sor.strip().split(";")
        self.title=s[0]
        self.titleurl=s[1]
        self.image=s[2]
        self.rate=s[3].replace(".","")
        self.year=s[4]
        self.certificate=s[5]
        self.time=s[6]
        self.genres=s[7].replace(" ","").split(",")
        self.rating=s[8].replace(",",".")
        self.content=s[9]
        self.director=s[11]
        self.directorurl=s[10]
        self.star1=s[13]
        self.star1url=s[12]
        self.star2=s[15]
        self.star2url=s[14]
        self.star3=s[17]
        self.star3url=s[16]
        self.star4=s[19]
        self.star4url=s[18]
        self.votes=s[20]
        self.gross=s[21]

filmek=[]

def beolvasas():
    f=open("filmek.csv", encoding="UTF-8")
    sor=f.readline()
    while True:
        sor=f.readline()
        if not sor:
            break
        else:
            obj=Filmek(sor)
            filmek.append(obj)

def html():
    f=open("filmek.html", "w", encoding="UTF-8")
    elso = open("1.html", encoding="UTF-8")
    masodik = open("2.html", encoding="UTF-8")
    harmadik = open("3.html", encoding="UTF-8")

    for item in elso:
        f.write(item)
    
    for item in filmek:
        masodik = open("2.html", encoding="UTF-8")
        for adat in masodik:
            if item.gross=="":
                item.gross="nincs adat"
            csere=adat.replace("#cim", item.title).replace("cimurl", item.titleurl).replace("#rendezo", item.director).replace("rendezourl",item.directorurl).replace("evecske", item.year).replace("hossz", item.time).replace("ertekeles", item.rate).replace("iplratingstar", item.rating).replace("szavazatok", item.votes).replace("gross", item.gross).replace("tartalom", item.content).replace("#szinesz1", item.star1).replace("szinesz1url", item.star1url).replace("#szinesz2", item.star2).replace("szinesz2url", item.star2url).replace("#szinesz3", item.star3).replace("szinesz3url", item.star3url).replace("#szinesz4", item.star4).replace("szinesz4url", item.star4url).replace("#kep", item.image)
            f.write(csere)

    for item in harmadik:
        f.write(item)

def main():
    beolvasas()
    html()

main()
