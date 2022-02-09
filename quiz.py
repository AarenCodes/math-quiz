import datetime
import random

#Custom import
from questions import Add, Multiply

class Quiz:
    questions = []
    answers = []
    
    def __init__(self):
        question_types = (Add, Multiply)
        # generate 10 random questions with numbers 1-10
        for _ in range(10):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = random.choice(question_types)(num1, num2)
            # add these questions into self.questions
            self.questions.append(question)
        
    def take_quiz(self):
        #log start time
        self.start_time = datetime.datetime.now()
        
        #ask all questions
        for question in self.questions:
            #log if question = right
            self.answers.append(self.ask(question))
        else:
            #log end time
            self.end_time = datetime.datetime.now()
        
        #show a summary
        return self.summary()
        
    def ask(self, question):
        correct = False
        #log start time
        question_start = datetime.datetime.now()
        
        #capture answer
        answer = input(question.text + ' = ')
        
        #check answer
        if answer == str(question.answer):
            correct = True
            
        #log end time
        question_end = datetime.datetime.now()
        
        #if answer = right = true
        #if answer = wrong = false
        #send back elapsed time
        return correct, question_end - question_start
        
        
    def total_correct(self):
        #return total # of correct numbers
        total = 0
        for answer in self.answers:
            if answer[0]:
                total +=1
        return total
        
        
    def summary(self):
        #print how many you got right and the total # of questions
        print("You got {} out of {} correct.".format
              (self.total_correct(), len(self.questions)
        ))
        #print total time for quiz
        print("It took you {} seconds total.".format(
              (self.end_time-self.start_time).seconds
             ))

Quiz().take_quiz()