import pickle

from tf_idf import Tf, Idf, TfIdf


def save_tf(path: str, tf: Tf):
    with open(path, 'wb') as f:
        pickle.dump(tf, f)


def load_tf(path: str) -> Tf:
    with open(path, 'rb') as f:
        tf = pickle.load(f)
    return tf


def save_idf(path: str, idf: Idf):
    with open(path, 'wb') as f:
        pickle.dump(idf, f)


def load_idf(path: str) -> Idf:
    with open(path, 'rb') as f:
        idf = pickle.load(f)
    return idf


def save_tf_idf(path: str, tf_idf: TfIdf):
    with open(path, 'wb') as f:
        pickle.dump(tf_idf, f)


def load_tf_idf(path: str) -> TfIdf:
    with open(path, 'rb') as f:
        tf_idf = pickle.load(f)
    return tf_idf
