from typing import TypedDict, Any

class Channel:
    def __init__(self, users: dict = {'admin': True, 'user01': False, 'user02': False}, usingUser: int = 0, passwords: list = ['admin123', '', ''], password: str = 'admin123') -> None:
        if len(users) == len(passwords):
            self.__user = users
            self.__using = usingUser
            self.__msg: list = []
            self.__password: list = passwords
            self.__requests: list[str] = []
        else: raise Exception()
        if self.__password[self.__using] != password: raise Exception()
    
    def changeUser(self, usingUser: int = 0, password: str = '') -> None:
        if self.__password[usingUser] == password: self.__using = usingUser
        else: print('password is wrong, cannot log in this user')
    
    def chat(self, msg: str = 'Hello?') -> None: self.__msg.append(f'{list(self.__user.keys())[self.__using]}: {msg}')
    
    def showChatMsg(self):
        for i in self.__msg: print(i)
    
    def showUsers(self):
        for k, v in self.__user.items(): print(f'{k}: {v}')
    
    def createOrSet(self, name: str = 'user01', type: bool = True) -> None:
        if self.__user[list(self.__user.keys())[self.__using]]: self.__user[name] = type
        else: print(f'This user "{list(self.__user.keys())[self.__using]}" is not an admin')
    
    def removeAll(self):
        if self.__user[list(self.__user.keys())[self.__using]]: self.__msg = []
        else: print(f'This user "{list(self.__user.keys())[self.__using]}" is not an admin')
    
    def sendBot(self, name: str = 'Bot', msg: str = 'pls don\'t spam'):
        if self.__user[list(self.__user.keys())[self.__using]]: self.__msg.append(f'{name}(Bot): {msg}')
        else: print(f'This user "{list(self.__user.keys())[self.__using]}" is not an admin')
    
    def changePassword(self, oldPassword: str, newPassword: str):
        if self.__password[self.__using] == oldPassword: self.__password[self.__using] = newPassword
        else: print('old password is worng, cannot set a new password')
    
    def sendAdminRequest(self):
        if self.__user[list(self.__user.keys())[self.__using]]: print('u r an admin, nothing can request')
        else:
            self.__requests.append(f'{list(self.__user.keys())[self.__using]} want to be an admin')
            print('request sent')
    
    def checkRequests(self):
        if self.__user[list(self.__user.keys())[self.__using]]: print(self.__requests)
        else: return f'This user "{list(self.__user.keys())[self.__using]}" is not an admin'
    
    def markRead(self):
        if self.__user[list(self.__user.keys())[self.__using]]: self.__requests = []
        else: print(f'This user "{list(self.__user.keys())[self.__using]}" is not an admin')

class SecurityQuestion(TypedDict):
    title: str
    answer: str

class privateNotes:
    def __init__(self, password: str = "", securityQuestion: SecurityQuestion = {"title": "", "answer": ""}) -> None:
        self.__password = password
        self.__title = securityQuestion["title"]
        self.__answer = securityQuestion["answer"]
        self.__note: dict = {}
    
    def showSecurityTitle(self) -> str: return self.__title

    def changePassword(self, answer: str, newPassword: str):
        if answer == self.__answer: self.__password = newPassword
        else: print('security question is wrong')
    
    def write(self, password: str, head: str, body: str):
        if self.__password == password: self.__note[head] = body
        else: print('password is wrong')
    
    def see(self, password: str, head: str) -> str:
        if self.__password == password: return self.__note[head]
        else: return 'password is wrong'

class form:
    def __init__(self) -> None:
        self.__data: list[list] = []
    
    def add(self, val: list):
        a: list = []
        for i in val:
            a.append(str(i))
        self.__data.append(a)
    
    def show(self, better: bool = True) -> str:
        if better:
            lenlist: list[int] = []
            for k in self.__data:
                lenlist.append(len(max(k, key=len)))
            ll = max(lenlist)
            a = ''
            for i in self.__data:
                a = a+"|"
                for j in i:
                    a = a+self.__fill(str(j), ll)+'|'
                a = a+'\n'
            return a
        else:
            a = ''
            for i in self.__data:
                a = a+"|"
                for j in i:
                    a = a+str(j)+'|'
                a = a+'\n'
        return a
    
    def change(self, y: int, x: int, value):
        (self.__data[y])[x] = str(value)
    
    def addBatch(self, y: int, x: int, val):
        h: list = []
        for _ in range(x): h.append(str(val))
        for _ in range(y): self.__data.append(h)
    
    def stdShow(self) -> list:
        return self.__data
    
    def showOne(self, y: int, x: int):
        return (self.__data[y])[x]
    
    def autoFill(self, data1Y: int, data1X: int, data2Y: int, data2X: int, fillY: int, fillX: int, type: str = 'number'):
        if type == 'number':
            a = float(self.showOne(data1Y, data1X))
            b = float(self.showOne(data2Y, data2X))
            c = b-a
            self.change(fillY, fillX, str(b+c))
        else: print('this type is not developed')
    
    def __fill(self, val: str, how: int) -> str:
        i = how - int(len(val))
        for _ in range(i):
            val = val + " "
        return val

class testPaper:
    def __init__(self) -> None:
        self.question: list[str] = []
        self.answer: list[str] = []
        self.score: list[float] = []
    
    def topic(self, question: str, answer: str, score: float) -> None:
        self.question.append(question)
        self.answer.append(answer)
        self.score.append(score)

    def __total(self):
        return sum(number for number in self.score if isinstance(number, (int, float)))

    def start(self):
        score = 0
        print(f"You must get {self.__total()} scores to win A+")
        wrongTopicBook: list = []
        for i in range(len(self.question)):
            asw = input(self.question[i]+"\n(Enter your answer)> ")
            if asw == self.answer[i]: score += self.score[i]
            else: wrongTopicBook.append(f"------------------------------\nWrong topic #{i}\nquestion: {self.question[i]}\nyour answer   : {asw}\ncorrect answer: {self.answer[i]}")
            print("Next")
        print(f"Your score is {score}")
        if len(wrongTopicBook) != 0:
            for i in wrongTopicBook: print(i)
        print("------------------------------")

class Iterator:
    def __init__(self, data: list[Any]) -> None:
        self.__data = data
        self.__index = -1
        if len(data) == 0:
            del self
            raise Exception("List is empty")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__index = 0 if self.__index == len(self.__data) -1 else self.__index + 1
        return self.__data[self.__index]


def main() -> None:
    a = Iterator([
        '\x1b[5m\x1b[4m\x1b[30mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[31mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[32mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[33mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[34mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[35mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[36mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[37mtext\x1b[0m',
        '\x1b[5m\x1b[4m\x1b[38mtext\x1b[0m',
    ])
    for _ in range(24):
        print(next(a))

if __name__ == "__main__":
    main()
