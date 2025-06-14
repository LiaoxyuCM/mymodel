from random import randint

def _xor(a: bool | int | str, b: bool | int | str):
    """
    truth table about _xor

    |input|input|output|
    |-----|-----|------|
    |False|False|False |
    |True |True |False |
    |False|True |True  |
    |True |False|True  |
    """
    return not (a is b)

class Plain:
    def __init__(self, plaindec: int = randint(0, 255)):
        if plaindec <= 255:
            k = format(plaindec, 'b')
            k = '0' * (8 - len(k)) + k
            self.p = k

    def randomPlain(self):
        k = format(randint(0, 255), 'b')
        k = '0' * (8 - len(k)) + k
        self.p = k

class Key:
    def __init__(self, keydec: int = randint(0, 255)):
        if keydec <= 255:
            k = format(keydec, 'b')
            k = '0' * (8 - len(k)) + k
            self.key = k

    def randomKey(self):
        k = format(randint(0, 255), 'b')
        k = '0' * (8 - len(k)) + k
        self.key = k

def XOR(plain: Plain, key: Key) -> int:
    enc: str = ''
    for i in range(len(plain.p)):
        a = int(plain.p[i])
        b = int(key.key[i])
        if _xor(a, b):
            enc += '1'
        else:
            enc += '0'
    return int(enc, 2)

def fill(a: str, b: str, fill_spec: str = '\0') -> tuple[str, str]:
    """
    Fill the shorter string with zeros to match the length of the longer string.
    """
    if len(a) < len(b):
        return a + fill_spec * (len(b) - len(a)), b
    elif len(b) < len(a):
        return a, b + fill_spec * (len(a) - len(b))
    return a, b

def main():
    # Command-line mode
    import argparse
    parser = argparse.ArgumentParser(description='XOR Password Encryption/Decryption Tool')
    parser.add_argument('--Plain', '-p', type=str, required=True, help='Plaintext to encrypt/decrypt')
    parser.add_argument('--Key', '-k', type=str, required=True, help='Key for encryption/decryption')
    parser.add_argument('--CopyResult', '-cr', '-cl', '-c', action='store_true',  help='[Button] Copy result to your clipboard')
    parser.add_argument('--HideResult', '-hr', '-H', action='store_true', help='[Button] Tell me about do not show result')
    parser.add_argument('--OutFile', '-of', '-o', type=str, required=False, default='', help='Write result into file')
    parser.add_argument('--Encoding', '-E', type=str, default='utf-8', help='Specify file encoding (default: utf-8)')
    parser.add_argument('--PrintFormat', '-pformat', '-pfmt', '-pF', type=str, choices=['plain', 'json'], default='plain', help='Specify print format (default: plain)')
    parser.add_argument('--OutputFormat', '-oformat', '-ofmt', '-oF', type=str, choices=['plain', 'json'], default='plain', help='Specify output format (default: plain)')

    args = parser.parse_args()

    plain = args.Plain
    key = args.Key
    plain, key = fill(plain, key)
    encrypted = ''
    for i in range(len(plain)):
        pl = Plain(ord(plain[i]))
        k = Key(ord(key[i]))
        encrypted += chr(XOR(pl, k))
    if not args.HideResult:
        if args.PrintFormat == "plain":
            print(encrypted)
        elif args.PrintFormat == "json":
            import json
            print(json.dumps({"result": encrypted}))
    if args.CopyResult:
        try:
            import pyperclip
            pyperclip.copy(encrypted)
        except ModuleNotFoundError:
            import os
            # Fix ModuleNotFoundError
            if input("Module 'pyperclip' not found. To copy the result, this module is required. Install it? [Y/n]> ").lower() == "y":
                print("[Log] Checking... [0/1]")
                if os.system("pip -V"):
                    raise Exception("Likes pip is not installed or installer didn't add pip to your path. Please fix it.")
                else:
                    print("All checks are passed. [1/1]")
                    if not os.system("pip install pyperclip"):
                        print("OK, the module is installed. Please reenter this program to continue")
                        exit(0)
            else:
                raise ModuleNotFoundError("Module \"pyperclip\" not found")
    if args.OutFile:
        with open(args.OutFile, 'w', encoding=args.Encoding) as f:
            if args.OutputFormat == "plain":
                f.write(encrypted)
            elif args.OutputFormat == "json":
                import json
                f.write(json.dumps({"result": encrypted}))

# Not-command-line mode
def compile(plain: str, key: str) -> str:
    """
    Compile the XOR encryption/decryption.
    """
    plain, key = fill(plain, key)
    encrypted = ''
    for i in range(len(plain)):
        pl = Plain(ord(plain[i]))
        k = Key(ord(key[i]))
        encrypted += chr(XOR(pl, k))
    return encrypted

if __name__ == '__main__':
    main()