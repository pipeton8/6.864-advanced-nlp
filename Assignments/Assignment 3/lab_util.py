import re

class Tokenizer:
  def __init__(self, min_occur=10):
    self.word_to_token = {}
    self.token_to_word = {}
    self.word_count = {}

    self.word_to_token['<unk>'] = 0
    self.token_to_word[0] = '<unk>'
    self.vocab_size = 1

    self.min_occur = min_occur

  def fit(self, corpus):
    for review in corpus:
      review = review.strip().lower()
      words = re.findall(r"[\w']+|[.,!?;]", review)
      for word in words:
          if word not in self.word_count:
              self.word_count[word] = 0
          self.word_count[word] += 1

    for review in corpus:
      review = review.strip().lower()
      words = re.findall(r"[\w']+|[.,!?;]", review)
      for word in words:
        if self.word_count[word] < self.min_occur:
          continue
        if word in self.word_to_token:
          continue
        self.word_to_token[word] = self.vocab_size
        self.token_to_word[self.vocab_size] = word
        self.vocab_size += 1

  def tokenize(self, corpus):
    tokenized_corpus = []
    for review in corpus:
      review = review.strip().lower()
      words = re.findall(r"[\w']+|[.,!?;]", review)
      tokenized_review = []
      for word in words:
        if word not in self.word_to_token:
          tokenized_review.append(0)
        else:
          tokenized_review.append(self.word_to_token[word])
      tokenized_corpus.append(tokenized_review)
    return tokenized_corpus

  def de_tokenize(self, tokenized_corpus):
    corpus = []
    for tokenized_review in tokenized_corpus:
      review = []
      for token in tokenized_review:
        review.append(self.token_to_word[token])
      corpus.append(" ".join(review))
    return corpus
