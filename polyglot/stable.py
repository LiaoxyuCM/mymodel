# polyglot.py-stable-v1.1

import argparse, json

# Define arguments
parser = argparse.ArgumentParser(description='Here is polyglot creator and thank @SugarBreeze_微风 and @sally4953 so much.')
parser.add_argument('--PolyglotWith', '-pw', type=str, choices=['JSandPY', 'jap', 'jp', 'CPPandPY', 'cap', 'cp', 'pass'], default='pass', help="Set which two langs are polyglot with")
parser.add_argument('--JSandPY', '-jap', '-jp', action='store_true', help='[Button][NeverRecommendAgain] Polyglot with JavaScript and Python')
parser.add_argument('--CPPandPY', '-cap', '-cp', action='store_true', help='[Button][NeverRecommendAgain] Polyglot with C++ and Python')
parser.add_argument('--CPPorJSfile', '-cojf', '-jocf', '-jf', '-cf', type=str, required=True, help='C++ file or JavaScript file')
parser.add_argument('--PYfile', '-pf', type=str, required=True, help='Python file')
parser.add_argument('--CopyResult', '-cr', '-cl', '-c', action='store_true',  help='[Button] Copy result to your clipboard')
parser.add_argument('--HideResult', '-hr', '-H', action='store_true', help='[Button] Tell me about do not show result')
parser.add_argument('--OutFile', '-of', '-o', type=str, required=False, default='', help='Write result into file')
parser.add_argument('--SkipErrorCheckers', '-sec', '-s', action='store_true', help='[Button][NotRecommend] Skip every ErrorCheckers')
parser.add_argument('--Encoding', '-e', type=str, default='utf-8', help='Specify file encoding (default: utf-8)')
parser.add_argument('--PrintFormat', '-pformat', '-pfmt', type=str, choices=['plain', 'json'], default='plain', help='Specify print format (default: plain)')
parser.add_argument('--OutputFormat', '-oformat', '-ofmt', type=str, choices=['plain', 'json'], default='plain', help='Specify output format (default: plain)')

# Parse arguments
args = parser.parse_args()
rs = ''
jap = args.JSandPY
cap = args.CPPandPY
if args.PolyglotWith in ['JSandPY', 'jap', 'jp']:
    jap = True
    cap = False
if args.PolyglotWith in ['CPPandPY', '-cap', '-cp']:
    jap = False
    cap = True
oformat = args.OutputFormat
pformat = args.PrintFormat

# [ReadyToDelete] Useless module
if not args.SkipErrorCheckers:
    if jap == cap:
        print('[ErrorChecker #00/04] You must choose one of these two args (--JSandPY or --CPPandPY)' if jap is False else "[ErrorChecker #01/04] You can't choose two args (--JSandPY and --CPPandPY)")
        exit(1)

# Execute
with open(args.CPPorJSfile, mode='r', encoding=args.Encoding) as cojf:
    with open(args.PYfile, mode='r', encoding=args.Encoding) as pf:
        # Check errors
        if jap:
            if not args.SkipErrorCheckers:
                if ("'''" in cojf.read() or '"""' in cojf.read()):
                    print("[ErrorChecker #02/04] Cannot contain three double quotes or three single quotes in this JavaScript file. It is recommended to use string concatenation.")
                    exit(1)
                if "*/" in pf.read():
                    print("[ErrorChecker #03/04] Cannot contain '*/' in this Python file, it is recommended to use string concatenation.")
                    exit(1)

        # Add contents into result
        rs += ("1//1;'''\n" if jap else "#if 0\n1 // 1; '''\n#endif\n" if cap else '')
        rs += (cojf.read())
        rs += ("\n/*'''\n" if jap else "\n#if 0\n1 // 1; '''\n" if cap else '')
        rs += (pf.read())
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
        # Fix ModuleNotFoundError
        if not args.SkipErrorCheckers:
            if input("Module 'pyperclip' not found. To copy the result, this module is required. Install it? [Y/n]> ").lower() == "y":
                import os
                extcode = os.system("pip install pyperclip")
                print("Failed to install 'pyperclip', please check it." if extcode else "Successify to install 'pyperclip', please reenter this program.")
                exit(extcode)
            else:
                print("[ErrorChecker #04/04] Module \"pyperclip\" does not found")
                exit(1)
        else:
            raise ModuleNotFoundError("Module \"pyperclip\" does not found.\nPlease do not use the '--SkipErrorCheckers' argument unless necessary")

if args.OutFile:
    # Write to file
    with open(args.OutFile, 'a') as o:
        if oformat == "plain":
            o.write(f'\n{rs}')
        elif oformat == "json":
            o.write(json.dumps({"content": rs}))

