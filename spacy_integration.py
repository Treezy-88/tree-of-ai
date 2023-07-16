```python
import spacy

class SpacyIntegration:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def preprocess_data(self, text):
        doc = self.nlp(text)
        return doc

    def tokenize(self, doc):
        tokens = [token.text for token in doc]
        return tokens

    def entity_recognition(self, doc):
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return entities

    def pos_tagging(self, doc):
        pos_tags = [(token.text, token.pos_) for token in doc]
        return pos_tags

    def lemmatization(self, doc):
        lemmas = [token.lemma_ for token in doc]
        return lemmas
```