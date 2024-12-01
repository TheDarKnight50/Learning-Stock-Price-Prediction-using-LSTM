"""
Linear Regression Assignment with Bias Term

Complete the following functions to implement linear regression.
Each function will be tested in the main function.
"""

import numpy as np

def mean_squared_error(y_true, y_pred):
    """
    Calculate Mean Squared Error (MSE) between true and predicted values.
    
    Parameters:
    y_true (numpy array): True target values
    y_pred (numpy array): Predicted target values
    
    Returns:
    float: MSE value
    """
    # TODO: Implement the formula for MSE
    pass


def compute_gradient(X, y, weights):
    """
    Compute the gradient for linear regression.
    
    Parameters:
    X (numpy array): Feature matrix (n_samples x n_features)
    y (numpy array): Target values
    weights (numpy array): Model weights
    
    Returns:
    numpy array: Gradient vector
    """
    # TODO: Implement the gradient computation
    pass


def train_linear_regression(X, y, learning_rate, epochs):
    """
    Train a linear regression model using gradient descent.
    
    Parameters:
    X (numpy array): Feature matrix (n_samples x n_features)
    y (numpy array): Target values
    learning_rate (float): Learning rate for gradient descent
    epochs (int): Number of iterations
    
    Returns:
    numpy array: Final weights
    """
    # TODO: Initialize weights, iterate over epochs, and update weights
    pass


def predict(X, weights):
    """
    Predict the target values using the learned weights.
    
    Parameters:
    X (numpy array): Feature matrix (n_samples x n_features)
    weights (numpy array): Model weights
    
    Returns:
    numpy array: Predicted target values
    """
    # TODO: Implement the prediction logic
    pass


def generate_data(m, c, num_samples, noise_level):
    """
    Generate data based on a standard line y = mx + c with noise.
    
    Parameters:
    m (float): Slope of the line
    c (float): Intercept of the line
    num_samples (int): Number of data points to generate
    noise_level (float): Standard deviation of noise to add
    
    Returns:
    tuple: Feature matrix X and target vector y
    """
    X = np.linspace(0, 10, num_samples).reshape(-1, 1)
    noise = np.random.normal(0, noise_level, num_samples)
    y = m * X.squeeze() + c + noise
    return X, y


def main():
    """
    Main function to test all components of the assignment.
    """
    # Generate data for y = 2x + 3 with some noise
    m, c = 2, 3
    num_samples = 50
    noise_level = 1.0
    X, y = generate_data(m, c, num_samples, noise_level)
    
    # Append a column of ones to X for the bias term
    X_with_bias = np.hstack((np.ones((X.shape[0], 1)), X))
    
    # Parameters for training
    learning_rate = 0.01
    epochs = 1000
    
    print("Step 1: Training the linear regression model...")
    weights = train_linear_regression(X_with_bias, y, learning_rate, epochs)
    print("Trained weights (should be close to [c, m]):", weights)
    
    print("Step 2: Making predictions...")
    predictions = predict(X_with_bias, weights)
    print("Sample Predictions:", predictions[:5])
    
    print("Step 3: Calculating Mean Squared Error...")
    mse = mean_squared_error(y, predictions)
    print("Mean Squared Error (MSE):", mse)
    
    # Testing correctness
    print("\nTesting individual functions:")
    # Test MSE
    test_y_true = np.array([2, 4, 6])
    test_y_pred = np.array([2.1, 3.9, 5.8])
    print("Test MSE (expected ~0.01):", mean_squared_error(test_y_true, test_y_pred))
    
    # Test gradient computation
    test_X = np.array([[1, 1], [1, 2], [1, 3]])
    test_y = np.array([1, 2, 3])
    test_weights = np.array([0, 1])
    print("Test Gradient (expected ~[-2, -6.67]):", compute_gradient(test_X, test_y, test_weights))


if __name__ == "__main__":
    main()
