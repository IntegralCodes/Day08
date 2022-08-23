class Member: #나는 개똥벌래
    def __init__(self, n, m):
        self.name = n
        self.count = m
    def enter(self):
        print("회원 {}님 이 입장하였습니다.".format(self.name))
        self.count = self.count + 1
        print("{}님 입장 횟수는 {}회 입니다.".format(self.name, self.count))

jong = Member("종민", 0)
jong.enter()
jong.enter()
jong.enter()

tom = Member("톰", 0)
tom.enter()
tom.enter()
