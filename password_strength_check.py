# Requirements:
# Password Input:
# Allow the user to input a password.
# Validate its length (minimum 8 characters).
# Strength Criteria:
# Weak: Fails to meet at least one of these criteria.
# Moderate: Meets at least 3 criteria.
# Strong: Meets all criteria.
# Criteria for Password Strength:
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Contains at least one number.
# Contains at least one special character (e.g., !@#$%^&*).
# Is at least 12 characters long.
# Feedback: Provide specific suggestions to improve weak or moderate passwords.
# Edge Cases: Handle empty inputs or passwords with only whitespace.
import re
suggestions = {"upper":"Password must have at least one uppercase lettter",
               "lower":"Password must have atleast one lowercase letter", 
               "number":"Password must have at least one number",
               "special":"Password must have at least one special character (!@#$%^&*)", 
               "minchar":"Password should have minimum 8 characters"
               }



def length_check(password):
    if 0 <len(password) < 8:
        return False
    return True

def uppercase_check(password):
    if re.search('[A-Z]', password):
        return True
    return False

def lowercase_check(password):
    if re.search('[a-z]', password):
        return True
    return False

def number_check(password):
    if re.search('[0-9]', password):
        return True
    return False 

def special_char_check(password):
    if re.search('[\!\@\#\$\%\^\&\*]', password):
        return True
    return False

def get_password_strength(password):
    if not password:
        return "Enter a valid password"
    if not length_check(password):
        return suggestions["minchar"]
    msg = []
    if not uppercase_check(password):
        msg.append(suggestions["upper"])

    if not lowercase_check(password):
        msg.append(suggestions["lower"])

    if not number_check(password):
        msg.append(suggestions["number"])
    
    if not special_char_check(password):
        msg.append(suggestions["special"])

    if not msg:
        return "Strong!!!"
    if 0 <= len(msg) < 3:
        return "Weak;)", ";".join(msg)
    if  len(msg) in [3,4]:
        return "Moderate", ";".join(msg)

print(get_password_strength(input("Enter your password")))



def search_in_rotated_array(nums,key):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = (high - low) // 2
        if nums[mid] == key:
            return mid
        if nums[mid] > key and nums[low] > key:
            low = mid + 1
        if nums[mid] > key and nums[low] < key:
            high = mid - 1



# Day 1: Arrays
# Find the maximum subarray sum (Kadane's Algorithm).
# Reverse an array.
# Merge two sorted arrays.
# Search in a rotated sorted array.
# Find duplicates in an array.
# Find the first missing positive number.
# Move all zeroes to the end of an array.
# Find the intersection of two arrays.
# Find the subarray with the given sum.
# Rotate an array (left or right).
# Day 2: Strings
# Check if two strings are anagrams.
# Find the longest palindromic substring.
# Implement string matching algorithms (Naive, KMP).
# Reverse a string (iteratively and recursively).
# Check if a string is a palindrome.
# Find the longest common prefix of an array of strings.
# Implement strstr() (substring search).
# Count and find the most frequent character in a string.
# Convert a string to an integer (atoi).
# Check if a string contains all unique characters.
# Day 3: Linked Lists
# Reverse a linked list (iterative and recursive).
# Detect a cycle in a linked list (Floyd’s cycle-finding algorithm).
# Find the nth node from the end of a linked list.
# Merge two sorted linked lists.
# Find the middle element of a linked list.
# Remove the nth node from the end of a linked list.
# Flatten a linked list (with next and random pointers).
# Rotate a linked list by k places.
# Check if a linked list is a palindrome.
# Find the intersection point of two linked lists.
# Day 4: Stacks & Queues
# Implement a stack using arrays and linked lists.
# Implement a queue using stacks.
# Evaluate postfix expressions.
# Design a stack that retrieves the minimum element in constant time.
# Implement a circular queue.
# Check for balanced parentheses using a stack.
# Implement an undo mechanism using stacks.
# Design a priority queue (min-heap or max-heap).
# Implement a sliding window maximum using a deque.
# Implement a queue using two stacks.
# Day 5: Hashing
# Find the first non-repeating character in a string.
# Count frequencies of elements in an array.
# Two-sum problem (find two numbers that add up to a target).
# Group anagrams (using a hash map).
# Subarray sum with a given sum (using a hash map).
# Find the longest subarray with distinct elements.
# Find all pairs in an array that sum up to a given number.
# Find the intersection of two arrays using hashing.
# Find the longest consecutive sequence using a hash set.
# Find the duplicate number in an array (using hash map).
# Day 6: Recursion & Backtracking
# Solve the N-Queens problem using backtracking.
# Generate all permutations of a string/array.
# Subset sum problem.
# Solve the sudoku puzzle using backtracking.
# Generate all subsets of a set (power set).
# Find all combinations of numbers that sum up to a target.
# Solve the rat in a maze problem.
# Find all possible words from a given set of characters.
# Solve the 8-puzzle problem.
# Find all distinct permutations of a list of numbers.
# Day 7: Sorting Algorithms
# Implement quicksort.
# Implement mergesort.
# Find the kth smallest/largest element in an array.
# Sort an array of 0s, 1s, and 2s (Dutch National Flag problem).
# Sort an array of strings based on their lengths.
# Find the majority element (element that appears more than n/2 times).
# Sort a nearly sorted array (with a given k distance).
# Find the intersection of two sorted arrays.
# Sort an array of positive and negative numbers.
# Count the number of inversions in an array (merge sort approach).