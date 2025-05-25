class Mark: #分数
    def __init__(self, denominator: int, molecule: int) -> None: # ?分子和分母不可以是小数，所以参数类型只给int, 没给float. 但是参数先传分母，再传分子
        self.deno = denominator
        self.mole = molecule
    
    def __str__(self) -> str:
        return f"{self.mole}/{self.deno}"

def gcd(x: int, y: int) -> int: # 获取最大公因数的函数
    while y:
        x, y = y, x % y
    return x

def add(a: Mark, b: int | Mark) -> Mark: # 模拟分数的相加操作

    if isinstance(b, int):
        # 将整数转换为分数
        # ! 不支持小数转分数, 参数b也只让传分数或整数，因为做小数转分数太难
        b = Mark(1, b)

    # 判断分数是不是同分子
    if a.deno != b.deno: # 如果不是
        # 模拟分数通分
        commonnedDeno: int = a.deno * b.deno
        commonnedMoleWithA = a.mole * b.deno
        commonnedMoleWithB = b.mole * a.deno
    else:# 否则
        commonnedDeno: int = a.deno
        commonnedMoleWithA = a.mole
        commonnedMoleWithB = b.mole

    commonnedMole: int = commonnedMoleWithA + commonnedMoleWithB
    # 返回结果且约分
    return Mark(commonnedDeno // gcd(commonnedDeno, commonnedMole), commonnedMole // gcd(commonnedDeno, commonnedMole))

def minus(a: Mark, b: int | Mark) -> Mark: # 模拟分数的相减操作

    if isinstance(b, int):
        # 将整数转换为分数
        # ! 不支持小数转分数, 参数b也只让传分数或整数，因为做小数转分数太难
        b = Mark(1, b)

    # 判断分数是不是异分子
    if a.deno != b.deno: # 如果是
        # 模拟分数通分
        commonnedDeno: int = a.deno * b.deno
        commonnedMoleWithA = a.mole * b.deno
        commonnedMoleWithB = b.mole * a.deno
    else:# 否则
        commonnedDeno: int = a.deno
        commonnedMoleWithA = a.mole
        commonnedMoleWithB = b.mole

    commonnedMole: int = commonnedMoleWithA - commonnedMoleWithB
    # 返回结果且约分
    return Mark(commonnedDeno // gcd(commonnedDeno, commonnedMole), commonnedMole // gcd(commonnedDeno, commonnedMole))

def times(a: Mark, b: int | Mark) -> Mark: # 模拟分数的相乘操作

    if isinstance(b, int):
        # 将整数转换为分数
        # ! 不支持小数转分数, 参数b也只让传分数或整数，因为做小数转分数太难
        newB = Mark(1, b)
    else:
        newB = b
    
    # 返回结果且约分
    if a.deno == newB.deno:
        mole = a.mole + newB.mole
        return Mark(a.deno // gcd(a.deno, mole), mole // gcd(a.deno, mole))
    else:
        deno = a.deno*newB.deno
        mole = a.mole*newB.mole
        return Mark(deno // gcd(deno, mole), mole // gcd(deno, mole))


def divide(a: Mark, b: int | Mark) -> Mark: # 模拟分数的相除操作

    if isinstance(b, int):
        #将整数转换为分数，再转化为倒数
        # ! 不支持小数转分数, 参数b也只让传分数或整数，因为做小数转分数太难
        newB = Mark(b, 1)
    else:
        newB = Mark(b.mole, b.deno)
    
    # 返回结果且约分
    if a.deno == newB.deno:
        mole = a.mole + newB.mole
        return Mark(a.deno // gcd(a.deno, mole), mole // gcd(a.deno, mole))
    else:
        deno = a.deno*newB.deno
        mole = a.mole*newB.mole
        return Mark(deno // gcd(deno, mole), mole // gcd(deno, mole))


def main() -> None:
    a = Mark(5, 2)
    b = Mark(4, 10)

    #做一次分数运算！
    print(a, b)
    print(f" {a.mole}     {b.mole}     {add(a, b).mole} \n--- + ---- = ----\n {a.deno}      {b.deno}     {add(a, b).deno} \n")
    print(f" {a.mole}     {b.mole}     {times(a, b).mole} \n--- * ---- = ---\n {a.deno}      {b.deno}     {times(a, b).deno} ")

if __name__ == "__main__":
    main()
