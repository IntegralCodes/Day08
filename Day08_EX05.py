class Snack:
    companyName = "해태"

    def __init__(self, n, p):
        self.name = n
        self.price = p

    def info(self):
        print("{}는(은) {}원이고, 제조 회사는 {}입니다.".format(self.name, self.price, self.companyName))


pepero = Snack("빼빼로", 1500)
pepero.info()


