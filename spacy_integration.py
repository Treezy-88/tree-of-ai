```python
import spacy

class SpacyIntegration:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def tokenize(self, text):
        doc = self.nlp(text)
        return [token.text for token in doc]

    def entity_recognition(self, text):
        doc = self.nlp(text)
        return [(ent.text, ent.label_) for ent in doc.ents]

    def pos_tagging(self, text):
        doc = self.nlp(text)
        return [(token.text, token.pos_) for token in doc]

    def lemmatization(self, text):
        doc = self.nlp(text)
        return [token.lemma_ for token in doc]

    def dependency_parsing(self, text):
        doc = self.nlp(text)
        return [(token.text, token.dep_, token.head.text) for token in doc]
```