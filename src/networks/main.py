import mnist_loader
import binary_number_loader
import network
import numpy as np
from matplotlib import pyplot as plt

# training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
# net = network.Network([784, 20, 10])

# print(test_data)

training_data, test_data = binary_number_loader.load_binary_numbers()
# print(test_data)
net = network.Network([16, 10, 4])
#
results = net.SGD(training_data, 30, 20, 3.0, test_data=test_data)

plt.plot(results)
plt.savefig('epochs.png')
