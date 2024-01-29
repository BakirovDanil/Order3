"""Создание класса NeuralNetwork"""


class NeuralNetwork:
    def __init__(self, layers, weights):  # конструктор класса
        self.layers = layers  # количество нейронов на каждом слое
        self.weights = weights  # вес связей между нейронами
        print(self.weights)  # вывод веса связей между нейронами

    def feed_forward(self, inputs):
        neurons = []
        print("Количество слоев в сети: ", len(self.layers))
        for c in range(len(self.layers) - 1):  # цикл по количеству слоев
            outputs = []  # выходные значения со слоя
            for j in range(self.layers[c + 1]):
                summ = 0
                for i in range(self.layers[c]):
                    summ += inputs[i] * self.weights[c][i][j]
                outputs.append(self.activate(summ))
            inputs = outputs
            if c < 1:
                neurons.append(outputs)
            inputs = inputs
            print(outputs)

    def activate(self, summ):
        if summ >= 0.5:
            return 1
        else:
            return 0


my = NeuralNetwork([2, 2, 1], [[[-1, 1], [-1, 1]], [[-1], [1]]])
my.feed_forward([0, 0])  # 0
my.feed_forward([0, 1])  # 1
my.feed_forward([1, 0])  # 1
my.feed_forward([1, 1])  # 0
