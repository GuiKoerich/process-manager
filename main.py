from process import Process
from time import sleep
from process_manager import ProcessManager


#Apresentação
print('' * 3)
print('Gerenciador de Processos - Arquitetura de Computadores')
print('Aluno: Guilherme Rosa Koerich - 4ª Fase')
print('Professor: Patryck Ramos Martins')
print('' * 3)

#Configurações para simulação
qnt_initial_process = int(input('Com quantos processos você deseja iniciar o gerenciador, (mínimo 1): '))

if qnt_initial_process < 0:
    qnt_initial_process *= -1

print()

while(qnt_initial_process == 0):
    print('O número de processos deve ser no mínimo 1')
    qnt_initial_process = int(input('Qual número de processos você deseja iniciar o gerenciador: '))
    print()

max_process = int(input('Qual a quantidade de processos máxima na lista, (mínimo 1): '))

if max_process < 0:
    max_process *= -1

print()

clock_simulation = int(input('Quantos segundos você deseja para que o clock seja simulado: '))

if clock_simulation < 0:
    clock_simulation *= -1


#Simulação
manager = ProcessManager()

for i in range(qnt_initial_process):
    process = Process()
    manager.add_process(process)

manager.show_list()

add_process = True

while(not manager.list_is_empty()):
    print()
    print('--------------------------------')
    print(f'Clock inicial: {manager.clock}')
    manager.execute_first_process()
    print(f'Clock final: {manager.clock}')
    print('--------------------------------')
    print()
    manager.show_list()
    print()
    manager.show_finished()
    print()

    if manager.final_simulation(max_process):
        add_process = False

    if add_process:
        process = Process()
        manager.add_process(process)

    sleep(clock_simulation)
