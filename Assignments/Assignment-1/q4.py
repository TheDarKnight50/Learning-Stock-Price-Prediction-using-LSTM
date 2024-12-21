import numpy as np

def modify_array(arr):
    """
    Function to replace all odd numbers in the array with -1.
    Returns the modified array.
    """
    # Loop through the array and replace odd numbers with -1
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr[i] = -1

    return arr

# Main function for evaluation
if __name__ == "__main__":
    # Test data
    test_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    expected_result = np.array([-1, 2, -1, 4, -1, 6, -1, 8, -1, 10])

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing modify_array
    print("Testing modify_array...")
    try:
        result = modify_array(test_array)
        if not np.array_equal(result, expected_result):
            print(f"Test failed for modify_array. Got: {result}, Expected: {expected_result}")
            all_tests_passed = False
    except Exception as e:
        print(f"Test for modify_array raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")
