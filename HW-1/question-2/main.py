# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


class DocumentVector:
    def __init__(self, hash_document, size, index):
        self.vector = hash_document
        self.size = size
        self.index = index

    def dot(self, document_vector):
        dot_product = 0
        for key, value in self.vector.items():
            occurrence = document_vector.vector.get(key, 0)
            dot_product += occurrence * value
        return dot_product


def init_vector(document):
    hash_document = {}
    vector_len_square = 0
    for word in document.split(" "):
        if word in hash_document:
            vector_len_square += 2 * hash_document[word] + 1
            hash_document[word] += 1
        else:
            hash_document[word] = 1
            vector_len_square += 1
    return hash_document, math.sqrt(vector_len_square)


def main():
    doc_num = int(input())
    doc_list = []
    for i in range(doc_num):
        text = str(input())
        hash_document, size = init_vector(text)
        doc_list.append(DocumentVector(hash_document, size, i + 1))

    for doc in doc_list:
        most_similar_doc = 0
        most_similarity = 0
        for other in doc_list:
            if doc != other:
                pearson_correlation = doc.dot(other) / (doc.size * other.size)
                if pearson_correlation > most_similarity:
                    most_similar_doc = other.index
                    most_similarity = pearson_correlation
        print(most_similar_doc)


if __name__ == '__main__':
    main()
