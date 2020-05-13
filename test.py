class question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What color are apples?\n(a) Red/Green\n(b)Orange",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow",
]

questions = [
     question(question_prompts[0], "a"),
     question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(questions)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)