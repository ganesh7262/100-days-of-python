path=r"C:\Users\GANESH\Desktop\my_text.txt"



with open(path) as text:
    content=text.read()
    print(content)


with open("game_data.txt") as t:
    print(t.read())