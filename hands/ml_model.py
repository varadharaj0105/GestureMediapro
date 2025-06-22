import os
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier

MODEL_PATH = "hands/gesture_model.pkl"

class GestureClassifier:
    def __init__(self):
        self.model = None
        if os.path.exists(MODEL_PATH):
            with open(MODEL_PATH, "rb") as f:
                self.model = pickle.load(f)

    def train(self, data, labels):
        self.model = RandomForestClassifier(n_estimators=100)
        self.model.fit(data, labels)

        with open(MODEL_PATH, "wb") as f:
            pickle.dump(self.model, f)

    def predict(self, landmarks):
        if self.model is None:
            return None
        landmarks = np.array(landmarks).reshape(1, -1)
        return self.model.predict(landmarks)[0]

    def is_trained(self):
        return self.model is not None
