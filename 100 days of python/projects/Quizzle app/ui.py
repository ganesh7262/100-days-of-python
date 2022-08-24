from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizIntface:
    
    
    def __init__(self,quiz_brain:QuizBrain) -> None:
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quzzler')
        self.window.resizable(0,0)
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        
        
        self.score_title=Label(text='Score: 0',padx=20,bg=THEME_COLOR,fg='white',font=12)
        self.score_title.grid(row=0,column=1)
        
        
        
        self.canvas=Canvas(height=250,width=300,background='white')
        self.question_text=self.canvas.create_text(150,125,text='Some Question here...',fill=THEME_COLOR,font=('Arial',12,'italic'),width=250)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=(30,10))
        
        
        
        
        self.true_img=PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\Quizzle app\images\true.png')
        self.false_img=PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\100-days-of-python\100 days of python\projects\Quizzle app\images\false.png')
        
        self.true_button=Button(image=self.true_img,highlightthickness=0,command=self.true_button_methood)
        self.true_button.grid(row=2,column=0,pady=(20,10))
        self.false_button=Button(image=self.false_img,highlightthickness=0,command=self.flase_button_methood)
        self.false_button.grid(row=2,column=1,pady=(20,10))
        
        self.get_next_question()
        
        
        
        
        self.window.mainloop()
        
    
    
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_title.config(text=f'Score: {self.quiz.score}')
            quest=self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=quest)
            self.canvas.configure(bg='white')
        else:
            self.canvas.itemconfig(self.question_text,text=f'You have reached the end of quiz\nFinal Score:{self.quiz.score}')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')
    
    def true_button_methood(self):
        self.give_feedback(self.quiz.check_answer('True'))
            
            
    
    def flase_button_methood(self):
        self.give_feedback(self.quiz.check_answer('False'))
            
    
    def give_feedback(self,is_right):
        if is_right==True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000,self.get_next_question)