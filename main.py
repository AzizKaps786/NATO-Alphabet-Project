import pandas as pd

words = input("Enter a word: ").upper()
df = pd.read_csv('nato_phonetic_alphabet.csv')
dict = {value.letter:value.code for (key, value) in df.iterrows()}
Nato_alphabets = [dict[letter] for letter in words if letter in dict]
print(Nato_alphabets)



