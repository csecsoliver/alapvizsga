from gitar import Guitar

guitarlist : list[Guitar] = []

def main():
    beolvas('gitarok.csv')
    print(f'Gitárok száma a boltban: {len(guitarlist)}')
    print(f'P-Bass típusú gitárok száma: {osszeszamolas("Precision Bass")}')
    print(f'Legdrágább gitár neve: {legdragabb().nev}')
    print(f'Legdrágább gitár típusa: {legdragabb().tipus}')
    print(f'legdrágább gitár ára: {legdragabb().ar} Ft')
    print(f'6 húros gitárok:')
    hathur()
    print(f'Gibson gitár értékelések átlaga: {gibsonatlag()}')
    nev = str(input('Keresett gitár: '))
    keres(nev)
    fajlbairas()
def beolvas(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        guitarlist.append(Guitar(row))
    file.close()

def osszeszamolas(gyarto):
    count = 0
    for g in guitarlist:
        if g.tipus == gyarto:
            count += 1
    return count

def legdragabb():
    dragabb = guitarlist[1]
    for g in guitarlist:
        if g.ar > dragabb.ar:
            dragabb = g
    return dragabb

def hathur():
    for g in guitarlist:
        if g.hurok_szama == 6:
            print(f'{g.nev}')



def gibsonatlag():
    atlag = 0
    count = 0
    for g in guitarlist:
        if g.gyarto == 'Gibson':
            atlag += g.ertekeles
            count += 1
    return atlag / count

def fajlbairas():
    file = open('Fender.txt', 'w', encoding='utf-8')
    for g in guitarlist:
        if 'Fender' in g.gyarto:
            file.write(f'{g.nev} - {g.tipus} - {g.gyarto} \n')
    file.close()

def keres(nev):
    for g in guitarlist:
        if g.nev == nev:
            print('Kapható ilyen gitár.')
            break
    else:
        print('Nem kapható ilyen gitár.') 

main()

    



