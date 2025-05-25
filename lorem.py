import random

class Random:
    def __init__(self, Min: int, Max: int) -> None:
        self.Min = Min
        self.Max = Max

lorem = [
    "adipisci",
    "aliquam",
    "amet",
    "consectetur",
    "dolor",
    "dolore",
    "dolorem",
    "eius",
    "est",
    "et",
    "incidunt",
    "ipsum",
    "labore",
    "magnam",
    "modi",
    "neque",
    "non",
    "numquam",
    "porro",
    "quaerat",
    "qui",
    "quia",
    "quisquam",
    "sed",
    "sit",
    "tempora",
    "ut",
    "velit",
    "voluptatem",
    "lorem",
    "adipiscing",
    "elit",
    "do",
    "eiusmod",
    "tempor",
    "incididunt",
    "magna",
    "aliqua",
    "enim",
    "ad",
    "minim",
    "veniam",
    "quis",
    "nostrud",
    "exercitation",
    "ullamco",
    "laboris",
    "nisi",
    "ex",
    "ea",
    "commodo",
    "consequat",
    "duis",
    "aute",
    "irure",
    "in",
    "reprehenderit",
    "voluptate",
    "esse",
    "cillum",
    "eu",
    "fugiat",
    "nulla",
    "pariatur",
]

def words(wordsNumber: int = 1, toUpperAllFirstLetter: bool = False):
    result: str = ' '.join(random.choices(lorem, k=wordsNumber))
    if toUpperAllFirstLetter:
        result = result[0].upper()+result[1:]
    return result

def sentenses(sentensesNumber: int = 1, wordsNumberPerSentense: int | Random = 3, toUpperAllFirstLetter: bool = False):
    result: str = ''
    for i in range(sentensesNumber):
        result += f'{words(wordsNumberPerSentense \
                           if isinstance(wordsNumberPerSentense, int) else random.randint(wordsNumberPerSentense.Min, 
                                                                                              wordsNumberPerSentense.Max)
                           , toUpperAllFirstLetter)}.'
        if i + 1 != sentensesNumber:
            result += ' '
    return result

def paragraphs(paragraphsNumber: int = 1, sentensesNumberPerParagraph: int | Random = 3, wordsNumberPerSentense: int | Random = 3, toUpperAllFirstLetter: bool = False):
    result: str = ''
    for i in range(paragraphsNumber):
        result += sentenses(sentensesNumberPerParagraph \
                            if isinstance(sentensesNumberPerParagraph, int) else random.randint(sentensesNumberPerParagraph.Min, 
                                                                                              sentensesNumberPerParagraph.Max)
                            , wordsNumberPerSentense
                            , toUpperAllFirstLetter)
        if i + 1 != paragraphsNumber:
            result += '\n'
    return result

def essays(essaysNumber: int = 1, paragraphsNumberPerEssay: int | Random = 3, sentensesNumberPerParagraph: int | Random = 3, wordsNumberPerSentense: int | Random = 3, toUpperAllFirstLetter: bool = False):
    result: str = ''
    for i in range(essaysNumber):
        result += paragraphs(paragraphsNumberPerEssay \
                             if isinstance(paragraphsNumberPerEssay, int) else random.randint(paragraphsNumberPerEssay.Min, 
                                                                                              paragraphsNumberPerEssay.Max)
                             , sentensesNumberPerParagraph
                             , wordsNumberPerSentense
                             , toUpperAllFirstLetter)
        if i + 1 != essaysNumber:
            result += '\n\n'
    return result


def ipsum() -> str:
    return essays(random.randint(2, 4),
                  Random(2, 5),
                  Random(2, 6),
                  Random(2, 7),
                  True)
