```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from utils import preprocess_data

class TensorFlowIntegration:
    def __init__(self):
        self.model = None

    def create_model(self, input_shape):
        self.model = Sequential()
        self.model.add(LSTM(128, input_shape=(input_shape), activation='relu', return_sequences=True))
        self.model.add(Dropout(0.2))

        self.model.add(LSTM(128, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(32, activation='relu'))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(10, activation='softmax'))

    def compile_model(self):
        self.model.compile(loss='sparse_categorical_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])

    def train_model(self, train_data, train_labels, epochs=5):
        preprocessed_data, preprocessed_labels = preprocess_data(train_data, train_labels)
        self.model.fit(preprocessed_data, preprocessed_labels, epochs=epochs)

    def predict(self, data):
        preprocessed_data = preprocess_data(data)
        return self.model.predict(preprocessed_data)

    def save_model(self, file_path):
        self.model.save(file_path)

    def load_model(self, file_path):
        self.model = tf.keras.models.load_model(file_path)
```