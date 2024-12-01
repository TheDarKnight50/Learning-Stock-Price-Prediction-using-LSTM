"""
Logistic Regression Assignment with Bias Term

Complete the following functions to implement logistic regression.
Each function will be tested in the main function.
"""

import numpy as np

def sigmoid(z):
    """
    Compute the sigmoid function for the input z.
    
    Parameters:
    z (numpy array): Input values (linear combination of weights and features)
    
    Returns:
    numpy array: Sigmoid of input z
    """
    # TODO: Implement sigmoid function
    pass


def binary_cross_entropy(y_true, y_pred):
    """
    Compute binary cross-entropy loss.
    
    Parameters:
    y_true (numpy array): True target values (0 or 1)
    y_pred (numpy array): Predicted probabilities (0 to 1)
    
    Returns:
    float: Binary cross-entropy loss
    """
    # TODO: Implement the formula for binary cross-entropy loss
    pass


def compute_gradient(X, y, weights):
    """
    Compute the gradient for logistic regression.
    
    Parameters:
    X (numpy array): Feature matrix (n_samples x n_features)
    y (numpy array): Target values (0 or 1)
    weights (numpy array): Model weights
    
    Returns:
    numpy array: Gradient vector
    """
    # TODO: Implement the gradient computation
    pass


def train_logistic_regression(X, y, learning_rate, epochs):
    """
    Train a logistic regression model using gradient descent.
    
    Parameters:
    X (numpy array): Feature matrix (n_samples x n_features)
    y (numpy array): Target values (0 or 1)
    learning_rate (float): Learning rate for gradient descent
    epochs (int): Number of iterations
    
    Returns:
    numpy array: Final weights
    """
    # TODO: Initialize weights, iterate over epochs, and update weights
    pass


def predict(X, weights, threshold=0.5):
    """
    Predict the binary class labels (0 or 1) using the learned weights.
    
    Parameters:
    X (numpy array): Feature matrix (n_samples x n_features)
    weights (numpy array): Model weights
    threshold (float): Classification threshold (default 0.5)
    
    Returns:
    numpy array: Predicted class labels (0 or 1)
    """
    # TODO: Implement the prediction logic
    pass


def generate_data(num_samples, noise_level):
    """
    Generate synthetic data for logistic regression (binary classification).
    
    Parameters:
    num_samples (int): Number of data points to generate
    noise_level (float): Standard deviation of noise to add
    
    Returns:
    tuple: Feature matrix X and target vector y
    """
    np.random.seed(42)  # For reproducibility
    X = np.random.randn(num_samples, 2)  # Two features
    true_weights = np.array([1.5, -2.0])  # True weights
    bias = -0.5  # True bias
    linear_combination = X @ true_weights + bias
    probabilities = sigmoid(linear_combination + np.random.normal(0, noise_level, num_samples))
    y = (probabilities >= 0.5).astype(int)
    return X, y


def main():
    """
    Main function to test all components of the assignment.
    """
    # Generate synthetic data
    num_samples = 100
    noise_level = 0.1
    X, y = generate_data(num_samples, noise_level)
    
    # Append a column of ones to X for the bias term
    X_with_bias = np.hstack((np.ones((X.shape[0], 1)), X))
    
    # Parameters for training
    learning_rate = 0.1
    epochs = 500
    
    print("Step 1: Training the logistic regression model...")
    weights = train_logistic_regression(X_with_bias, y, learning_rate, epochs)
    print("Trained weights (including bias):", weights)
    
    print("Step 2: Making predictions...")
    predictions = predict(X_with_bias, weights)
    print("Sample Predictions:", predictions[:10])
    
    print("Step 3: Calculating Binary Cross-Entropy Loss...")
    probabilities = sigmoid(X_with_bias @ weights)
    loss = binary_cross_entropy(y, probabilities)
    print("Binary Cross-Entropy Loss:", loss)
    
    # Testing correctness
    print("\nTesting individual functions:")
    # Test sigmoid
    test_z = np.array([-2, 0, 2])
    print("Test Sigmoid (expected ~[0.12, 0.5, 0.88]):", sigmoid(test_z))
    
    # Test binary cross-entropy
    test_y_true = np.array([1, 0, 1])
    test_y_pred = np.array([0.9, 0.1, 0.8])
    print("Test BCE Loss (expected ~0.164):", binary_cross_entropy(test_y_true, test_y_pred))
    
    # Test gradient computation
    test_X = np.array([[1, 0.5], [1, -0.5], [1, 1.0]])
    test_y = np.array([1, 0, 1])
    test_weights = np.array([0, 0])
    print("Test Gradient (expected ~[-0.17, -0.33]):", compute_gradient(test_X, test_y, test_weights))


if __name__ == "__main__":
    main()
