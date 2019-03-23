import math
from typing import List
from document import Document
from document import read_docs

def tf(word: str, document: Document) -> float:
    if len(document.words) == 0:
        return 0
    return document.words.count(word) / len(document.words)

def idf(word: str, documents: List[Document]) -> float:
    matches = 0
    for doc in documents:
        if word in doc.words:
            matches = matches + 1

    if matches == 0:
        return 0
    return math.log2(len(documents) / matches)

def tf_idf(word: str, document: Document, documents: List[Document]) -> float:
    return tf(word, document) * idf(word, documents)


if __name__ == "__main__":
    docs = read_docs('./lem')
    all_words = set()
    for doc in docs:
        all_words.update(doc.words)

    # TODO



