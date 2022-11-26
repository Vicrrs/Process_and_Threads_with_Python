from threading import Thread
import threading
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10))

    th.start()  # adicionar a nossa thread na pool de threads prontas para execução

    print('\nPodemos fazer outras no programa  enquanto a thread vai executando...')
    print('Geek University\n' * 2)
    th.join()  # avisa pra ficar aguardando aq até a thread terminar a execução
    print('\nPronto')


def contar(oq, num):
    for n in range(1, num + 1):
        print(f'{n} {oq}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
