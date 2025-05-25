def aiCn(q: str)-> str:
    return q.strip('吗？?').replace('你', '我')+'!'

def caeserPassword(text: str, offset: int = 1) -> str:
    l = list(text)
    for i in range(len(text)):
        l[i] = chr(ord(text[i])+offset)
    msg = ''.join(l)
    return msg

def superimport(modulename: str, fullnane: str | None = None):
    import os
    if fullnane == None:
        fullnane = modulename
    try: module = __import__(modulename)
    except ModuleNotFoundError:
        os.system(f"pip install {modulename}")
        os.system('cls' if os.name == 'nt' else 'clear')
        module = __import__(modulename)
    
    return module

def main() -> None:
    pass
if __name__ == "__main__":
    main()
