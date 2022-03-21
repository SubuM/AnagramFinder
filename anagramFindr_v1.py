
from itertools import permutations,combinations
import enchant

d = enchant.Dict('en_US')
word = input('Enter word: ')
letters = [chr for chr in word]
repeat_check = []

for number in range(3,len(letters)+1): #For Loop
    for current_set in combinations(letters,number): #Combinations Function
        #Code for the Basic Anagram Finder
        for current in permutations(current_set):
            current_word = ''.join(current)
            if d.check(current_word)and current_word not in repeat_check:
                print(current_word)
                repeat_check.append(current_word)
