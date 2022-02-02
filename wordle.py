#!/usr/bin/env python3

# A wordle game for Abby


import random
import re
import os
import sys

# System call for ANSI codes in Windows
os.system("")

word_re = re.compile('^[a-z]{5}$', re.I)
GREEN = '\u001b[30m\u001b[1m\u001b[42;1m'
YELLOW = '\u001b[30m\u001b[1m\u001b[43;1m'
RESET = '\u001b[0m'

def get_word():
    with open("word_list.txt", "r") as file:
        allText = file.read()
        all_words = list(map(str, allText.split()))
        return random.choice(all_words)


def get_guess():
    while(True):
        guess = input("")
        if not re.match(word_re, guess):
            print("Error: Only 5 letter words are allowed.")
            continue
        sys.stdout.write("\033[F") #back to previous line 
        sys.stdout.write("\033[K") 
        return guess.lower()


def main():
    print("Welcome to Wordle for Abby.")
    count = 0
    word = get_word()
    while(count < 6):
        guess = get_guess()
        count +=1
        for i,c in enumerate(guess):
            if c == word[i]:
                print(GREEN + '{}'.format(c.upper()) + RESET, end='')
            elif c in word:
                print(YELLOW + '{}'.format(c.upper()) + RESET, end='')
            else:
                print('\u001b[1m{}'.format(c.upper()) + RESET, end='')
        print()
        if guess == word:
            print('Congrats!')
            break
        elif count >= 6:
            print(':(')
            print('The word was {}'.format(word.upper()))
            break


if __name__ == "__main__":
    main()