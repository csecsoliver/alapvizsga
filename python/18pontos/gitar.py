class Guitar:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        self.nev = str(splitted[0])
        self.tipus = str(splitted[1])
        self.gyarto = str(splitted[2])
        self.hurok_szama = int(splitted[3])
        self.ertekeles = float((splitted[4]).replace(',','.'))
        self.ar = int(splitted[5])

        
