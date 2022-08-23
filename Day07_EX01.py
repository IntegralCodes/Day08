class Player: #플레이어라는 클래스 설명서를 작성한거임

    def play(self):
        print("{} 선수 ({}세) 경기에 출전합니다.".format(self.name,self.age))

    def __init__(self, n, a):
        self.name = n
        self.age = a



sonny = Player("손흥민", 30)
sonny.play()

