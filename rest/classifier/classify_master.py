#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
======================================================
Classifier for features
======================================================
"""
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.externals import joblib

from collections import Counter

dict_vectorizer = DictVectorizer()
tfidf_transformer = TfidfTransformer()
clf = MultinomialNB(alpha=.01)

def weight_train_vectors(vectors):
    """
    Weight train feature vectors
    """
    sparse_matrix = dict_vectorizer.fit_transform(vectors)
    sparse_tf_idf = tfidf_transformer.fit_transform(sparse_matrix)

    return sparse_tf_idf


def weight_test_vectors(vectors):
    """
    Weight test feature vectors
    """
    sparse_matrix = dict_vectorizer.transform(vectors)
    sparse_tf_idf = tfidf_transformer.transform(sparse_matrix)

    return sparse_tf_idf


def train(train_set, categories):
    """
    Train Classifier on feature vectors
    in: sparse matrix, labels sequence
    """
    clf.fit(train_set, categories)

def predict(test_set):
    """
    Predict results
    in: sparse matrix
    """
    pred = clf.predict(test_set)
    return pred

def save_on_disk(filename):
    """
    Save Classifier on Disk
    """
    joblib.dump(clf, filename, compress=9)

def load_from_disk(filename):
    """
    Load Classifier from disk
    """
    clf = joblib.load(filename)