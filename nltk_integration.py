```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class NLTKIntegration:
    def __init__(self):
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stemmer = PorterStemmer()

    def tokenize(self, text):
        return word_tokenize(text)

    def remove_stopwords(self, tokens):
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [token for token in tokens if token not in stop_words]
        return filtered_tokens

    def stem(self, tokens):
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens]
        return stemmed_tokens

    def preprocess(self, text):
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        tokens = self.stem(tokens)
        return tokens
```