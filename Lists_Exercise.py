# Create a list named fruits with the elements "apple", "banana", "cherry", and "orange".
fruits = ["apple", "banana", "cherry", "orange"]
# Create another list named vegetables with "carrot", "potato", "cucumber".
vegetables = ["carrot", "potato", "cucumber"]
# Combine fruits and vegetables into a new list named grocery.
grocery = fruits + vegetables
# Print the grocery list.
print(grocery)

# Part 2. 

# Print the first three elements of the grocery list using slicing
print(grocery[0:3])

# Print the last two items from the grocery list in reverse order.
print(grocery[-1:-3:-1])

# Part 3.

# Create a nested list named matrix with two lists inside it: [1, 2, 3] and [4, 5, 6].
matrix = [[1, 2, 3], [4, 5, 6]]

# Access and print the second element of the first nested list.
print(matrix[0][1])

# Part 4.

# Using list comprehension, create a new list named squared_numbers containing the squares of numbers from 1 to 10.
squared_numbers = [x**2 for x in range(1, 11)]

# Print the squared_numbers list.
print(squared_numbers)

# Part 5.

# Add "kiwi" to the fruits list.
fruits.append("kiwi")

# Remove "potato" from the vegetables list.
vegetables.remove("potato")

# Insert "spinach" at the second position in the vegetables list.
vegetables.insert(1, "spinach")

# Print the updated fruits and vegetables lists.
print(fruits)

# Part 6.

# Sort the grocery list alphabetically and print it.
grocery.sort()
print(grocery)

# Reverse the order of the grocery list and print it.
grocery.reverse()
print(grocery)

# Part 7.

# Use a loop to print each item in the grocery list alongside its index in the format: "Index: [index], Item: [item]".
for i in grocery:
    print("Index: " + str(grocery.index(i)) + ", Item: " + i)

# Part 8.
    
# Create a function filter_short_words that takes a list of words and an integer n as arguments and returns a new list containing only the words that are longer than n characters.
def filter_short_words(words, n):
    for w in words:
        if len(w) > n:
            print(w)

# Call the filter_short_words function with the list of words and the number 5 as arguments.
filter_short_words(grocery, 4)










