# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes a string of numbers
# and updates the dictionary to show which multiple of three occurs
# the most. That multiple is returned.

def count_threes(n):
  # YOUR CODE HERE
  n = list(n)
  three_count = dict([
    (3,0),
    (6,0),
    (9,0)
  ])

  for i in range(len(n)):
    if(int(n[i]) == 0):
      print()
    elif(int(n[i]) % 9 == 0):
      three_count[9] += 1
    elif(int(n[i]) % 6 == 0):
      three_count[6] += 1
    elif(int(n[i]) % 3 == 0):
      three_count[3] += 1
  max_val = -1
  ind = -1
  for key, value in three_count.items():
    if max_val < value:
      max_val = value
      ind = key
  return ind


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  chars = dict([])
  letter = ''
  count = 0
  for i in range(0, len(s)-1):
    if(s[i] == s[i+1]):
      count += 1
      letter = s[i]
      chars.update({letter:count})
    else:
      count = 0

  ch_arr = []
  all_values = chars.values()
  max_val = max(all_values)
  for key, value in chars.items():
    if max_val == value:
      ch_arr.append(key)
  return ch_arr
  print(chars.items())
  print(ch_arr)


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  str = s.lower().replace(" ", "")
  back_str = '';
  for i in reversed(str):
    back_str += i
  return back_str == str
