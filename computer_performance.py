import multiprocessing
import time
start_time = time.time()

cpu = multiprocessing.cpu_count()

task = 100

def sum(a):
    s = 0
    for i in a:
        s += i
    return s

def add(x):
    xx = x
    while not(time.time() - start_time >= 60):
    # for _ in range(0, task ** 2):
        xx += 0.00001 # * (10 ** 5)
    return round(xx)

if __name__ == '__main__':
    print('\nCaculating...\n')

    core = [0 for _ in range(0, task)]

    pool = multiprocessing.Pool(processes=task)
    result = pool.map(add, core)

    score = sum(result)
    # score = round(1000000 / (time.time() - start_time))
    print("Single Core: {}".format(score // cpu))
    print("Multi Core: {}\n".format(score))