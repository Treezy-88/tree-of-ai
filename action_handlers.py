```python
import actions
from utils import preprocess_data
from nlp_utils import extract_entities

class ActionHandler:
    def __init__(self):
        self.actions = actions.Action()

    def handle_action(self, action_type, data):
        if action_type == 'collect_data':
            return self.actions.collect_data(data)
        elif action_type == 'preprocess_data':
            preprocessed_data = preprocess_data(data)
            return preprocessed_data
        elif action_type == 'train_bot':
            return self.actions.train_bot(data)
        elif action_type == 'create_agent':
            return self.actions.create_agent(data)
        elif action_type == 'deploy_agent':
            return self.actions.deploy_agent(data)
        else:
            raise ValueError(f'Invalid action type: {action_type}')

    def handle_intent(self, intent, data):
        entities = extract_entities(data)
        if intent == 'collect_data':
            return self.handle_action('collect_data', entities)
        elif intent == 'preprocess_data':
            return self.handle_action('preprocess_data', entities)
        elif intent == 'train_bot':
            return self.handle_action('train_bot', entities)
        elif intent == 'create_agent':
            return self.handle_action('create_agent', entities)
        elif intent == 'deploy_agent':
            return self.handle_action('deploy_agent', entities)
        else:
            raise ValueError(f'Invalid intent: {intent}')
```