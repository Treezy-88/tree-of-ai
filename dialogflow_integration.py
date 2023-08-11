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

    def process_response(self, response):
        result = response.query_result
        intent = result.intent.display_name
        confidence = result.intent_detection_confidence
        fulfillment_text = result.fulfillment_text
        return intent, confidence, fulfillment_text
```