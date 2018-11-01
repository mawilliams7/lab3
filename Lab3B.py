"""
CS 2302
Mark Williams
Lab 3 - Option B
Diego Aguirre/Manoj Saha
10-26-18
Purpose: Use binary search trees to quickly search for words in a 
         collection of all english words.
"""

from AVLNode import AVLNode 
from AVLTree import AVLTree 
from RBNode import RBNode 
from RBTree import RBTree
import time

english_words = None


def largest_anagram(filename):
  """
  Finds the words with the most anagrams in a file of words
  
  Args:
    filename: The name of the file of words
  
  Returns:
    largest: The word with the greatest number of anagrams

  """
  reader = open(filename, "r")
  lines = reader.readlines()
  largest = ""
  count = 0
  for line in lines:
    # Removes newline character from line
    if "\n" in line:
      line = line.replace("\n", "")
    temp = count_anagrams(line)
    if temp > count:
      count = temp
      largest = line
  return largest


def read_file_avl(filename):
  """
  Creates an avl binary search tree from a file of words
  
  Args:
    filename: The name of the file to be parsed
  
  Returns:
    tree: An AVL binary search tree

  """
  reader = open(filename, "r")
  lines = reader.readlines()
  tree = AVLTree()
  for line in lines:
    # Removes newline character from line
    if "\n" in line:
      line = line.replace("\n", "")
    node = AVLNode(line)
    tree.insert(node)
  return tree
  

def read_file_rb(filename):
  """
  Creates a red black binary search tree from a file of words
  
  Args:
    filename: The name of the file to be parsed
  
  Returns:
    tree: A red black binary search tree

  """
  reader = open(filename, "r")
  lines = reader.readlines()
  tree = RBTree()
  for line in lines:
    # Removes newline character from line
    if "\n" in line:
      line = line.replace("\n", "")
    tree.insert(line)
  return tree


def print_anagrams(word, prefix=""):
  """
  Prints all the anagrams a word has recursively.
  
  Args:
    word: The word to be analyzed
    prefix: A prefix made from word
  
  Returns:
    None

  """
  if len(word) <= 1:
    string = prefix + word
    if english_words.search(string):
      print(string)
  else:
    for i in range(len(word)):
      cur = word[i: i + 1]
      before = word[0: i] # letters before cur
      after = word[i + 1:] # letters after cur
      if cur not in before: # Check if permutations of cur have not been generated.
        print_anagrams(before + after, prefix + cur)


def count_anagrams(word, prefix=""):
  """
  Counts the number of anagrams a word has.
  
  Args:
    word: The word to be analyzed
    prefix: A prefix made from word
  
  Returns:
    counter: The number of anagrams a word has 

  """
  if len(word) <= 1:
    string = prefix + word
    if english_words.search(string):
      return 1
    return 0
  else:
    counter = 0
    for i in range(len(word)):
      cur = word[i: i + 1]
      before = word[0: i] # letters before cur
      after = word[i + 1:] # letters after cur
      if cur not in before: # Check if permutations of cur have not been generated.
        counter += count_anagrams(before + after, prefix + cur)
    return counter


def main():
  global english_words
  user_input = 0
  while user_input <= 0 or user_input >= 3:
    print("What type of BST do you want to use?")
    print("Enter 1 for AVL, 2 for Red Black.")
    user_input = int(input())
    if user_input == 1 or user_input == 2:
      break
    print("Not valid input. Please try again.")
  filename = "words.txt"
  if user_input == 1:
    english_words = read_file_avl(filename)
  else:
    english_words = read_file_rb(filename)
  print("Spot has " + str(count_anagrams("spot")) + " anagrams.")
  test = "test.txt"
  most = largest_anagram(test)
  print("In " + test + " the word with the most anagrams is " + 
        most + ". It has " + str(count_anagrams(most)) + " anagrams.")

main()
