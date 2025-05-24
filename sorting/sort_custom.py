"""Sort Custom
We can also specify a custom sorting order by using the key parameter in the .sort() method.
The key parameter doesn't accept a value, instead, it accepts a function that returns a value to be used for sorting.

def get_word_length(word: str) -> int:
    return len(word)

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]

words.sort(key=get_word_length)

print(words) # ['kiwi', 'pear', 'apple', 'banana', 'cherry', 'blueberry', 'watermelon']
In the example above, we defined a function get_word_length that returns the length of a word. 
We then passed this function as the key parameter to the .sort() method.
This means the words will be sorted based on their length, in ascending order, and not based on their lexicographical order.

Challenge
Implement the following functions:

sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted based on their length, in descending order.
sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted based on their absolute value, in ascending order. Hint: You may use the abs() function to get the absolute value of a number.
"""

from typing import List

"""
sort_words(words: List[str]) -> List[str] -
This function accepts a list of words and returns a new list of words sorted based on their length, in descending order.
Hint: words.sort(key=get_word_length)
"""
def get_word_length(word:str) -> int:
    return len(word)

def get_numbers_length(num:int) -> int:
    return abs(num)

def sort_words(words: List[str]) -> List[str]:
    # print("Custom sorted words: ", words)
    words.sort(key=get_word_length, reverse=True)  # This returns None
    return words
"""sort_numbers(numbers: List[int]) -> List[int] - 
This function accepts a list of numbers and returns a new list of numbers sorted based on their absolute value,
in ascending order. Hint: You may use the abs() function to get the absolute value of a number.

"""
def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=get_numbers_length, reverse=False)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
