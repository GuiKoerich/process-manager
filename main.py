from process import Process
from time import sleep
from process_manager import ProcessManager


manager = ProcessManager()

for i in range(3):
    process = Process()
    manager.add_process(process)

manager.show_list()

stop = False

while(not manager.list_is_empty()):
    print()
    print('--------------------------------')
    manager.execute_first_process()
    print('--------------------------------')
    print()
    manager.show_list()
    print()


    if not stop:
        process = Process()
        manager.add_process(process)
        if manager.final_simulation(20):
            stop = True

    sleep(2)