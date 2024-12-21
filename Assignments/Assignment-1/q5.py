import numpy as np

def matrix_operations(A, B):
    """
    Function to perform matrix operations on two 2x2 matrices A and B:
    1. Computes (A + B).
    2. Computes (A × B) (matrix multiplication).
    3. Returns the transpose of (A).
    
    Returns a tuple: (sum_matrix, product_matrix, transpose_A)
    """
    # Matrix addition
    sum_matrix = A + B

    # Matrix multiplication
    product_matrix = np.dot(A, B)

    # Transpose of A
    transpose_A = np.transpose(A)

    return sum_matrix, product_matrix, transpose_A

# Main function for evaluation
if __name__ == "__main__":
    # Test data
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    # Expected results
    expected_sum = np.array([[6, 8], [10, 12]])
    expected_product = np.array([[19, 22], [43, 50]])
    expected_transpose_A = np.array([[1, 3], [2, 4]])

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing matrix_operations
    print("Testing matrix_operations...")
    try:
        sum_matrix, product_matrix, transpose_A = matrix_operations(A, B)

        # Check each operation's result
        if not np.array_equal(sum_matrix, expected_sum):
            print(f"Test failed for matrix addition. Got: {sum_matrix}, Expected: {expected_sum}")
            all_tests_passed = False

        if not np.array_equal(product_matrix, expected_product):
            print(f"Test failed for matrix multiplication. Got: {product_matrix}, Expected: {expected_product}")
            all_tests_passed = False

        if not np.array_equal(transpose_A, expected_transpose_A):
            print(f"Test failed for matrix transpose. Got: {transpose_A}, Expected: {expected_transpose_A}")
            all_tests_passed = False

    except Exception as e:
        print(f"Test for matrix_operations raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")
