import string
import random

number_of_strings = 5
length_of_string = 8
for x in range(number_of_strings):
  print(''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))