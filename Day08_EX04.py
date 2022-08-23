class beer:
    company = "로대"

    def __init__(self,n):
        self.name = n

    def ad(self):
        print("맥주이름은 {}이고, 제조회사는 {}입니다.".format(self.name, beer.company))

kloud = beer("클라우드")
fitz =  beer("피츠")