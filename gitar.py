class Guitar:
    def __init__(self, row: str) -> None:
        splitted = row.split(';')
        self.nev = str(splitted[0])
        self.tipus = splitted[1]
        self.hurok_szama = splitted[2]
        self.gyartasi_datum = splitted[3]
        self.ar = splitted[4]
        
