class BrainOfgame:
    def __init__(self,question_list:list) -> None:
        self.question_no=0
        self.question_list=question_list
        self.current_score=0

    def main_game_loop(self):
        '''The main game loop'''
        for i in range(len(self.question_list)):
            print(f"Q{self.question_no+1}: {self.question_list[i].text}")
            self.question_no+=1
            if self.question_list[i].answer==input('True/False: '):
                print('Your Win')
                self.score()
                print(f"Current Score: ",self.current_score,'/',len(self.question_list))

                continue
            else:
                print('Wrong Answer')
                print(f"Current Score: {self.current_score}/{len(self.question_list)}")
            
        if input("Continue(Yes/No): ")=='Yes':
            self.next_question()
        else:
            return
            
    def score(self):
        '''Increases the score each time user gets correct answer'''
        self.current_score+=1
        
            
        

        

        
    