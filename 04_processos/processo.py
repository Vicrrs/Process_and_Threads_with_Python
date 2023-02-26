import multiprocessing

print(f"Iniciando o processo com nome: {multiprocessing.current_process().name}")

def faz_algo(valor):
    print(f"Fazendo algo com o {valor}")

def main():
    pc = multiprocessing.Process(target=faz_algo, args=('Passaro',), name ='Vetor')

    print(f"Iniciando o processo com o nome: {pc.name}")

    pc.start()
    pc.join()

if __name__ == '__main__':
    main()
