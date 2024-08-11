#!/usr/bin/python3
"""
Pascal's Triangle - Combined Approach
"""

def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal’s triangle of n."""
    if n <= 0:
        return []

    res = [[1]]  # Start with the first row

    for i in range(1, n):
        prev_row = res[-1]  # Get the last row added to the result list
        curr_row = [1]  # Start the current row with a 1

        # Fill in the middle values of the row
        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])

        curr_row.append(1)  # End the row with a 1
        res.append(curr_row)  # Add the current row to the result list

    return res  # Return the full Pascal's Triangle

# Example usage:
print(pascal_triangle(5))

