import pandas as pd

nato_data=pd.read_csv("nato_phonetic_alphabet.csv")




nato_dict={row.letter:row.code for (index,row) in nato_data.iterrows() }

name=input("Enter your Name: ")

nato_list=[nato_dict[letter.upper()] for letter in list(name)]

print(nato_list)