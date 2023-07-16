```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('wordnet')
nltk.download('stopwords')

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def tokenize_text(text):
    return word_tokenize(text)

def remove_stopwords(tokenized_text):
    return [word for word in tokenized_text if word not in stop_words]

def lemmatize_text(tokenized_text):
    return [lemmatizer.lemmatize(word) for word in tokenized_text]

def tag_parts_of_speech(tokenized_text):
    return pos_tag(tokenized_text)

def extract_entities(tagged_text):
    return ne_chunk(tagged_text)

def preprocess_text(text):
    tokenized_text = tokenize_text(text)
    tokenized_text = remove_stopwords(tokenized_text)
    tokenized_text = lemmatize_text(tokenized_text)
    tagged_text = tag_parts_of_speech(tokenized_text)
    entities = extract_entities(tagged_text)
    return tokenized_text, tagged_text, entities
```