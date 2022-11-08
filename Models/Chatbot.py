import nltk
import pandas as pd

from nltk import word_tokenize
from nltk.tag import untag
from nltk import UnigramTagger
from nltk.corpus import indian
nltk.download('punkt')
nltk.download('indian')


pd.set_option('display.max_columns', None)  
pd.set_option('display.expand_frame_repr', False)
pd.set_option('max_colwidth', -1)


def train_POS_tagger():
  #Load data
  tagged_set = 'marathi.pos'
  articles = indian.sents(tagged_set)
  count = 0
  for sentence in articles[0]:
      print(sentence)     #View the dataset
  sentence1 = " ".join(articles[0])
  count=len(articles)  #Size of dataset
  #print(count)


  # Split dataset into training and testing
  train_perc = .9
  train_rows = int(train_perc*count)
  test_rows = train_rows + 1
  #print(train_rows,test_rows)
  data = indian.tagged_sents(tagged_set)
  train_data = data[:train_rows] 
  test_data = data[test_rows:]


  #Combining unigram tagger with backoff tagging
  # Train the unigram model
  unigram_tagger = UnigramTagger(train_data,backoff=nltk.DefaultTagger('NN'))
  # Test it on a single sentence
  unigram_tagger.tag(untag(test_data[0]))
  unigram_tag.tag(untag(test_data[0]))
  unigram_tagger.evaluate(test_data)  #Evaluation of new model

  #Generalized function that would return the POS tags in a structured table format
  from collections import defaultdict