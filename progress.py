from typing import TypedDict
from math import floor

class ValidIndexOfPatternOfProgressBar(TypedDict):
    count: int
    left_char: str
    right_char: str
    empty_char: str
    full_char: str
    cursor: str

def ProgressBar(progress: float, pattern: ValidIndexOfPatternOfProgressBar = {
    "count": 20,
    "left_char": "[",
    "right_char": "]",
    "empty_char": " ",
    "full_char": "=",
    "cursor": ">",
}) -> str:
    assert 0 <= progress <= 100, "Invalid assert. Valid assert: 0 <= progress <= 100"
    j = floor(progress / 100 * pattern["count"])
    return f"{pattern["left_char"]}{pattern["full_char"]*j}{pattern["cursor"]if j<pattern['count']else""}{pattern['empty_char']*(pattern['count']-j-1)}{pattern['right_char']}"

def main() -> None:
    import time, random
    for i in range(0, 101):
        print(f"""{ProgressBar(progress=i, pattern={
            "count": i,
            "cursor": ":",
            "empty_char": "-",
            "full_char": "#",
            "left_char": "<",
            "right_char": ">"
        })} {i}%       """, end="\r")
        time.sleep(random.uniform(.01, .5))
    print()
    for i in range(0, 101):
        print(f"""{ProgressBar(i, pattern={
            "count": i,
            "cursor": ":",
            "empty_char": "-",
            "full_char": "#",
            "left_char": "<",
            "right_char": ">"
        })} {i}%       """, end="\n")

if __name__ == "__main__":
    main()