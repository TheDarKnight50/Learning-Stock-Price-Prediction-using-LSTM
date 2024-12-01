def is_prime(n):
    """
    Function to check if the given number is prime.
    Returns True if n is prime, otherwise False.
    """
    pass  # TODO: Implement this function

# Main function for evaluation
if __name__ == "__main__":
    # Test data and expected results
    test_cases = {
        2: True,
        3: True,
        4: False,
        17: True,
        20: False,
        29: True,
    }

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing is_prime
    print("Testing is_prime...")
    for number, expected in test_cases.items():
        try:
            result = is_prime(number)
            if result != expected:
                print(f"Test failed for is_prime({number}). Got: {result}, Expected: {expected}")
                all_tests_passed = False
        except Exception as e:
            print(f"Test for is_prime({number}) raised an exception: {e}")
            all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")
