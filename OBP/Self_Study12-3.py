import threading

class SumThread(threading.Thread):
    def __init__(self, start, end):
        threading.Thread.__init__(self)
        self.start_num = start
        self.end_num = end
        self.result = 0 

    def run(self):
        self.result = sum(range(self.start_num, self.end_num + 1))
        print(f"{self.start_num}부터 {self.end_num}까지의 합: {self.result}")

t1 = SumThread(1, 1000)
t2 = SumThread(1, 100000)
t3 = SumThread(1, 10000000)

t1.start()
t2.start()
t3.start()