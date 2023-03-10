import pytest
import numpy as np
from neural_network import NeuralNetwork, sigmoid, sigmoid_prime


def test_init_neural_network():
    """
    Test initializing the Neural Network class
    """
    nn = NeuralNetwork([784, 16, 16, 10])
    assert len(nn.weights) == 3
    assert len(nn.biases) == 3


def test_sigmoid():
    # Test the sigmoid function with different values of z_vector
    assert np.isclose(sigmoid(0), 0.5, rtol=1e-05, atol=1e-08), "Test case 1 failed"
    assert np.isclose(sigmoid(-100), 0, rtol=1e-05, atol=1e-08), "Test case 2 failed"
    assert np.isclose(sigmoid(100), 1, rtol=1e-05, atol=1e-08), "Test case 3 failed"


def test_sigmoid_prime():
    # Test the sigmoid_prime function with different values of z_vector
    assert np.isclose(sigmoid_prime(0), 0.25, rtol=1e-05, atol=1e-08), "Test case 1 failed"
    assert np.isclose(sigmoid_prime(-100), 0, rtol=1e-05, atol=1e-08), "Test case 2 failed"
    assert np.isclose(sigmoid_prime(100), 0, rtol=1e-05, atol=1e-08), "Test case 3 failed"


def test_feedforward():
    # Set up a mock neural network with test biases and weights
    mock_network = NeuralNetwork([1,2,3])
    mock_network.biases = [np.array([1, 2, 3]), np.array([4, 5, 6])]
    mock_network.weights = [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                            np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])]

    # Set up test input data
    test_input = np.array([1, 2, 3])

    # Calculate the expected result
    expected_result = sigmoid(np.dot(mock_network.weights[0], test_input) + mock_network.biases[0])
    expected_result = sigmoid(np.dot(mock_network.weights[1], expected_result) + mock_network.biases[1])

    # Compare the expected result to the result of the feedforward function
    result = mock_network.feedforward(test_input)
    assert np.allclose(result, expected_result), f"Expected {expected_result}, but got {result}"

def test_cost_derivative():
    # Create a random output and target values
    output_layer_activations = np.array([[0.3], [0.7], [0.1]])
    target_values = np.array([[1], [0], [1]])
    # Compute the cost derivative using the neural network's method
    nn = NeuralNetwork([3, 2, 1])
    cost_derivative = nn.cost_derivative(output_layer_activations, target_values)
    # Check that the shape of the result is correct
    assert cost_derivative.shape == (3, 1)
    # Check that the result is correct
    expected_result = np.array([[-0.7], [0.7], [-0.9]])
    assert np.allclose(cost_derivative, expected_result)
