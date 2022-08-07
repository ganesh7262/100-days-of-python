import pandas as pd

nato_data=pd.read_csv("nato_phonetic_alphabet.csv")




nato_dict={row.letter:row.code for (index,row) in nato_data.iterrows() }

def create_nato():
    name=input("Enter a Word: ")
    nato_list=[nato_dict[letter.upper()] for letter in list(name)]
    print(nato_list)


try:
    create_nato()
    
except KeyError as err:
    print('Sorry only letters from alphabets accepted')
    create_nato()
    