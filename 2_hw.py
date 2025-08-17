def task_1() -> str:
    a: int = 7
    b: float = 3.14
    c: str = 'prophecy'
    d: list = [1, 2, 5, 10, 18]
    e: bool = True
    return print(type(a), ', ', type(b), ', ', type(c), ', ', type(d), ', ', type(e))

task_1()

def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return print(a[0:3], '- это список')

task_2()

def task_3(num: int) -> int:
    return num**2

print(task_3(10))