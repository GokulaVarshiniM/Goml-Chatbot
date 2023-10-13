
class Chatbot:
    def __init__(self):
        self.questions = [
            "Hello there! Today, we're going to learn about the U.S. Government branches. Are you ready to get started?",
            "Great! Let's start with a basic overview. The federal government of the United States consists of three branches: the executive, legislative, and judicial branches.Can you explain what each branch does?",
            "That's correct! Now, tell me, how is the president elected in the United States?",
            "Good job! Now, let's move on to the legislative branch. What is it, and who does it consist of?",
            "Excellent! Lastly, tell me about the House of Representatives.",
        
        ]
        # self.answers = [
        #     "Great! Let's start with a basic overview. The federal government of the United States consists of three branches: the executive, legislative, and judicial branches.",
        #     "The executive branch is headed by the president, who enforces laws made by Congress.",
        #     "The president is elected by United States citizens through the electoral college system.",
        #     "The legislative branch, known as Congress, is composed of the Senate and the House of Representatives.",
        #     "The Senate has 100 senators, with each state represented by two Senators.",
        #     "The House of Representatives has 435 members, with the number of representatives per state determined by the population."
        # ]
        self.current_question = 0

    def ask_question(self,student_answer):
        if self.current_question == len(self.questions) - 1:
            return "You've done an impressive job explaining these concepts! This is a prime example of teaching by learning. By explaining the material to me, you're reinforcing your understanding of the topic. This interactive process can help students retain information effectively."
        # if self.current_question==0:
        #     self.current_question+=1
        #     return "Hello there! Today, we're going to learn about the U.S. Government branches. Are you ready to get started?"
        if self.check_answer(student_answer):
            self.current_question += 1
            return self.questions[self.current_question]
        else:
            return "Hmm, it seems like you didn't quite get it. Please try again."
        return self.questions[self.current_question]

    def check_answer(self, student_answer):
        keywords = [
            ["yes"],
            ["executive branch", "president", "enforces laws"],
            ["elected", "United States citizens", "electoral college"],
            ["legislative branch", "Congress", "Senate", "House of Representatives"],
            ["Senate", "100 senators", "two Senators"],
            ["House of Representatives", "435 members", "number of representatives", "population"]
        ]
        expected_keywords = keywords[self.current_question]

        for keyword in expected_keywords:
            if keyword.lower() not in student_answer.lower():
                return False

        return True

    # def respond(self, student_answer):
    #     if self.current_question == len(self.questions) - 1:
    #         return "You've done an impressive job explaining these concepts! This is a prime example of teaching by learning. By explaining the material to me, you're reinforcing your understanding of the topic. This interactive process can help students retain information effectively."
    #     if self.current_question==0:
    #         self.current_question+=1
    #         return "Hello there! Today, we're going to learn about the U.S. Government branches. Are you ready to get started?"
    #     if self.check_answer(student_answer):
    #         self.current_question += 1
    #         return self.questions[self.current_question]
    #     else:
    #         return "Hmm, it seems like you didn't quite get it. Please try again."

def main():
    chatbot = Chatbot()

    while chatbot.current_question < len(chatbot.questions):
        question = chatbot.ask_question()
        print(question)
        student_answer = input("> ")
        response = chatbot.respond(student_answer)
        print(response)


if __name__ == "__main__":
    main()
