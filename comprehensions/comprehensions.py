# https://www.reddit.com/r/learnpython/comments/4d2yl7/i_need_list_comprehension_exercises_to_drill/d1ndggs/

# Find all of the numbers from 1-1000 that are divisible by 7
li = [i for i in range(1, 1001) if i % 7 == 0]
print(li, '\n')

# Find all of the numbers from 1-1000 that have a 3 in them
li = [i for i in range(1, 1001) if '3' in str(i)]
print(li, '\n')

# Count the number of spaces in a string
string = "The quick brown fox jumps over the lazy dog"
count = len([char for char in string if char == ' '])
print(count, '\n')

# Remove all of the vowels in a string
vowels = ['a', 'e', 'i', 'o', 'u']
li = [char for char in string.lower() if char not in vowels]
print("".join(li), '\n')

# Find all of the words in a string that are less than 4 letters
words = string.split()
li = [word for word in words if len(word) < 4]
print(li, '\n')

# Challenge problems!

# Use a dictionary comprehension to count the length of each word in a sentence
word_lengths = {word: len(word) for word in words}
print(word_lengths, '\n')

# Use a nested list comprehension to find all of the numbers from 1-1000 that are divisible by any single digit besides 1 (2-9)
li = [num for num in range(1, 1001) if [div for div in range(2, 10) if num % div == 0]]
print(li, '\n')

# For all the numbers 1-1000, use a nested list/dictionary comprehension to find the highest single digit any of the numbers is divisible by
highest_div = {i: max([j for j in range(1, 10) if i % j == 0]) for i in range(1, 1001)}
print(highest_div, '\n')
