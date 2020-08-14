from threading import Thread
import time
class Th1(Thread):
    def __init__(self, var, item):
        Thread.__init__(self)
        self.var = var
        self.item = item
    def print_data(self):
        print ("{}   {}".format(self.var, self.item))
    def run(self):
        for i in range(0, 5):
            print("{}, TH1".format(i))
            time.sleep(1)
        self.print_data()

class Th2(Thread):
    def __init__(self, var):
        Thread.__init__(self)
        print (var)
    def run(self):
        for i in range(0, 5):
            print("{}, TH2".format(i))
            time.sleep(1)

thread1 = Th1("Hi there", "Ivan")
thread3 = Th1("Hi there", "Simo")
thread2 = Th2("Hello there")

thread1.start()
time.sleep(0.5)
thread2.start()
time.sleep(0.5)
thread3.start()

thread1.join()
thread2.join()

print("Main thread here!")
