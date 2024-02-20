tarefas = []

while True:
    print('Opções:')
    print('1. Adicionar Tarefa')
    print('2. Mostrar tarefas')
    print('3. Sair')
    escolha = input('Escolha uma opção: ')

    if escolha == '1':
        tarefa = input('Digite a tarefa: ')
        tarefas.append(tarefa)
    elif escolha == '2':
        print('Tarefas: ')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i} - {tarefa}')
            print("-"*30)
    elif escolha == '3':
        break
    else:
        print('Opção inválida!')

