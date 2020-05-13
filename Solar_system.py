class question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is the largest planet?\n(a) Saturn\n(b) Jupiter",
     "Which planet is the most simillar in size to earth?\n(a) Venus\n(b) Mars",
     "How many inner planets are in the solar system?\n(a) 5\n(b) 4",
     "How many planets are in the solar system?\n(a) 9\n(b) 8",
     "How many outer planets are in the solar system?\n(a) 4\n(b) 5",
     "Where is the asteroid belt?\n(a) between mars and jupiter\n(b) between jupiter and saturn",
     "Is pluto a planet?\n(a) no\n(b) yes",
     "Which was the first country to visit space?\n(a) Britain\n(b) America",
     "Where is NASA located?\n(a) America\n(b) Australia",
     "What planet is the smallest?\n(a) Mercury\n(b) Mars",     
]

question = [
     question(question_prompts[0], "b"),
     question(question_prompts[1], "a"),
     question(question_prompts[2], "b")
     question(question_prompts[3], "b")
     question(question_prompts[4], "a")
     question(question_prompts[5], "a")
     question(question_prompts[6], "a")
     question(question_prompts[7], "b")
     question(question_prompts[8], "a")
     question(question_prompts[9], "b")
]

def run_quiz(question):
     score = 0
     for questions in question:
          answer = input(questions)
          if answer == question.answer:
               score = score + 1
     print("you got", score, "out of", len(question))

run_quiz(question)