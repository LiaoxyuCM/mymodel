from typing import TypedDict, NotRequired, Literal, Any
from datetime import datetime

class MetadataInfo(TypedDict):
    name: str
    company: NotRequired[str]
    partner: NotRequired[list[str]]
    author: NotRequired[str]
    creator: NotRequired[str]
    writer: NotRequired[str]
    encoder: NotRequired[str]
    downloadFrom: NotRequired[str]
    uploadTo: NotRequired[str | list[str]]
    receiveFrom: NotRequired[str]
    sendTo: NotRequired[str | list[str]]
    CC: NotRequired[str | list[str]]
    BCC: NotRequired[str | list[str]]
    version: NotRequired[str | int | float]
    url: NotRequired[str]
    tel: NotRequired[str | int]
    ID: NotRequired[str | int]
    finished: NotRequired[bool]
    finishDate: NotRequired[datetime]
    grade: NotRequired[Literal[1] | Literal[2] | Literal[3] | Literal[4] | Literal[5]]
    note: NotRequired[str]
    Copyright: NotRequired[str]
    tag: NotRequired[str]
    title: NotRequired[str]
    language: NotRequired[str] # English, Chinese, ...
    programmingLanguage: NotRequired[str] # Python, JavaScript, ...
    important: NotRequired[bool]
    dateOfLastModification: NotRequired[datetime]
    dateOfCreation: NotRequired[datetime]
    others: NotRequired[dict[str, Any]]


class File:
    def __init__(self, metadata: MetadataInfo = {"name": "test.txt"}, body: str = "") -> None:
        self.meta = metadata
        self.body = body

class Dir:
    def __init__(self, files: list[File]) -> None:
        self.files = files

def main() -> None:
    test1 = File(
        {"name": "test1.txt", "author": "Xiaoming", "ID": 1}, 
        "Hello!"
    )
    test2 = File(
        {"name": "test2.txt", "author": "Xiaoming", "ID": 2}, 
        "I'm Xiaoming!"
    )
    d = [test1, test2]
    dir = Dir(d)
    print(dir.files)
    


if __name__ == "__main__":
    main()