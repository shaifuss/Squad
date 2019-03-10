import json
import nltk
import numpy as np


def tokenize(sentences):
    """
    Extracts all words from sentences, returns as set
    :param sentences:
    :return: words: sorted set of all words in sentences, in list form
    """
    words = []
    for sentence in sentences:
        w = nltk.corpus.word_extraction(sentence)
        words.extend(w)
    clean_words = [w.lower() for w in words if w not in nltk.corpus.stopwords.words('english')]
    clean_words = sorted(list(set(clean_words)))
    return words


def generate(sentences):
    """
    generates overall vocabulary and builds wordcount vectors for each sentence
    :param sentences:
    :return: matrix of word count vectors (one per sentence)
    """
    vocab = tokenize(sentences)
    mat = np.zeros(len(sentences), len(vocab))
    for index, sentence in enumerate(sentences):
        words = nltk.corpus.word_extraction(sentence)
        bag_vector = np.zeros(len(vocab))
        for w in words:
            for i, word in enumerate(vocab):
                if word == w:
                    bag_vector[i] += 1
        mat[:, index] = bag_vector
    return mat


def unpack():
    with open('C:\\Users\\Harriet\\PycharmProjects\\Squad\\dev-v2.0.json') as jfile:
        dataset = json.load(jfile)
        context = []
        qas = []
        for i in range(len(dataset['data'])):   # for each article
            temp = dataset['data'][i]['paragraphs']
            for j in range(len(temp)):          # for each paragraph in given article
                context.append((temp[j]['context']))
                qas.append((temp[j]['qas']))
        # filter out questions
        q_list = []
        for i in range(len(qas)):
            temp = qas[i]
            for j in range(len(temp)):
                q_list.append(temp[j]['question'])







