import multiprocessing

def calcular(dado):
    return dado ** 2

def main():
    tamanho_pool = multiprocessing.cpu_count() 

    print(f'Tamanho da pool é: {tamanho_pool}')

    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saidas: {saidas}')

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()
