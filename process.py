from random import randint


class Process(object):
    __MIN_PID = 1000
    __MAX_PID = 9999
    __MIN_TTL = 1
    __MAX_TTL = 9
    __MIN_PRIORITY = 0
    __MAX_PRIORITY = 5
    __STATUS = {0:'Ready', 1:'Executing', 2:'Paused', 3:'Finished'}

    def __init__(self):
        self.__pid = self.__generate_process_infos(self.__MIN_PID, self.__MAX_PID)
        self.__priority = self.__generate_process_infos(self.__MIN_PRIORITY, self.__MAX_PRIORITY)
        self.__ttl = self.__generate_process_infos(self.__MIN_TTL, self.__MAX_TTL)
        self.__status = self.__STATUS.get(0)
        self.__time_finished = 0

    @property
    def time_finished(self):
        if self.__time_finished == 0:
            return 'Not finished'

        return self.__time_finished

    @property
    def pid(self):
        return self.__pid

    @property
    def ttl(self):
        return self.__ttl

    @property
    def priority(self):
        return self.__priority

    @property
    def status(self):
        return self.__status

    def __generate_process_infos(self, init, finish):
        return randint(init, finish)

    def make_process(self, pause, clock):
        self.__ttl = self.ttl - 1
        self.__change_status(pause, clock)

    def __change_status(self, pause, clock):
        if self.status == self.__STATUS.get(0) and self.__to_execute():
            self.__status = self.__STATUS.get(1)
            return

        elif self.status == self.__STATUS.get(0) and not self.__to_execute():
            self.__status = self.__STATUS.get(3)
            self.__time_finished = clock
            return

        elif self.status == self.__STATUS.get(1) and pause:
            self.__status = self.__STATUS.get(2)
            return

        elif self.status == self.__STATUS.get(1) and not pause and self.__to_execute():
            return

        elif self.status == self.__STATUS.get(1) and not pause and not self.__to_execute():
            self.__status = self.__STATUS.get(3)
            self.__time_finished = clock
            return

        elif self.status == self.__STATUS.get(2) and self.__to_execute():
            self.__status = self.__STATUS.get(1)
            return

        elif self.status == self.__STATUS.get(2) and not self.__to_execute():
            self.__status = self.__STATUS.get(3)
            self.__time_finished = clock
            return

    def __to_execute(self):
        if self.ttl > 0:
            return True

        return False

    def __str__(self):
        return f'PID: {self.pid} | Priority: {self.priority} | TTL: {self.ttl} | Status: {self.status} | Time clock finished: {self.time_finished}'
