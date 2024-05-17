from gitar import Guitar

guitarlist : list[Guitar] = []

def beolvas(filename):
    file = open(filename, 'r', encoding='utf-8')
    file.readline()
    for row in file:
        guitarlist.append(Guitar(row))
    file.close()

def main():
    beolvas('gitarok.csv')
    print(f'Gitárok száma a boltban: {len(guitarlist)}')
main()