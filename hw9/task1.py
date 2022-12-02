import csv
import time


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


@time_decorator
def multiple(matrix_1, matrix_2):
    matrix = [[0]*len(matrix_2[0]) for t in range(len(matrix_1))]
    for i in range(len(matrix_1)):
        for k in range(len(matrix_2[0])):
            for j in range(len(matrix_1[0])):
                matrix[i][k] += matrix_1[i][j] * matrix_2[j][k]
    for i in matrix:
        print(' '.join(list(map(str, i))))
    return ""

with open('matrix_1.csv', mode='r') as f_1:
    reader_1 = csv.reader(f_1, delimiter=';')
    data_read_1 = [row for row in reader_1]
    height_1 = len(data_read_1)
    length_2 = len(data_read_1[0])
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

        multiple(a, b)


