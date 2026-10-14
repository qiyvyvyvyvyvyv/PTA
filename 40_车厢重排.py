"""
问题描述：
一列货运列车共有n节车厢,每节车厢将停放在不同的车站.假定n个车站的编号为1--n,
即货运列车按照第n站至第1站的次序经过这些车站。为了便于列车卸掉相应的车厢,车厢的编号应与车站的编号相同。
使各个车厢按1~n次序排列,这样每次卸掉最后一节车厢即可.所以给定任意次序的车厢,必须重排列它们.
可排列的地方是转轨站,转轨站由一个入轨站,一个出轨站,缓冲轨k个.列车由入轨站进站,经过缓冲轨,出轨.
开始时,n节车厢从入轨进入入轨站,转轨结束后按照1-n的次序出轨.假定缓冲轨具有先进先出的特性,且禁止将车厢从缓冲轨移址入轨,
将出轨移至缓冲轨.假设有k个缓冲轨,则可以用来暂存车厢的为k-1个,另一个直接出轨。重排车厢的规则包含如下三条：
一个车厢从入轨移至出轨或缓冲轨；
一个车厢只有在其编号恰是下一个待输出编号时，可移到出轨；
一个车厢移到某个缓冲轨，仅当其编号大于该缓冲轨中队尾车厢的编号，
若多个缓冲轨满足这一条件，则选择队尾车厢编号最大的，否则选择一个空缓冲轨，若无空缓冲轨则无法重排。
本题要求使用之前实现的链式队列类实现一个目标函数，该函数接收车厢入轨顺序数组in_track，
空队列out_track，出轨队列车厢数量n和缓冲轨数量k，将出轨的位序依次入队out_track，如果车厢重排问题无解，
输出"error: task is impossible"并返回空队列，否则返回out_track
对于n=9,k=3,in_track=[5,8,1,7,4,2,9,6,3],因为in_track[2]=1最先出轨，所以将2先入队out_track，
随后因为in_track[5]=2随后出轨，
所以5入队out_track，最后out_track=[2,5,8,4,0,7,3,1,6]
"""
class QueueNode:
    def __init__(self, data):
        self.data = data  # 存储数据
        self.next = None  # 链式队列中下一个元素的位置

class Queue:
    def __init__(self):
        self.size = 0  # 链式队列中当前元素个数
        self.front = None  # 链式队列的队首指针，初始化为None
        self.rear = None  # 链式队列的队尾指针，初始化为None

def InitQueue():
    queue = Queue()
    return queue

def IsEmpty(queue):
    return queue.size == 0

def DestroyQueue(queue):
    queue = None

def EnQueue(queue, x):
    new_node = QueueNode(x)
    if queue.rear is None:
        queue.front = new_node
    else:
        queue.rear.next = new_node
    queue.rear = new_node
    queue.size += 1

def GetFront(queue):
    if IsEmpty(queue):
        # print("Queue is empty")
        return None
    else:
        return queue.front.data

def DeQueue(queue):
    if IsEmpty(queue):
        # print("Queue is empty")
        pass
    else:
        temp = queue.front
        queue.front = queue.front.next
        if queue.front is None:
            queue.rear = None
        queue.size -= 1
        del temp

def GetRear(queue):
    if IsEmpty(queue):
        # print("queue is empty")
        return None
    else:
        return queue.rear.data

# 算法3-15：车厢重排 TrainCarriageScheduling(in_track, n, k)
def TrainCarriageScheduling(in_track, n, k):
    buffer_queue_list = [InitQueue() for _ in range(k)]
    buffer_data_list = [[] for _ in range(k)]
    j, z = 1, 0
    out_track = InitQueue()
    for i in range(n):
        if in_track[i] == j:
            EnQueue(out_track, i)
            j += 1
        else:
            if buffer_queue_list[z].rear is None:
                EnQueue(buffer_queue_list[z], in_track[i])
                buffer_data_list[z].append(i)
            elif buffer_queue_list[z].rear.data < in_track[i]:
                if z == k - 1:
                    last_data_list = []
                    for h in range(k):
                        if buffer_queue_list[h].rear.data < in_track[i]:
                            last_data_list.append(buffer_queue_list[h].rear.data)
                    if len(last_data_list) == k:
                        min_value = max(last_data_list)
                        idx = last_data_list.index(min_value)
                        EnQueue(buffer_queue_list[idx], in_track[i])
                        buffer_data_list[idx].append(i)
                    else:
                        EnQueue(buffer_queue_list[z], in_track[i])
                        buffer_data_list[z].append(i)
                else:
                    EnQueue(buffer_queue_list[z], in_track[i])
                    buffer_data_list[z].append(i)
            else:
                z += 1
                if z + 1 > k:
                    print("error: task is impossible")
                    return Queue()
                EnQueue(buffer_queue_list[z], in_track[i])
                buffer_data_list[z].append(i)
    z = j
    while out_track.size < n:
        for i in range(k):
            if buffer_queue_list[i].rear is not None and buffer_queue_list[i].front.data == j:
                EnQueue(out_track, buffer_data_list[i].pop(0))
                DeQueue(buffer_queue_list[i])
                j += 1
        if z == j:
            print("error: task is impossible")
            return Queue()
        z += 1
    return out_track

# 算法3-15 结束
def main():
    n, k = map(int, input().split())
    in_track = list(map(int, input().split()))
    out_track = TrainCarriageScheduling(in_track, n, k)
    for i in range(n):
        print(GetFront(out_track))
        DeQueue(out_track)
    DestroyQueue(out_track)

main()