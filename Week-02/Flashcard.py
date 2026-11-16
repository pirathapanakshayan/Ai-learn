class Flashcard:
    def __init__(self,german,english):
        self.german = german
        self.english = english
        self.correct = 0
        self.wrong = 0

    def ask(self):
        answer = input(f"what does'{self.german}' mean?")
        if answer.lower().strip() == self.english:
            self.correct += 1
            print("correct")

        else:
            self.wrong += 1
            print(f"wrong. It means '{self.english}'")

card = Flashcard("Haus", "house")
card.ask()
card.ask()

print(f"Correct: {card.correct}, Wrong: {card.wrong}")