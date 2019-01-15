import threading
import time

class MyThread(threading.Thread):
	def __init__(self, name):
		super (MyThread, self).__init__()
		self.name = name

	def run(self):
		print('hello', self.name)
		time.sleep(3)

t1 = MyThread('alex')
t2 = MyThread('zing')

t1.start()
t2.start()

