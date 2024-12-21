import pandas as pd
import matplotlib.pyplot as plt

def analyze_and_plot_student_data():
    """
    Function to:
    1. Create a DataFrame with student names, marks in Math, and marks in Science.
    2. Calculate the average marks for each student.
    3. Plot a bar chart showing the marks in Math and Science for each student.
    
    Returns:
    - DataFrame with student data including average marks.
    """
    # Test data for 20 students
    student_data = {
        "Name": [
            "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack",
            "Ken", "Lily", "Mike", "Nina", "Oscar", "Paul", "Quincy", "Rita", "Sam", "Tina"
        ],
        "Math": [
            85, 90, 78, 88, 92, 79, 84, 93, 81, 76, 
            95, 88, 84, 87, 90, 82, 91, 77, 85, 89
        ],
        "Science": [
            80, 89, 84, 91, 85, 92, 78, 88, 85, 81, 
            90, 87, 89, 91, 93, 86, 85, 88, 90, 84
        ]
    }

    # Note : this function works even without writing the above code, as the student_data is already defined in the global scope.

    # Create DataFrame from the test data
    student_df = pd.DataFrame(student_data)

    # Calculate average marks for each student
    student_df["Average"] = student_df[["Math", "Science"]].mean(axis=1)

    # Plot bar chart showing marks in Math and Science for each student
    student_df.plot(x="Name", y=["Math", "Science"], kind="bar", figsize=(12, 6))
    plt.title("Student Marks in Math and Science")
    plt.xlabel("Student Name")
    plt.ylabel("Marks")
    plt.show()

    return student_df

# Main function for evaluation
if __name__ == "__main__":
    # Test data for 20 students
    student_data = {
        "Name": [
            "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack",
            "Ken", "Lily", "Mike", "Nina", "Oscar", "Paul", "Quincy", "Rita", "Sam", "Tina"
        ],
        "Math": [
            85, 90, 78, 88, 92, 79, 84, 93, 81, 76, 
            95, 88, 84, 87, 90, 82, 91, 77, 85, 89
        ],
        "Science": [
            80, 89, 84, 91, 85, 92, 78, 88, 85, 81, 
            90, 87, 89, 91, 93, 86, 85, 88, 90, 84
        ]
    }

    # Create DataFrame from the test data
    test_df = pd.DataFrame(student_data)

    # Calculate average marks for each student
    test_df["Average"] = test_df[["Math", "Science"]].mean(axis=1)

    # Expected average marks
    expected_averages = test_df["Average"]

    # Testing analyze_and_plot_student_data
    print("Testing analyze_and_plot_student_data...")
    all_tests_passed = True

    try:
        # Call the function and get the resulting DataFrame
        result_df = analyze_and_plot_student_data()

        # Check if the resulting DataFrame matches the test data
        if not result_df["Average"].equals(expected_averages):
            print("Test failed: Average marks calculation is incorrect.")
            print(f"Expected averages:\n{expected_averages}")
            print(f"Got:\n{result_df['Average']}")
            all_tests_passed = False

        # Plot validation
        print("Verify the generated bar chart visually.")

    except Exception as e:
        print(f"Test for analyze_and_plot_student_data raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
