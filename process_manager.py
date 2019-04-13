class ProcessManager(object):
    __list = []
    __index = -1
    __STATUS = {0: 'Ready', 1: 'Executing', 2: 'Paused', 3: 'Finished'}
    __finished = []
    __clock = 0

    def __init__(self):
        pass

    @property
    def clock(self):
        return self.__clock

    def __increase_clock(self):
        self.__clock += 1


    def add_process(self, process):
        if self.list_is_empty():
            self.__list.append(process)
        else:
            self.__get_index_by_priority(process)

            self.__list.insert(self.__index, process) if (self.__index > - 1) else self.__list.append(process)

            self.__clear_index()

    def execute_first_process(self):
        self.__increase_clock()
        if not self.list_is_empty():
            first_process = self.__list.__getitem__(0)
            ttl = first_process.ttl
            first_process.make_process(self.__is_pause_process(), self.clock)

            print()
            print('Processando...')
            print(f'PID: {first_process.pid} | TTL: {ttl} -> {first_process.ttl} | Status: {first_process.status}')
            print()


            self.__change_process_to_begin()

            self.__remove_process_finished()

        else:
            print('Todos os processos foram executados, programa finalizado!')
            exit(0)

    def __remove_process_finished(self):
        for i in self.__list:
            if i.ttl == 0:
                self.__list.remove(i)
                self.__finished.append(i)

    def __clear_index(self):
        self.__index = -1

    def list_is_empty(self):
        if len(self.__list) == 0:
            return True

        return False

    def __get_index_by_priority(self, process):
        for i in self.__list:
            if i.priority > process.priority and self.__process_is_stand_by(i):
                self.__index = self.__list.index(i)
                break

    def __process_is_stand_by(self, process):
        if process.status == self.__STATUS.get(0) or process.status == self.__STATUS.get(2):
            return True

        return False

    def __is_pause_process(self):
        if self.have_process():
            first_process = self.__list.__getitem__(0)
            next_process = self.__list.__getitem__(1)

            if first_process.priority > next_process.priority:
                return True
            else:
                return False

        return False

    def __change_process_to_begin(self):
        if self.__is_pause_process():
            next_process = self.__list.__getitem__(1)
            self.__list.remove(next_process)
            self.add_process(next_process)

    def show_list(self):
        if self.list_is_empty():
            print('A lista de processos está vazia')
        else:
            print('=== INÍCIO FILA EXECUÇÃO ===')
            for i in self.__list:
                print(i)
            print('=== FIM FILA EXECUÇÃO ===')

    def have_process(self):
        if not self.list_is_empty() and len(self.__list) > 1:
            return True
        return False

    def final_simulation(self, value):
        if len(self.__list) >= value :
            return True

        return False

    def show_finished(self):
        if self.__finished.__len__() == 0:
            print('A lista de processos finalizados está vazia!')
        else:
            print('=== INÍCIO FILA DE PROCESSOS FINALIZADOS ===')
            for process in self.__finished:
                print(process)
            print('=== FINAL FILA PROCESSOS FINALIZADOS ===')