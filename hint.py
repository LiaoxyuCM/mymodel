alert = lambda imporantMessage: input(f'{imporantMessage} [ENTER]')
confirm = lambda imporantMessage: input(f'{imporantMessage} [Y/n] (n)').lower() == 'y'
prompt = lambda imporantMessage, defaultText = "": q if (q := input(f'{imporantMessage} > ')) else defaultText

def main() -> None:
    alert('alert message')
    print(confirm('confirm message'))
    print(prompt('prompt message', 'default text'))

if __name__ == "__main__":
    main()