"""
一般机场里，航班到达后，旅客们会去到达区的行李传送带那里取自己的行李。
现假设有一座特别的机场，每条传送带只有一个取行李的窗口。旅客们必须排好队，逐一到窗口取自己的行李。但是当某人到窗口前，
发现行李不是自己的，那人就只好走到队尾去等下一次机会。此时那件行李会一直等在窗口，
直到它的主人把它取走。假设每一次认领需要 1 分钟，本题就要求你计算传送带清空需要的时间、以及旅客们的平均等待时间。
例如，假设行李 i 属于旅客 i。行李的到达顺序是 1、2、3，旅客的到达顺序是 2、1、3。
则 1 号行李要等 2 分钟才能被主人 1 号旅客取走。这时行李队列中有 2、3，旅客队列中是 3、2。
于是 2 号行李还要等 2 分钟才能被 2 号旅客取走，最后 3 号在第 5 分钟取走行李。旅客们的平均等待时间是 (2+4+5)/3≈3.7
"""
class Queue:
    def __init__(self, kMaxSize):
        self.kMaxSize = kMaxSize
        self.size = 0
        self.front = 0
        self.rear = 0
        self.data = [0] * self.kMaxSize

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.kMaxSize

    def enqueue(self, item):
        if self.isFull():
            print("Queue 满")
            return
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.kMaxSize
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            print("Queue 空")
            return None
        self.front = (self.front + 1) % self.kMaxSize
        self.size -= 1
        return self.data[self.front]

    def getFront(self):
        return self.data[self.front]

def calculate_waiting_time(n, passenger_queue:list):
    queue = Queue(n)
    time_list = []
    time = 0
    for i in range(1, n + 1):
        queue.enqueue(i)
    while not queue.isEmpty():
        p = passenger_queue.pop(0)
        if queue.getFront() == p:
            queue.dequeue()
            time += 1
            time_list.append(time)
        else:
            passenger_queue.append(p)
            time += 1
    average_wait_time = sum(time_list) / n
    return time, average_wait_time

if __name__ == '__main__':
    n = int(input())
    passenger_queue = list(map(int, input().split()))

    # 输出
    time, average_wait_time = calculate_waiting_time(n, passenger_queue)
    print(f"{time} {average_wait_time:.1f}")