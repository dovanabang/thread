import threading

def compute_square(number):
    print("Computing square of {}...".format(number))
    square = number * number
    print("Square of {} is: {}".format(number, square))

# Khởi tạo một luồng để tính toán bình phương của 2 số
thread = threading.Thread(target=compute_square, args=(5,))
thread.start()

# In ra thông báo cho người dùng trong khi đợi tính toán kết thúc
print("Please wait while we compute the square...")

# Chờ đợi cho luồng tính toán kết thúc
thread.join()

# In ra thông báo khi tính toán kết thúc
print("Square computation completed!")
