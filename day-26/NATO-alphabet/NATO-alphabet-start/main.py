# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# # Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# Loop through rows of a data frame
# for (index, row) in nato_data.iterrows():
#     # Access index and row
#     # Access row.student or row.score

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_data)

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
user_nato_words = [nato_dict[letter] for letter in user_input]

print(user_nato_words)
