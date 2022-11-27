import multiprocessing


def calcular(dado):
    return dado ** 2


def imprimir_nome_processo():
    print(
        f'Iniciando o processo com o nome: {multiprocessing.current_process().name}')


def main():
    tamanho_pool = multiprocessing.cpu_count()

    print(f'Tamanho da pool é: {tamanho_pool}')

    pool = multiprocessing.Pool(
        processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saidas: {saidas}')

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
