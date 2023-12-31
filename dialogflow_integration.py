```python
import os
from google.cloud import dialogflow

class DialogflowIntegration:
    def __init__(self):
        self.project_id = os.getenv('DIALOGFLOW_PROJECT_ID')
        self.session_client = dialogflow.SessionsClient()

    def detect_intent(self, session_id, text, language_code='en'):
        session = self.session_client.session_path(self.project_id, session_id)
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = self.session_client.detect_intent(session=session, query_input=query_input)
        return response

    def train_agent(self):
        parent = self.session_client.project_agent_path(self.project_id)
        operation = self.session_client.train_agent(parent)
        operation.result()

    def create_intent(self, display_name, training_phrases_parts, message_texts):
        intents_client = dialogflow.IntentsClient()
        parent = intents_client.project_agent_path(self.project_id)
        training_phrases = []
        for training_phrases_part in training_phrases_parts:
            part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
            training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)
        text = dialogflow.Intent.Message.Text(text=message_texts)
        message = dialogflow.Intent.Message(text=text)
        intent = dialogflow.Intent(display_name=display_name, training_phrases=training_phrases, messages=[message])
        response = intents_client.create_intent(parent, intent)
        return response
```