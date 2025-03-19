# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter.replace("[name]", f"{stripped_name}")
        with open(f"./Output/ReadyToSend/letters_{stripped_name}.txt", mode="w") as written_file:
            written_file.writelines(new_letter)
