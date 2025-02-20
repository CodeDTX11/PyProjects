#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# print(__file__)

with open("./Input/Names/invited_names.txt") as name_data:
    names_list = name_data.readlines()

# print(names_list)

PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter_data:
    start_letter = letter_data.read()

for name in names_list:
    name = name.strip()
    new_letter = start_letter.replace(PLACEHOLDER, name)
    with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as letter_file:
        letter_file.write(new_letter)



