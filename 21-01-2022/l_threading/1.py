import threading
import time



# # Section 1 - Threading ----------------------------------------------------- 

# class Test1(threading.Thread):
#     def run(self):
#         for i in range(100):
#             print(i)
#             time.sleep(1)

# class Test2(threading.Thread):
#     def run(self):
#         for i in range(100):
#             print(i)
#             time.sleep(1)

# t1 = Test1()
# t2 = Test2()

# t1.start()
# t2.start()
# t1.join()
# t2.join()


# # Section 2 - Threading -----------------------------------------------------

def func1():
    for i in range(100):
        print(i)
        time.sleep(1)

def func2():
    for i in range(100):
        print(i)
        time.sleep(1)

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()