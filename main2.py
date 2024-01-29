import numpy as np  # подключение библиотеки numpy


def activate(summ):
    if summ >= 0.5:
        return 1
    else:
        return 0


class Neuron:  # класс Neuron
    def __init__(self, weights):  # конструктор (установка веса входов нейрона)
        self.weights = weights

    def feedforward(self, inputs):  # функция получения скалярного произведения от входа и веса
        total = np.dot(self.weights, inputs)
        return activate(total)


class OurNeuralNetwork:
    def __init__(self):
        self.x1 = Neuron([-1, 1])
        self.x2 = Neuron([-1, 1])
        self.o1 = Neuron([1, 1])

    def feedforward(self, vvod):
        out_x1 = self.x1.feedforward(vvod)
        print("Вывод с первого нейрона первого слоя=", out_x1)
        out_x2 = self.x2.feedforward(vvod)
        print("Вывод со второго нейрона первого слоя=", out_x2)
        out_o1 = self.o1.feedforward(np.array([out_x1, out_x2]))
        return out_o1


network = OurNeuralNetwork()
x = np.array([0, 1])
print("Y=", network.feedforward(x))
