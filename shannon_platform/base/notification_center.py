from typing import Callable, Dict, List, Any
from shannon_platform.base.singleton import Singleton


class NotificationCenter(metaclass=Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.__observers: Dict[str, List[Callable]] = {}

    def add_observer(self, name: str, callback: Callable) -> None:
        if name in self.__observers.keys():
            self.__observers[name].append(callback)
        else:
            self.__observers[name] = [callback]

    def remove_observer(self, callback: Callable) -> None:
        for name in self.__observers.keys():
            self.__observers[name].remove(callback)

    def post(self, name: str, user_info: Dict[str, Any]) -> None:
        for callback in self.__observers[name]:
            callable(user_info)