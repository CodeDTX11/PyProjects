class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        user_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(user_answer, self.question_list[self.question_number].answer)

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("That's wrong.")

        self.question_number += 1
        print(f"The correct answer was: {c_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
