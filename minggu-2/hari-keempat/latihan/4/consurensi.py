import os
import time
import threading
import multiprocessing

NUM_WORKERS =4

def only_sleep() :
    print("PID : {}, Process Name : {}, Thread Name : {}".format(os.getpid(), multiprocessing.current_process().name, threading.current_thread().name))
    time.sleep(1)

def crunch_numbers() :
    print("PID : {}, Process Name : {}, Thread Name : {}".format(os.getpid(), multiprocessing.current_process().name, threading.cuurrent_thread().name))
    x = 0
    while x < 10000000 :
        x += 1
for _ in range(NUM_WORKERS) :
    only_sleep()
end_time = time.time()
start_time = time.time()
print("Serial time = ", end_time, start_time)

# Run tasks using threads

processes = [multiprocessing.Process(target=only_sleep()) for _ in range(NUM_WORKERS)]
[process.start() for process in processes]
[process.join() for process in processes]
end_time = time.time()

print("Parallel time = ", end_time-start_time)