def caeserPassword(text: str, offset: int = 1) -> str:
    l = list(text)
    for i in range(len(text)):
        l[i] = chr(ord(text[i])+offset)
    msg = ''.join(l)
    return msg

def superimport(modulename: str, fullnane: str | None = None):
    import os
    try: module = __import__(modulename)
    except ModuleNotFoundError:
        os.system(f"pip install {modulename}" if not fullname else f"pip install {fullname}")
        os.system('cls' if os.name == 'nt' else 'clear')
        module = __import__(modulename)
    
    return module

def main() -> None:
    pass
if __name__ == "__main__":
    main()
