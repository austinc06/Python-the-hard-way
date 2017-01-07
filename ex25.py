def break_words(stuff):
    """This function will break up words for us."""
    #That's a documentation comment. It is output when help() is called for the function
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    #-1 is the reference for the last in the list
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


#can be imported with: import ex25
#Alternatively, import with: from ex25 import *
    #This imports everything from ex25 so it can be called directly without having to re-reference ex25
    #Eg ex25.break_words(sentence) vs break_words(sentence)
