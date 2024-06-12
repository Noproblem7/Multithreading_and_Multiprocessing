import multiprocessing
import time
from datetime import datetime


def write_file(file_path: str, data: str):
    time.sleep(2)
    with open(file_path, 'r+') as file:
        file.write(data)
        print(f'File written successfully. {file_path}\n')


def main():
    file_path1 = "file_1.txt"
    file_path2 = "file_2.txt"
    data1 = "running Process 1"
    data2 = "running Process 2"

    process1 = multiprocessing.Process(target=write_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_file, args=(file_path2, data2))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print(f'Process 1 finished')
    print(f'Process 2 finished')


if __name__ == '__main__':
    print(datetime.now())
    main()
    print(datetime.now())
