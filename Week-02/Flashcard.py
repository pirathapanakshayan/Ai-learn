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

cards = [
    Flashcard("Haus", "house"),
    Flashcard("Hund","dog"),
    Flashcard("Buch", "book"),
    Flashcard("Wasser", "water"),
    Flashcard("Brot", "bread"),
]
for card in cards:
    card.ask()

total_correct =0
for card in cards:
    total_correct += card.correct

print(f"Correct: {card.correct}, Wrong: {card.wrong}")

