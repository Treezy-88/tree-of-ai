```python
import actions
from utils import preprocess_data, train_model, create_agent, deploy_agent

class ActionHandler:
    def __init__(self):
        self.actions = actions.Action()

    def handle_action(self, action_name, data):
        if action_name == 'retrieve_information':
            return self.actions.retrieve_information(data)
        elif action_name == 'execute_command':
            return self.actions.execute_command(data)
        elif action_name == 'provide_recommendation':
            return self.actions.provide_recommendation(data)
        else:
            return "Invalid action"

    def handle_agent_creation(self, agent_data):
        preprocessed_data = preprocess_data(agent_data)
        model = train_model(preprocessed_data)
        agent = create_agent(model)
        return deploy_agent(agent)

    def handle_agent_action(self, agent, action_name, data):
        if action_name == 'retrieve_information':
            return agent.retrieve_information(data)
        elif action_name == 'execute_command':
            return agent.execute_command(data)
        elif action_name == 'provide_recommendation':
            return agent.provide_recommendation(data)
        else:
            return "Invalid action"
```