import pickle
from build_gui import *
from model import anagram as a


def check_is_word(user_input):
    '''This evaluates a word, to see if it's English.
    :param user_input: is the word we're evaluating.'''
    is_english_word = False
    try:
        with open("source/words_alpha.txt", "r") as words_file:
            for line in words_file.readlines():
                if user_input == line.strip().lower():
                    is_english_word = True
            return is_english_word
    except FileNotFoundError:
        display_message("File not found")
    except IOError:
        display_message("File corrupt.")
    finally:
        words_file.close()


def evaluate_input(user_input):
    '''This takes user input string, removes any white spaces, and converts to lower case.'''
    word_string = user_input.strip().lower()
    try:
        anagram_object = a.Anagram(word_string)
    except ValueError:
        display_message("Invalid Characters!")
        print("Invalid Characters!")
    else:
        if not check_is_word(word_string):
            display_message("Not an English word.")
        else:
            search_for_anagram(anagram_object.get_sorted_anagram())


def format_input(word_string):
    '''This takes a sting of letters, removes any whitespace and puts the letters in
    alphabetical order.
    :param word_string: is the provided string of letters
    :returns alphabetically ordered string.'''
    word_lower = word_string.strip().lower()
    alphabetized_letters = sorted(list(word_lower))
    return "".join(alphabetized_letters)


def search_for_anagram(sorted_anagram):
    '''This opens a file and loads into a dictionary. It also searches the dictionary for a matching anagram.'''
    try:
        with open('source/anagramdict.obj', 'rb') as search_file:
            working_dict = pickle.load(search_file)
            search_file.close()
            words_list = working_dict.get(sorted_anagram)
            if len(words_list) == 1:
                display_message("This word has \nno anagrams.")
            else:
                display_results_gui(words_list)
    except FileNotFoundError:
        display_message("File Not Found!")
    except IOError:
        display_message("File corrupt.")
    finally:
        search_file.close()


def create_dictionary_file():
    """This is for use one time only, to create the dictionary file that
    this program will use."""
    master_file = open("source/words_alpha.txt", "r")
    anagram_dictionary = {}

    for line in master_file.readlines():
        alphabetized_letters = format_input(line)
        word_input = line.strip().lower()
        if alphabetized_letters in anagram_dictionary:
            anagram_dictionary[alphabetized_letters].append(word_input)
        else:
            anagram_dictionary[alphabetized_letters] = [word_input]

    dictionary_file = open('/Users/grego/git/Python/PythonasaurusRex/FinalProject/source/anagramdict.obj', 'wb')
    pickle.dump(anagram_dictionary, dictionary_file)
    dictionary_file.close()


if __name__ == '__main__':
     create_tables(db_name)
     create_anagrams_database()
     print(select_all_anagrams(create_connection(db_name)))
     print(find_specified_anagrams('arw'))
     search_for_anagram('thpnoy')
    print(check_is_word("python"))