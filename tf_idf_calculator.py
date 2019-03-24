import math

from typing import List, Set

import tf_idf_loader as til
from document import Document
from document import read_docs
from tf_idf import Tf, Idf, TfIdf

Words = Set[str]
Documents = List[Document]


def tf(word: str, document: Document) -> float:
    if len(document.words) == 0:
        return 0
    return document.words.count(word) / len(document.words)


def idf(word: str, documents: Documents) -> float:
    matches = 0
    for document in documents:
        if word in document.words:
            matches = matches + 1

    if matches == 0:
        return 0
    return math.log2(len(documents) / matches)


def tf_idf(word: str, document: Document, documents: Documents) -> float:
    return tf(word, document) * idf(word, documents)


def all_tf(words: Words, documents: Documents) -> Tf:
    all_word_tfs = {}
    for word in words:
        word_tfs = {}
        for document in documents:
            word_tfs[document] = tf(word, document)
        all_word_tfs[word] = word_tfs
    return all_word_tfs


def all_idf(words: Words, documents: Documents) -> Idf:
    all_idfs = {}
    for word in words:
        all_idfs[word] = idf(word, documents)
    return all_idfs


def all_tf_idf(tf: Tf, idf: Idf) -> TfIdf:

    result = {}
    sorted_tf = sorted(tf.items(), key=lambda i: i[0])
    sorted_idf = sorted(idf.items(), key=lambda i: i[0])
    for z in zip(sorted_tf, sorted_idf):
        result[z[0][0]] = dict(map(lambda t: (t[0], t[1] * z[1][1]), z[0][1].items()))
    return result


if __name__ == "__main__":
    docs = read_docs('./lem')
    all_words = set()
    for doc in docs:
        all_words.update(doc.words)

    tfs = all_tf(all_words, docs)
    til.save_tf('./tf_idf/tf.pickle', tfs)
    
    idfs = all_idf(all_words, docs)
    til.save_idf('./tf_idf/idf.pickle', idfs)

    tf_idf_s = all_tf_idf(tfs, idfs)
    til.save_tf_idf('./tf_idf/tf_idf.pickle', tf_idf_s)
