import pandas as pd

def process_csv(file_path):
    """
    Function to:
    1. Load a CSV file with columns City, Temperature, Rainfall.
    2. Filter and return rows where Temperature > 30.
    3. Calculate and return the average Rainfall.
    
    Parameters:
    - file_path: Path to the CSV file.
    
    Returns:
    - A tuple: (filtered DataFrame, average Rainfall)
    """
    pass  # TODO: Implement this function

# Main function for evaluation
if __name__ == "__main__":
    # Sample CSV data for testing (20 cities)
    csv_data = """City,Temperature,Rainfall
CityA,25,12.5
CityB,35,15.0
CityC,40,10.0
CityD,20,8.0
CityE,31,18.0
CityF,28,5.0
CityG,45,22.0
CityH,30,13.0
CityI,50,20.0
CityJ,15,9.0
CityK,32,14.0
CityL,38,19.0
CityM,26,6.0
CityN,29,7.5
CityO,41,11.0
CityP,33,12.0
CityQ,42,16.0
CityR,27,10.5
CityS,36,8.0
CityT,25,9.0
    """
    
    # Write the sample data to a test CSV file
    test_csv_path = "test_data_20_cities.csv"
    with open(test_csv_path, "w") as f:
        f.write(csv_data)

    # Expected filtered DataFrame (Temperature > 30)
    expected_filtered_data = [
        {'City': 'CityB', 'Temperature': 35, 'Rainfall': 15.0},
        {'City': 'CityC', 'Temperature': 40, 'Rainfall': 10.0},
        {'City': 'CityE', 'Temperature': 31, 'Rainfall': 18.0},
        {'City': 'CityG', 'Temperature': 45, 'Rainfall': 22.0},
        {'City': 'CityI', 'Temperature': 50, 'Rainfall': 20.0},
        {'City': 'CityK', 'Temperature': 32, 'Rainfall': 14.0},
        {'City': 'CityL', 'Temperature': 38, 'Rainfall': 19.0},
        {'City': 'CityO', 'Temperature': 41, 'Rainfall': 11.0},
        {'City': 'CityP', 'Temperature': 33, 'Rainfall': 12.0},
        {'City': 'CityQ', 'Temperature': 42, 'Rainfall': 16.0},
        {'City': 'CityS', 'Temperature': 36, 'Rainfall': 8.0},
    ]
    expected_filtered_df = pd.DataFrame(expected_filtered_data)

    # Expected average Rainfall
    expected_avg_rainfall = expected_filtered_df['Rainfall'].mean()

    # Flag to track if all tests pass
    all_tests_passed = True

    # Testing process_csv
    print("Testing process_csv...")
    try:
        filtered_df, avg_rainfall = process_csv(test_csv_path)

        # Check if the filtered DataFrame matches
        if not filtered_df.reset_index(drop=True).equals(expected_filtered_df):
            print(f"Test failed for filtered DataFrame. Got:\n{filtered_df}\nExpected:\n{expected_filtered_df}")
            all_tests_passed = False

        # Check if the average Rainfall matches
        if not abs(avg_rainfall - expected_avg_rainfall) < 1e-6:  # Allowing for minor floating-point differences
            print(f"Test failed for average Rainfall. Got: {avg_rainfall}, Expected: {expected_avg_rainfall}")
            all_tests_passed = False

    except Exception as e:
        print(f"Test for process_csv raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
    else:
        print("Some test cases failed")
