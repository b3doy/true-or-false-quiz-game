class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    
    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        player_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?: ").lower()
        self.check_answer(player_answer, current_question.answer)
    
    def check_answer(self, player_answer, correct_answer):
        if player_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("Sorry, Your answer is wrong!")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your Score is: {self.score}/{self.question_number}")
        print("\n")