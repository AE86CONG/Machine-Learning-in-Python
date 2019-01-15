import threading
import time

def func(name):
	print('i am', name)
	time.sleep(3)
	print('this thread done...')


start_time = time.time()


res = []
for i in range(50):
	t = threading.Thread(target = func, args = (i,))
	t.start()
	res.append(t)

for j in res:
	j.join()


print('all thread has finished...', threading.current_thread())

print('totall time:', time.time() - start_time)