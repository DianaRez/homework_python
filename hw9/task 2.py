import multiprocessing as mp
import csv
import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


with open('matrix_1.csv', mode='r') as f_1:
    reader_1 = csv.reader(f_1, delimiter=';')
    data_read_1 = [row for row in reader_1]
    height_1 = len(data_read_1)
    length_1 = len(data_read_1[0])
    a = [[] for t in range(height_1)]
    for i in range(height_1):
        a[i] = [int(x) for x in data_read_1[i]]
    with open('matrix_2.csv', mode='r') as f_2:
        reader_2 = csv.reader(f_2, delimiter=';')
        data_read_2 = [row for row in reader_2]
        height_2 = len(data_read_2)
        length_2 = len(data_read_2[0])
        b = [[] for t in range(height_2)]
        for i in range(height_2):
            b[i] = [int(a) for a in data_read_2[i]]

def work(nomer):
    list = [0 for t in range(length_2)]
    for k in range(length_2):
        for j in range(length_1):
            list[k] += a[nomer][j] * b[j][k]
    return list

@time_decorator
def multiple(number_of_proc):
    p = mp.Pool(number_of_proc)
    nomer = [i for i in range(height_1)]
    res = p.map(work, nomer)
    for i in res:
        print(' '.join(list(map(str, i))))


if __name__ == "__main__":
    multiple(1)




