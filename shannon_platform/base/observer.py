from typing import Callable, List

class Observer(object):
    def __init__(self) -> None:
        super().__init__()

        self.callbacks: List[Callable] = []

    def subscribe(self, callback: Callable) -> None:
        self.callbacks.append(callback)

    def fire(self) -> None:
        for fn in self.callbacks:
            fn()