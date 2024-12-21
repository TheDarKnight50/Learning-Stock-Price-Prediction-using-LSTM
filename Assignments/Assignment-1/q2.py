def reverse_string(s):
    """
    Function to reverse the given string.
    """
    return s[::-1]

def count_characters(s):
    """
    Function to count the number of characters in the given string.
    """
    return len(s)

# Main function for evaluation
if __name__ == "__main__":
    # Test data
    test_string = "Python"

    # Expected results
    expected_reversed = "nohtyP"
    expected_character_count = 6

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing reverse_string
    print("Testing reverse_string...")
    try:
        reversed_result = reverse_string(test_string)
        if reversed_result != expected_reversed:
            print(f"Test failed for reverse_string. Got: {reversed_result}, Expected: {expected_reversed}")
            all_tests_passed = False
    except Exception as e:
        print(f"Test for reverse_string raised an exception: {e}")
        all_tests_passed = False

    # Testing count_characters
    print("Testing count_characters...")
    try:
        character_count_result = count_characters(test_string)
        if character_count_result != expected_character_count:
            print(f"Test failed for count_characters. Got: {character_count_result}, Expected: {expected_character_count}")
            all_tests_passed = False
    except Exception as e:
        print(f"Test for count_characters raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")
