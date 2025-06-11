# polyglot.py-beta-v1.6

import json, enum

if __name__ == "__main__":
    import argparse
    
    # Define arguments
    parser = argparse.ArgumentParser(description='Here is polyglot creator and thank @SugarBreeze_Weifeng and @sally4953 so much.')
    polyglotwith = parser.add_mutually_exclusive_group(required=True)
    polyglotwith.add_argument('--JSandPY', '-jap', '-jp', action='store_true', help='[Button] Polyglot with JavaScript and Python')
    polyglotwith.add_argument('--CPPandPY', '-cap', '-cp', action='store_true', help='[Button] Polyglot with C++ and Python')
    parser.add_argument('--CPPorJSfile', '-cojf', '-jocf', '-jf', '-cf', type=str, required=True, help='C++ file or JavaScript file')
    parser.add_argument('--PYfile', '-pf', type=str, required=True, help='Python file')
    parser.add_argument('--CopyResult', '-cr', '-cl', '-c', action='store_true',  help='[Button] Copy result to your clipboard')
    parser.add_argument('--HideResult', '-hr', '-H', action='store_true', help='[Button] Tell me about do not show result')
    parser.add_argument('--OutFile', '-of', '-o', type=str, required=False, default='', help='Write result into file')
    parser.add_argument('--Encoding', '-e', type=str, default='utf-8', help='Specify file encoding (default: utf-8)')
    parser.add_argument('--PrintFormat', '-pformat', '-pfmt', '-pF', type=str, choices=['plain', 'json'], default='plain', help='Specify print format (default: plain)')
    parser.add_argument('--OutputFormat', '-oformat', '-ofmt', '-oF', type=str, choices=['plain', 'json'], default='plain', help='Specify output format (default: plain)')

    # Parse arguments
    args = parser.parse_args()
    rs = ''
    jap = args.JSandPY
    cap = args.CPPandPY
    oformat = args.OutputFormat
    pformat = args.PrintFormat

    with open(args.CPPorJSfile, encoding=args.Encoding) as cojf:
        with open(args.PYfile, encoding=args.Encoding) as pf:
            cojfcontent = cojf.read()
            pfcontent = pf.read()
            # Check errors
            if jap:
                if ("'''" in cojfcontent or '"""' in cojfcontent):
                    raise Exception("Cannot contain three double quotes or three single quotes in this JavaScript program. It is recommended to use string concatenation.")
                if "*/" in pfcontent:
                    raise Exception("Cannot contain '*/' in this Python program, it is recommended to use string concatenation.")
            
            # Add contents into result
            rs += ("1//1;'''\n" if jap else "#if 0\n1 // 1; '''\n#endif\n" if cap else '')
            rs += cojfcontent
            rs += ("\n/*'''\n" if jap else "\n#if 0\n1 // 1; '''\n" if cap else '')
            rs += pfcontent
            rs += ("\n# */\n" if jap else "\n#endif\n" if cap else '')

    if not(args.HideResult):
        # Print result
        if pformat == "plain":
            print(rs)
        elif pformat == "json":
            print(json.dumps({"content": rs}))
    if args.CopyResult:
        # Copy result
        try:
            import pyperclip
            pyperclip.copy(rs)
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
        # Write to file
        with open(args.OutFile, 'a') as o:
            if oformat == "plain":
                o.write(f'\n{rs}')
            elif oformat == "json":
                o.write(json.dumps({"content": rs}))

class PolyglotWith(enum.Enum):
    JSandPY = 0
    CPPandPY = 1

class Format(enum.Enum):
    plain = 0
    json = 1

def compile(polyglotwith: PolyglotWith, JSorCPPcode: str, PYcode: str, CopyResult: bool = False, ReturnFormat: Format = Format.plain):
    rs = ''
    cojfcontent = JSorCPPcode
    pfcontent = PYcode
    # Check errors
    if polyglotwith == PolyglotWith.JSandPY:
        if ("'''" in cojfcontent or '"""' in cojfcontent):
            raise Exception("Cannot contain three double quotes or three single quotes in this JavaScript program. It is recommended to use string concatenation.")
        if "*/" in pfcontent:
            raise Exception("Cannot contain '*/' in this Python program, it is recommended to use string concatenation.")
    
    # Add contents into result
    rs += ("1//1;'''\n" if polyglotwith == PolyglotWith.JSandPY else "#if 0\n1 // 1; '''\n#endif\n" if polyglotwith == PolyglotWith.CPPandPY else '')
    rs += cojfcontent
    rs += ("\n/*'''\n" if polyglotwith == PolyglotWith.JSandPY else "\n#if 0\n1 // 1; '''\n" if polyglotwith == PolyglotWith.CPPandPY else '')
    rs += pfcontent
    rs += ("\n# */\n" if polyglotwith == PolyglotWith.JSandPY else "\n#endif\n" if polyglotwith == PolyglotWith.CPPandPY else '')

    if CopyResult:
        # Copy result
        try:
            import pyperclip
            pyperclip.copy(rs)
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
    return rs if ReturnFormat == Format.plain else json.dumps({"content": rs}) if ReturnFormat == Format.json else ""

