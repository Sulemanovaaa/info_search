import document
import math
import tf_idf_loader as til
import tf_idf_calculator as tic
from tf_idf import Tf, Idf, TfIdf
from lematization import lemm_str
from document import Document
from pagerank import pagerank

def calc_doc_len(doc: Document, tf_idf: TfIdf) -> float:
    result = 0
    for word in doc.words:
        result = result + math.pow(tf_idf.get(word, {}).get(doc, 0), 2)
    return math.sqrt(result)


if __name__ == "__main__":
    query = input("Enter your request:")
    print("You entered" + query)
    lemm = lemm_str(query)
    docs = document.read_docs('./lem')
    query_doc = Document("query", lemm)
    idf = til.load_idf('./tf_idf/idf.pickle')
    tf_idf = til.load_tf_idf('./tf_idf/tf_idf.pickle')

    all_words = set()
    for doc in docs:
        all_words.update(doc.words)

    all_words_list = list(all_words)

    query_map = {}
    for word in lemm:
        word_idf = idf.get(word, 0)
        word_tf = tic.tf(word, query_doc)
        word_tf_idf = word_tf * word_idf
        query_map[word] = word_tf_idf
        print(word)
        print(word_idf)
        print(word_tf)
        print(word_tf_idf)


    answers = []
    query_len = math.sqrt(sum([math.pow(i, 2) for i in query_map.values()]))
    for doc in docs:
        up_def = 0
        for word in lemm:
            up_def += query_map[word] * tf_idf.get(word, {}).get(doc, 0)
        doc_len = calc_doc_len(doc, tf_idf)
        doc_len_x_query_len = doc_len * query_len
        if doc_len_x_query_len > 0:
            answers.append( (doc, up_def / doc_len_x_query_len ) )

    answers = list(map(lambda x: (x[0].name, x[1]), 
            sorted(answers, key=lambda i: i[1], reverse=True)))


