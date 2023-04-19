# import threading

# count = 0

# # Tạo một Lock object
# lock = threading.Lock()

# def increment():
#     global count
#     for _ in range(10):
#         # Đảm bảo rằng chỉ có một thread được phép truy cập vào biến count cùng một lúc
#         lock.acquire()
#         count += 1
        
#         lock.release()

# def decrement():
#     global count
#     for _ in range(10):
#         # Đảm bảo rằng chỉ có một thread được phép truy cập vào biến count cùng một lúc
#         lock.acquire()
#         count -= 1
#         print("decrement:", count)
#         lock.release()

# # Tạo các thread
# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=decrement)

# # Khởi chạy các thread
# t1.start()
# t2.start()

# # Chờ cho các thread kết thúc
# t1.join()
# t2.join()

# # In giá trị của biến count  print("increment:", count)
# print("Final value of count is:", count)

import threading

count = 0

# Tạo một Lock object
lock = threading.Lock()

def increment():
    global count
    for _ in range(10):
        # Đảm bảo rằng chỉ có một thread được phép truy cập vào biến count cùng một lúc
        lock.acquire()
        count += 1
        print("increment:", count)
        lock.release()

def decrement():
    global count
    for _ in range(10):
        # Đảm bảo rằng chỉ có một thread được phép truy cập vào biến count cùng một lúc
        lock.acquire()
        count -= 1
        print("decrement:", count)
        lock.release()

# Tạo các thread
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=decrement)

# Khởi chạy các thread
t1.start()
t2.start()

# Chờ cho các thread kết thúc
t1.join()
t2.join()

# In giá trị của biến count
print("Final value of count is:", count)
