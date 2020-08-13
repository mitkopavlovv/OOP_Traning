from threading import Thread
import time


class Hello(Thread):
    def __init__(self, counter, timeSleep, name):
        Thread.__init__(self)
        self.counter = counter
        self.timeSleep = timeSleep
        self.name = name

    def run(self):
        for i in range(0, self.counter):
            print("{} Hello {}".format(i, self.name))
            time.sleep(self.timeSleep)


class Hi(Thread):
    def __init__(self, counter, timeSleep, name):
        Thread.__init__(self)
        self.counter = counter
        self.timeSleep = timeSleep
        self.name = name

    def run(self):
        for i in range(0, self.counter):
            print("{} Hi {}".format(i, self.name))
            time.sleep(self.timeSleep)


printHello = Hello(5, 1, "Th1")
printHi = Hi(5, 1, "Th2")

printHello.start()
# time.sleep(0.4)
printHi.start()

printHello.join()
printHi.join()

print("Hi there Main Thread")
