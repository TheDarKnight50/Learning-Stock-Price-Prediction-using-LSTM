import matplotlib.pyplot as plt
import numpy as np

def plot_line_graph():
    """
    Function to:
    1. Plot a line graph for y = 2x + 1 for x ranging from -5 to 5.
    2. Label the X-axis and Y-axis.
    3. Add a title to the graph.
    """
    pass  # TODO: Implement this function

# Main function for evaluation
if __name__ == "__main__":
    # Testing plot_line_graph
    print("Testing plot_line_graph...")
    all_tests_passed = True

    try:
        # Call the function to plot the graph
        plot_line_graph()

        # Check if the plot appears correctly (manual validation required)
        print("Verify the generated plot visually.")

    except Exception as e:
        print(f"Test for plot_line_graph raised an exception: {e}")
        all_tests_passed = False

    # Final result
    if all_tests_passed:
        print("All test cases passed")
