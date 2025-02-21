student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    # print(key)
    # print(value)
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # print(row.student + " " + row.score)
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

FILE = "nato_phonetic_alphabet.csv"
df_nato_alpha = pandas.read_csv(FILE) #df -> dataframe

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

dict_nato_alpha = {row.letter:row.code for (index, row) in df_nato_alpha.iterrows()}
print(dict_nato_alpha)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

u_input = input("Enter word to convert to NATO alphabet: ").upper()

output_list = [dict_nato_alpha[char] for char in u_input]

print(output_list)
