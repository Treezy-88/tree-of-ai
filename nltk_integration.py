```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def nltk_tokenization(text):
    """
    Function to tokenize text using NLTK
    """
    return word_tokenize(text)

def nltk_remove_stopwords(tokenized_text):
    """
    Function to remove stopwords from tokenized text using NLTK
    """
    stop_words = set(stopwords.words('english'))
    return [word for word in tokenized_text if word not in stop_words]

def nltk_lemmatization(tokenized_text):
    """
    Function to lemmatize tokenized text using NLTK
    """
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokenized_text]

def nltk_preprocess_text(text):
    """
    Function to preprocess text using NLTK
    """
    tokenized_text = nltk_tokenization(text)
    tokenized_text = nltk_remove_stopwords(tokenized_text)
    return nltk_lemmatization(tokenized_text)
```