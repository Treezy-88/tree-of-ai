```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokens):
    return [token for token in tokens if token not in stop_words]

def lemmatize_tokens(tokens):
    return [lemmatizer.lemmatize(token) for token in tokens]

def tag_parts_of_speech(tokens):
    return pos_tag(tokens)

def preprocess_text(text):
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)
    tagged_tokens = tag_parts_of_speech(tokens)
    return tagged_tokens
```