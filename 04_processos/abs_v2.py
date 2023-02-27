import multiprocessing
import time


def procesar():
    print('[', end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)


if __name__ == '__main__':
    ex = multiprocessing.Process(target=procesar)

    ex.start()
    ex.join()
