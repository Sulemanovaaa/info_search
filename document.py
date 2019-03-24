import os


class Document:

    def __init__(self, name: str, words: [str]):
        self.name = name
        self.words = []
        self.words.extend(words)

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)


#
# set name of docs as simple name of file
#
def read_docs(path_to_dir: str) -> [Document]:
    rawdocs = os.listdir(path_to_dir)
    documents = []
    for rawdoc in rawdocs:
        f = open(path_to_dir + '/' + rawdoc, 'r')
        document = Document(rawdoc, [])
        for line in f:
            for word in line.split():
                document.words.append(word)
        f.close()
        documents.append(document)
    return documents
