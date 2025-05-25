class SimpleCounter:
    def __init__(self) -> None:
        self.count = 0

    def increase(self) -> None:
        self.count += 1
    
    def clear(self) -> None:
        self.count = 0

    def __int__(self) -> int:
        return self.count
    
    def __str__(self) -> str:
        return f"{self.count}"

class AdvancedCounter(SimpleCounter):
    def __init__(self) -> None:
        super().__init__()
        self.__saved: dict[str, int] = {}
    
    def decrease(self) -> None:
        if self.count > 0:
            self.count -= 1
    
    def save(self, id: str) -> None:
        self.__saved[id] = self.count
    
    def applySaved(self, id: str) -> None:
        self.count = self.__saved[id]

    def read(self, id: str) -> int:
        return self.__saved[id]
    
    def readAll(self) -> dict[str, int]:
        return self.__saved
        
    def deleteSaved(self, id: str) -> None:
        self.__saved.pop(id)
    
    def deleteSavedAll(self) -> None:
        self.__saved = {}

class CounterControlUnit:
    def init(self, initCnt : SimpleCounter | AdvancedCounter | None = None) -> None:
        self.initCnt = initCnt

    def increase(self, counter: SimpleCounter | AdvancedCounter | None = None) -> SimpleCounter | AdvancedCounter:
        if not counter:
            if self.initCnt: counter = self.initCnt
            else: counter = SimpleCounter()
        counter.count += 1
        return counter

    def clear(self, counter: SimpleCounter | AdvancedCounter | None = None) -> SimpleCounter | AdvancedCounter:
        if not counter:
            if self.initCnt: counter = self.initCnt
            else: counter = SimpleCounter()
        counter.count = 0
        return counter

    def __str__(self) -> str:
        return f"CounterControlUnit() -> {self.initCnt}"

    __init__ = init # Quick define function if they are same


def main() -> None:
    pass

if __name__ == "__main__":
    main()
