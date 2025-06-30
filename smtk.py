'''
Smtk is a good way to edit multi-line text with single-line text.

Try this CLI!
If you are new, please run these command (to get help):
1.  python smtk.py -u
2.  python smtk.py -h
Then you can:
    python smtk.py
'''

def execute(arg: str, return_status: bool = False):
    from typing import Literal
    preprint: list = []
    status: Literal[0, 1, 2] = 0
    result: str = ""
    for i in arg:
        if i == '\\':
            if status:
                if status != 2:
                    preprint.append('\\')
                status = 0
            else:
                status = 1
                continue
        elif i == '.':
            if status:
                if status != 2:
                    preprint.append('.')
                status = 0
            else:
                result += ''.join(preprint)+"\n"
                preprint = []
        elif status: status = 2
        else: preprint.append(i)
    return (result, status) if return_status else result 

def fill_with_color(arg: str):
    from typing import Literal
    status: Literal[0, 1, 2] = 0
    result: str = ""
    j = 0
    for i in arg:
        if i == "\\":
            if status == 2:
                result += "\x1b[90m\\\x1b[0m"
                status = 0
            elif status:
                result += "\\\x1b[0m"
                status = 0
            else:
                result += "\x1b[93m\\" if arg[j+1] == "." or arg[j+1] == "\\" else "\x1b[90m\\"
                status = 1
            j += 1
            continue
        elif i == ".":
            if status == 2:
                result += "\x1b[90m.\x1b[0m"
                status = 0
            elif status:
                result += ".\x1b[0m"
                status = 0
            else:
                result += "\x1b[94m.\x1b[0m"
            j += 1
            continue
        elif status:
            result += "\x1b[90m"
            status = 2
        j += 1
        result += i
    result += "\x1b[0m"
    return result


def main():
    from argparse import ArgumentParser
    from datetime import datetime
    try:
        from additional_modules import smtkx
    except:
        print("File ./additional_modules/smtkx.py not found. You may can't get the usage.")

    psr = ArgumentParser()
    psr.add_argument("-u", "--usage", action="store_true", help="Show usage.")
    psr.add_argument("-if", "--input_file", metavar="FileName", type=str, required=False, help="Input with a file.") # type: ignore
    psr.add_argument("-H", "--hint", action="count", help="Enable hint. Use -HH or two \"--hint\"s to get more detailed.")
    psr.add_argument("-c", "--colorful", action="store_true", help="Switch to the colorful mode")

    ags = psr.parse_args()

    if ags.usage:
        try:
            print(smtkx.usage)
            quit()
        except:
            print("File ./additional_modules/smtkx.py not found. You can't get the usage.\nYou can visit this repo to get it.")

    if ags.colorful:
        try:
            smtkx.colorful_that_under_win10()
        except Exception:
            import sys
            if sys.platform == "win32":
                if sys.getwindowsversion().major < 10:
                    print("File ./additional_modules/smtkx.py not found. You may get messy codes and not a colorful text")

    if ags.input_file:
        with open(ags.input_file, "r") as f:
            rs = execute(f.read())
            print(f"\x1b[92m{rs}\x1b[0m" if ags.colorful else rs, end="")
    else:
        if ags.hint:
            print(f"Smtk {datetime.now().strftime("on \x1b[92m%Y-%m-%d\x1b[0m at \x1b[92m%H:%M:%S\x1b[0m")}" \
                if ags.colorful else f"Smtk {datetime.now().strftime("on %Y-%m-%d at %H:%M:%S")}")
        while True:
            try:
                ip = input("\x1b[94m>>> \x1b[0m" if ags.colorful and ags.hint else '>>> ' if ags.hint else "")
                rs, stat = execute(ip, return_status=True)
                if stat:
                    raise SyntaxError("Invalid syntax because \"\\\" does not closed.")
                if ags.hint == 2:
                    print(f"==> {fill_with_color(ip)}" if ags.colorful else f"==> {ip}")
                if ags.hint == 2:
                    print("-----Out-----")
                print(f"\x1b[92m{rs}\x1b[0m" if ags.colorful else rs, end="")
                if ags.hint == 2:
                    print("-"*13)
            except KeyboardInterrupt:
                print("\n\x1b[93mQuitting...\x1b[0m" if ags.colorful else "\nQuitting...")
                quit(0)
            except Exception as e:
                print(f"\x1b[1m\x1b[91m{type(e).__name__}\x1b[0m \x1b[91m{e}\x1b[0m" if ags.colorful else f"{type(e).__name__}: {e}")

if __name__ == "__main__":
    main()
