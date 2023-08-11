```python
import torch
import torch.nn as nn
import torch.optim as optim

class PyTorchModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(PyTorchModel, self).__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), 1)
        hidden = self.i2h(combined)
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def initHidden(self):
        return torch.zeros(1, self.hidden_size)

def train_model(train_data, model, criterion, optimizer):
    for epoch in range(100):  
        for data in train_data:
            input_tensor, target_tensor = data
            hidden = model.initHidden()
            model.zero_grad()

            loss = 0
            for i in range(input_tensor.size(0)):
                output, hidden = model(input_tensor[i], hidden)
                l = criterion(output, target_tensor[i])
                loss += l

            loss.backward()
            optimizer.step()

def create_pytorch_model(input_size, hidden_size, output_size):
    model = PyTorchModel(input_size, hidden_size, output_size)
    return model

def integrate_pytorch(input_size, hidden_size, output_size, train_data):
    model = create_pytorch_model(input_size, hidden_size, output_size)
    criterion = nn.NLLLoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)
    train_model(train_data, model, criterion, optimizer)
    return model
```
