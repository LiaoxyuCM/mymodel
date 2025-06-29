class Frac:
    def __init__(self, denominator: int, molecule: int) -> None: 
        self.deno = denominator
        self.mole = molecule
    
    def __str__(self) -> str:
        return f"{self.mole}/{self.deno}"

def gcd(x: int, y: int) -> int:
    while y:
        x, y = y, x % y
    return x

def plus(a: Frac, b: int | Frac) -> Frac:
    if isinstance(b, int):
        b = Frac(1, b)

    if a.deno != b.deno:
        commonnedDeno: int = a.deno * b.deno
        commonnedMoleWithA = a.mole * b.deno
        commonnedMoleWithB = b.mole * a.deno
    else:
        commonnedDeno: int = a.deno
        commonnedMoleWithA = a.mole
        commonnedMoleWithB = b.mole

    commonnedMole: int = commonnedMoleWithA + commonnedMoleWithB
    return Frac(commonnedDeno // gcd(commonnedDeno, commonnedMole), commonnedMole // gcd(commonnedDeno, commonnedMole))

def minus(a: Frac, b: int | Frac) -> Frac:

    if isinstance(b, int):
        b = Frac(1, b)

    if a.deno != b.deno:
        commonnedDeno: int = a.deno * b.deno
        commonnedMoleWithA = a.mole * b.deno
        commonnedMoleWithB = b.mole * a.deno
    else:
        commonnedDeno: int = a.deno
        commonnedMoleWithA = a.mole
        commonnedMoleWithB = b.mole

    commonnedMole: int = commonnedMoleWithA - commonnedMoleWithB
    return Frac(commonnedDeno // gcd(commonnedDeno, commonnedMole), commonnedMole // gcd(commonnedDeno, commonnedMole))

def times(a: Frac, b: int | Frac) -> Frac:

    if isinstance(b, int):
        newB = Frac(1, b)
    else:
        newB = b
    
    if a.deno == newB.deno:
        mole = a.mole + newB.mole
        return Frac(a.deno // gcd(a.deno, mole), mole // gcd(a.deno, mole))
    else:
        deno = a.deno*newB.deno
        mole = a.mole*newB.mole
        return Frac(deno // gcd(deno, mole), mole // gcd(deno, mole))


def divide(a: Frac, b: int | Frac) -> Frac:

    if isinstance(b, int):
        newB = Frac(b, 1)
    else:
        newB = Frac(b.mole, b.deno)
    
    if a.deno == newB.deno:
        mole = a.mole + newB.mole
        return Frac(a.deno // gcd(a.deno, mole), mole // gcd(a.deno, mole))
    else:
        deno = a.deno*newB.deno
        mole = a.mole*newB.mole
        return Frac(deno // gcd(deno, mole), mole // gcd(deno, mole))


def main() -> None:
    a = Frac(5, 2)
    b = Frac(4, 10)

    print(a, b)
    print(f" {a.mole}     {b.mole}     {plus(a, b).mole} \n--- + ---- = ----\n {a.deno}      {b.deno}     {plus(a, b).deno} \n")
    print(f" {a.mole}     {b.mole}     {times(a, b).mole} \n--- * ---- = ---\n {a.deno}      {b.deno}     {times(a, b).deno} ")

if __name__ == "__main__":
    main()
