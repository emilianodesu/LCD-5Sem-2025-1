import numpy as np

def step_function(x):  # Función de activación
    return 1 if x >= 0 else 0

class Perceptron:
    def __init__(self):
        self.weights = np.random.rand(2)  # Número de entradas
        self.bias = np.random.rand(1)

    # Predicción
    def predict(self, inputs):  # Agregar self
        total_input = np.dot(inputs, self.weights) + self.bias
        return step_function(total_input)

    # Entrenamiento
    def train(self, training_inputs, labels, epochs=5):  # Agregar self
        for epoch in range(epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                # Ajuste de pesos y sesgo (en caso de error)
                self.weights += error * inputs  # Actualización de los pesos
                self.bias += error  # Actualización del sesgo

training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])

perceptron = Perceptron()
perceptron.train(training_inputs, labels, epochs=10)

# Probando nuestro perceptron :D
for inputs in training_inputs:
    print(f"{inputs} -> {perceptron.predict(inputs)}")
