"""
Imagine that you have a massive database, and you're tracking millions of unique data entries. 
If you need to frequently check whether certain items exist in your dataset, comparing the 
performance of lists versus hash sets could play an instrumental role in your memory management process.

We've prepared a starter code for a Python function, but part of it is missing. 
Could you complete the code? Your task is to check the existence of a test element in both a list 
and a set 100 times, then print the time it took to process each case.
"""

# Importing the necessary libraries
import time

# Define a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
  
    # Create a list and a set
    data_list = [] # O(N) time complexity 
    data_set = set() # O(1) time complexity

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list

    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_set` and print the result and time taken
    # loop over data_set 100 times using a for loop & range(100)
    start_time = time.time()
    for _ in range(100):
         result_set = test_item in data_set
    end_time = time.time()
    print("Hash Set Test Result 1:", result_set)
    print("Hash Set search time (100): ", end_time - start_time, "seconds.")

    # TODO: Time the 100 consecutive operations of checking whether `test_item` is in `data_list` and print the result and time taken
    start_time = time.time()
    for _ in range(100):
         result_list = test_item in data_list
    end_time = time.time()
    print("Hash Set Test Result 2:", result_list)
    print("Hash Set search time (100): ", end_time - start_time, "seconds.")

# Execute the function
compare_operations()