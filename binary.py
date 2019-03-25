# -*- coding: utf-8 -*-

import os
import ast
import csv
from lematization import lemm_str


def search(query: str, index_csv_path: str) -> [str]:
    lemms = lemm_str(query)
    doc_lists = []

    with open(index_csv_path) as f:
        reader = csv.DictReader(f, delimiter=',')
        for line in reader:
            for word in lemms:
                doc_lists.append(ast.literal_eval(line.get(word, '[]')))

    result = set()
    if len(doc_lists) > 0:
        result.update(set(doc_lists[0]))

    for docs in doc_lists:
        result.intersection_update(docs)
    return list(result)

if __name__ == "__main__":
    print(search( "релиз Firefox", "./inverted_index.csv"))


