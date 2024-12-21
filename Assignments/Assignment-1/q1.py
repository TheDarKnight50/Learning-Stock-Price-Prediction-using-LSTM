def print_even_numbers(numbers):
    """
    Function to print all even numbers from the given list.
    """
    # evennums = []
    for num in numbers: 
        if(num % 2 == 0) : 
            print(num)

def sum_of_odd_numbers(numbers):
    """
    Function to return the sum of all odd numbers from the given list.
    """
    sum = 0
    for num in numbers:
        if num % 2 == 1 : 
            sum += num

    return sum

# Main function for evaluation
if __name__ == "__main__":
    # Test data
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Expected results
    expected_even_numbers = [2, 4, 6, 8, 10]
    expected_sum_of_odds = 25

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing print_even_numbers
    print("Testing print_even_numbers...")
    try:
        from io import StringIO
        import sys

        # Capture printed output
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()

        print_even_numbers(test_list)

        # Restore stdout
        sys.stdout = old_stdout

        # Extract printed even numbers as a list of integers
        printed_numbers = list(map(int, captured_output.getvalue().strip().split('\n')))

        if printed_numbers != expected_even_numbers:
            print(f"Test failed for print_even_numbers. Got: {printed_numbers}, Expected: {expected_even_numbers}")
            all_tests_passed = False

    except Exception as e:
        print(f"Test for print_even_numbers raised an exception: {e}")
        all_tests_passed = False

    # Testing sum_of_odd_numbers
    print("Testing sum_of_odd_numbers...")
    try:
        result = sum_of_odd_numbers(test_list)
        if result != expected_sum_of_odds:
            print(f"Test failed for sum_of_odd_numbers. Got: {result}, Expected: {expected_sum_of_odds}")
            all_tests_passed = False
    except Exception as e:
        print(f"Test for sum_of_odd_numbers raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")