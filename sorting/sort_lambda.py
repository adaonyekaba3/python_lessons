"""
Sort Lambda
Defining a separate function just to pass it into the key parameter of the .sort() method can be cumbersome. 
We can use a lambda function to define a function in a single line and pass it directly to the .sort() method.

To sort a list of words by their length, we can use a lambda function like this:

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]

words.sort(key=lambda word: len(word))

print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']
The lambda function lambda word: len(word) is equivalent to the function get_word_length we defined in the previous example.
It takes a word as input and returns the length of the word.

The syntax includes:

The keyword lambda.
The input variable word. We can use any variable name here.
The colon :, after which we define the function body.
The expression len(word), which is the return value of the function.
A lambda function must be a single expression, and it cannot contain multiple statements.
It's a convenient way to define simple functions without the need to define a separate function.

Challenge
Implement the following functions:

sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted based on their length,
in descending order. Use a lambda function to sort the words by their length.
sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers
sorted based on their absolute value, in ascending order. Use a lambda function to sort the numbers by their absolute value.
"""
from typing import List

"""sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted
based on their length, in descending order. Use a lambda function to sort the words by their length.
Hint: words.sort(key=lambda word: len(word))
"""
def sort_words(words: List[str]) -> List[str]:
    # print("Sorted list of words based on length: ", words)
    words.sort(key=lambda word: len(word), reverse=True)
    return words

"""sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers
sorted based on their absolute value, in ascending order. Use a lambda function to sort the numbers by their absolute value.
"""
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=lambda number: abs(number), reverse=False)
    return numbers

# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))