import threading
import time

def func(name):
	print('i am', name)
	time.sleep(1)
	print('this thread done...')

start_time = time.time()

for i in range(50):
	t = threading.Thread(target = func, args =(i,))
	t.setDaemon(True)
	t.start()

print('all thread has finished...', threading.current_thread(), threading.active_count())
print('total time', time.time()- start_time)