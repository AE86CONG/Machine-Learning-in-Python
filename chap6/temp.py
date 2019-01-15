import threading
import time

def func(name):
	print('hello', name)
	time.sleep(3)

t1 = threading.Thread(target = func, args = ('coca',))
t2 = threading.Thread(target = func, args = ('nawa',))

start_time = time.time()
print(start_time)
t1.start()
t1_time = time.time()
print(t1_time)
t2.start()
t2_time = time.time()
print(t2_time)