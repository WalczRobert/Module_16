from gui_functions import *

master_file = open("source/words_alpha.txt", "r")
anagram_dictionary = {}
print(master_file.read())

for line in master_file.readlines():
     alphabetized_letters = format_input(line)
     word_input = line.strip().lower()
     # print(f'{line.strip()}: {alphabetized_letters} - {len(line.strip())}')

     if alphabetized_letters in anagram_dictionary:
         anagram_dictionary[alphabetized_letters].append(word_input)
     else:
         anagram_dictionary[alphabetized_letters] = [word_input]
