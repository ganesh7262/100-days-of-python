from random import choice
import tkinter
import string

FONT=("Ariel",10,"bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    
    set_of_char=string.ascii_letters + string.digits
    global rand_pass
    rand_pass=''.join([choice(set_of_char) for i in range(9)])
    password_inp.insert(0,rand_pass)

    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_values():
    return website_inp.get(),email_username_inp.get(),rand_pass

def add():
    with open(r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\Pass_data.txt','a') as pass_data:
        web,email_u,pas=get_values()
        pass_data.write(f'\n{web} | {email_u} | {pas}')
        website_inp.delete(0,tkinter.END)
        password_inp.delete(0,tkinter.END)
        

# ---------------------------- UI SETUP ------------------------------- #

window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=100,pady=100)

logo_img=tkinter.PhotoImage(file=r"C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\my_pass(password manager)\logo.png")
canvas=tkinter.Canvas(width=200,height=200)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=tkinter.Label(text="Website: ",font=FONT)
website_label.grid(row=1,column=0)

website_inp=tkinter.Entry(width=40)
website_inp.grid(row=1,column=1,columnspan=2)
website_label.config(pady=5)
website_inp.focus()

email_username_label=tkinter.Label(text="Email/Username: ", font=FONT)
email_username_label.grid(row=3,column=0,pady=5)

email_username_inp=tkinter.Entry(width=40)
email_username_inp.insert(0,"ganeshshinde@gmail.com")
email_username_inp.grid(row=3,column=1,columnspan=2)

password_label=tkinter.Label(text="Password: ",font=FONT)
password_label.grid(row=4,column=0,pady=5)

password_inp=tkinter.Entry(width=25)
password_inp.grid(row=4,column=1)


generate_button=tkinter.Button(text="Generate",command=password_gen)
generate_button.grid(row=4,column=2)

add_button=tkinter.Button(text='Add',width=35,command=add)
add_button.grid(row=5,column=1,columnspan=2)

window.mainloop()