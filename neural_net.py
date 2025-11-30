import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, lr=0.1):
        self.W1 = np.random.randn(input_size, hidden_size)
        self.W2 = np.random.randn(hidden_size, output_size)
        self.b1 = np.random.randn(hidden_size)
        self.b2 = np.random.randn(output_size)
        self.lr = lr

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_deriv(self, x):
        return x * (1 - x)

    def forward(self, x):
        self.z1 = np.dot(x, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        return self.sigmoid(self.z2)

    def train(self, inputs, targets, epochs=5000):
        for epoch in range(epochs):
            pred = self.forward(inputs)
            error = targets - pred

            delta2 = error * self.sigmoid_deriv(pred)
            delta1 = np.dot(delta2, self.W2.T) * self.sigmoid_deriv(self.a1)

            self.W2 += np.dot(self.a1.T, delta2) * self.lr
            self.b2 += np.sum(delta2, axis=0) * self.lr
            self.W1 += np.dot(inputs.T, delta1) * self.lr
            self.b1 += np.sum(delta1, axis=0) * self.lr
