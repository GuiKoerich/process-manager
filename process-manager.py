class ProcessManager(object):
    __list = []
    __index = -1

    def __init__(self):
        pass

    def add_process(self, process):
        if self.__list_is_empty():
            self.__list.append(process)
        else:
            self.__get_index_by_priority(process)

            self.__list.insert(self.__index, process) if (self.__index > - 1) else self.__list.append(process)

            self.__clear_index()

    def execute_first_process(self):
        if not self.__list_is_empty():
            first_process = self.__list.__getitem__(0)
            ttl = first_process.ttl
            first_process.make_process()

            print(f'PID: {first_process.pid} | TTL: {ttl} -> {first_process.ttl}')

            self.__remove_process_finished()

    def __remove_process_finished(self):
        for i in self.__list:
            if i.ttl == 0:
                self.__list.remove(i)

    def __clear_index(self):
        self.__index = -1

    def __list_is_empty(self):
        if len(self.__list) == 0:
            return True

        return False

    def __get_index_by_priority(self, process):
        for i in self.__list:
            if (i.priority > process.priority):
                self.__index = self.__list.index(i)
                break

    def show_list(self):
        if self.__list_is_empty():
            print('A lista de processos está vazia')
        else:
            for i in self.__list:
                print(i)

    def have_process(self):
        if not self.__list_is_empty():
            return True
        return False

