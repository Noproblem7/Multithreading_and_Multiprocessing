import time
from datetime import datetime
import threading


def read_file(file_path):
    time.sleep(2)
    with open(file_path, "r") as file:
        data = file.read()
        print(f"data read from {file_path}:{data}")


def main():
    file_path1 = 'data/file_1.txt'
    file_path2 = 'data/file_2.txt'

    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("Done")


if __name__ == '__main__':
    print(datetime.now())
    main()
    print(datetime.now())
