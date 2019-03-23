import os
import csv
import math
from typing import List
from document import Document
from document import read_docs



#
#  Inverted index
#  
def inverted_index(documents: List[Document]) -> {str, List[Document]}:
    all_words = set()
    for document in documents:
        all_words.update(set(document.words))

    print("all_words len " + str(len(all_words)))

    word_to_doc_map = {}
    for word in all_words:
        word_to_doc_map.setdefault(word, [])
        doc_list = word_to_doc_map[word]
        for document in documents:
            if word in document.words:
                doc_list.append(document)

    return word_to_doc_map

def write_to_csv(word_to_doc_map: {str, List[Document]}, csv_path: str):
    with open(csv_path, 'w', newline='') as f:
        prepared_map = {}
        for item in word_to_doc_map.items():
            prepared_map[item[0]] = list(map(lambda doc: doc.name, item[1]))
        table = csv.DictWriter(f, prepared_map.keys())
        table.writeheader()
        table.writerow(prepared_map)


    
if __name__ == "__main__":
    path_to_lemms = "./lem"
    docs = read_docs(path_to_lemms)
    index = inverted_index(docs)
    write_to_csv(index, "./inverted_index.csv")
    











