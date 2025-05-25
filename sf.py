from enum import Enum
from time import sleep, time

class UserType(Enum):
    DEFAULT = 0
    VIP = 1
    SVIP = 2

def getStringsLength(string: str, user: UserType = UserType.DEFAULT, debug: bool = False) -> int | tuple:
    startTime = 0
    if debug: startTime = time()
    
    if   user == UserType.SVIP:
        return len(string) if not debug else (len(string), time() - startTime)
    elif user == UserType.VIP :
        sleep(1)
        return len(string) if not debug else (len(string), time() - startTime)
    elif user == UserType.DEFAULT:
        sleep(5)
        rs = 0
        for _ in range(len(string)):
            rs += 1
        return rs if not debug else (rs, time() - startTime)
    else: return 0

def main() -> None:
    print(getStringsLength("Hello, world!", UserType.DEFAULT, True))
    print(getStringsLength("Hello, world!", UserType.VIP, True))
    print(getStringsLength("Hello, world!", UserType.SVIP, True))

if __name__ == "__main__":
    main()