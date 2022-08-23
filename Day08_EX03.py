class Family:
    address = ""

    def __init__(self, n, a):
        self.name = n
        Family.address = a

    def info(self):
        print("저는 {} 이구요, {}에 살고 있어요.".format(self.name, self.address))

    def move(self, a):
        self.address = a

father = Family("아빠", "서울")
father.move("부산")
father.info()
son = Family("아들", "서울")
son.info()

