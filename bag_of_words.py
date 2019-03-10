import nltk.tokenize
import numpy as np


def tokenize(paragraphs):
    """
    Extracts all words from sentences (ignoring stopwords), returns as sorted list with no duplicates
    :param sentences:
    :return: words: sorted list of all words in sentences
    """
    words = []
    for paragraph in paragraphs:
        w = nltk.word_tokenize(paragraph)
        words.extend(w)
    words = set(words)  # remove duplicates, stopwords, and punctuation
    vocab = [w.lower() for w in words if w not in nltk.corpus.stopwords.words('english') and w.isalpha()]
    return vocab


def generate(paragraphs, questions):
    """
    generates overall vocabulary and builds wordcount vectors for each paragraph
    :param sentences:
    :param sentences:
    :return: matrix of word count vectors (one per sentence)
    """
    paragraphs.extend(questions)
    vocab = tokenize(paragraphs)
    mat = np.zeros([len(vocab), len(paragraphs)], dtype=int)
    for index, paragraph in enumerate(paragraphs):
        words = nltk.word_tokenize(paragraph)
        bag_vector = np.zeros(len(vocab), dtype=int)
        for w in words:
            for i, word in enumerate(vocab):
                if word == w:
                    bag_vector[i] += 1
        mat[:, index] = bag_vector
    return mat
