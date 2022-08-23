class Queue:
    def __init__(self):
        self.front = 0 # 빨간 화살표
        self.rear = 0 #  파란 화살표
        self.size = 5 # 큐의 크기
        self.queue = [None] * 5

    def isEmpty(self):
        if self.front == self.rear :
            return True

        else:
            return False

    def isFull(self):
        if self.front == self.rear + 1:
            return True
        else:
            return False

    #rear가 front 보다 한칸 전에 있으면
    #rear == front - 1
    #front 가 rear보다 한칸 뒤에 있으면
    #front == rear + 1

    def enqueue(self, item):
        self.queue[self.rear] = item     # item을 rear(파란화살표 자리)에 넣어주는 거
        self.rear = self.rear + 1         # rear 가 한칸 전진


    def dequeue(self):
        self.queue[self.front] = [None]
        self.front = self.front + 1


