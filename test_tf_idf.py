
import tf_idf_loader as til
import document as dc
import tf_idf_calculator as tic

if __name__ == "__main__":
    tf_idf = til.load_tf_idf('./tf_idf/tf_idf.pickle')
    k = list(tf_idf.keys())[666]
    print(k)
    for i in tf_idf[k].items():
        if i[1] != 0:
            print(i[0].name + ' ' + str(i[1]))

    docs = dc.read_docs('./lem')
    doc = list(filter(lambda x: x.name == '85.txt', docs))[0]

    print('tf ' + str(tic.tf(k, doc)))
    print('idf ' + str(tic.idf(k, docs)))
