import matplotlib.pyplot as plt

def plot_pie_chart():
    """
    Function to:
    1. Create a pie chart to show the distribution of fruits in a basket:
       Apples: 30, Bananas: 20, Oranges: 50.
    2. Add labels to each section.
    """
    # Data for the pie chart
    sizes = [30, 20, 50]
    labels = ['Apples', 'Bananas', 'Oranges']

    # Plot the pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    
    # Add a title to the pie chart
    plt.title("Fruit Distribution in a Basket")

    # Display the plot
    plt.show()

# Main function for evaluation
if __name__ == "__main__":
    # Testing plot_pie_chart
    print("Testing plot_pie_chart...")
    all_tests_passed = True

    try:
        # Call the function to plot the pie chart
        plot_pie_chart()

        # Check if the plot appears correctly (manual validation required)
        print("Verify the generated pie chart visually.")

    except Exception as e:
        print(f"Test for plot_pie_chart raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
