from random import randint


class Process(object):
    __MIN_PID = 1000
    __MAX_PID = 9999
    __MIN_TTL = 1
    __MAX_TTL = 10
    __MIN_PRIORITY = 0
    __MAX_PRIORITY = 5

    def __init__(self):
        self.__pid = self.__generate_process_infos(self.__MIN_PID, self.__MAX_PID)
        self.__priority = self.__generate_process_infos(self.__MIN_PRIORITY, self.__MAX_PRIORITY)
        self.__ttl = self.__generate_process_infos(self.__MIN_TTL, self.__MAX_TTL)

    @property
    def pid(self):
        return self.__pid

    @property
    def ttl(self):
        return self.__ttl

    @property
    def priority(self):
        return self.__priority

    def __generate_process_infos(self, init, finish):
        return randint(init, finish)

    def make_process(self):
        self.__ttl = self.ttl - 1

    def __str__(self):
        return f'PID: {self.pid} | Priority: {self.priority} | TTL: {self.ttl}'
