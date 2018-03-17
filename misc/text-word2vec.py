#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gensim
import logging
import os


class WikiCorpus(object):
    '''Corpus class which allows to read recursively a set of directories
    containing raw text documents'''

    def __init__(self, directory):
        self.directory = directory

    def __iter__(self):
        for subdir, dirs, files in os.walk(self.directory):
            for f in files:
                for line in open(os.path.join(subdir, f), 'rt'):
                    yield line.split()


                    
if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    CORPUSDIR = 'YOUR_CORPUS_DIR'
    sentences = WikiCorpus(CORPUSDIR)

    logging.info('Building vocabulary and training')
    model = gensim.models.Word2Vec(sentences, min_count=10, size=200, workers=2)
    logging.info('Saving the model...')
    model.save('./efe-200.w2v')
    logging.info('Done')

