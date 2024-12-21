import pandas as pd

def create_and_filter_dataframe(data):
    """
    Function to:
    1. Create a Pandas DataFrame with columns Name, Age, Marks.
    2. Add a new column Passed where Marks > 50.
    3. Filter and return rows where Passed is True.
    
    Parameters:
    - data: List of dictionaries with keys 'Name', 'Age', and 'Marks'.
    
    Returns:
    - Filtered DataFrame with rows where Passed is True.
    """
    # Create DataFrame from input data
    df = pd.DataFrame(data)
    
    # Add new column Passed where Marks > 50
    df['Passed'] = df['Marks'] > 50
    
    # Filter rows where Passed is True
    filtered_df = df[df['Passed']]
    
    return filtered_df

# Main function for evaluation
if __name__ == "__main__":
    # Test data
    input_data = [
        {'Name': 'Alice', 'Age': 20, 'Marks': 45},
        {'Name': 'Bob', 'Age': 22, 'Marks': 55},
        {'Name': 'Charlie', 'Age': 23, 'Marks': 65},
        {'Name': 'Diana', 'Age': 21, 'Marks': 49},
    ]
    
    # Expected result
    expected_data = [
        {'Name': 'Bob', 'Age': 22, 'Marks': 55, 'Passed': True},
        {'Name': 'Charlie', 'Age': 23, 'Marks': 65, 'Passed': True},
    ]
    expected_df = pd.DataFrame(expected_data)

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing create_and_filter_dataframe
    print("Testing create_and_filter_dataframe...")
    try:
        result_df = create_and_filter_dataframe(input_data)

        # Check if the result matches the expected DataFrame
        if not result_df.reset_index(drop=True).equals(expected_df):
            print(f"Test failed for create_and_filter_dataframe. Got:\n{result_df}\nExpected:\n{expected_df}")
            all_tests_passed = False

    except Exception as e:
        print(f"Test for create_and_filter_dataframe raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")
