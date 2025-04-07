
class Flashcard:
    def __init__(self, front, back):
        self.front = front
        self.back = back

class FlashcardManager:
    def __init__(self):
        self.deck = []

    def add_flashcard(self, front, back):
        self.deck.append(Flashcard(front, back))

    def list_flashcards(self):
        print("\nFlashcards:")
        for i, card in enumerate(self.deck):
            print(f"{i+1}. {card.front} - {card.back}")

class QuizEngine:
    def __init__(self, questions):
        self.questions = questions

    def start_quiz(self):
        print("\nStarting quiz:")
        score = 0
        for i, (q, a) in enumerate(self.questions):
            print(f"Q{i+1}: {q}")
            user_answer = input("Your answer: ").strip()
            if user_answer.lower() == a.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong. The correct answer was: {a}")
        print(f"Your score: {score}/{len(self.questions)}")

def main():
    print("Welcome to the English Learning App")

    manager = FlashcardManager()
    manager.add_flashcard("Break the ice", "To start a conversation in a social setting")
    manager.add_flashcard("Spill the beans", "To reveal a secret")
    manager.list_flashcards()

    sample_questions = [
        ("What does 'break the ice' mean?", "To start a conversation in a social setting"),
        ("What does 'spill the beans' mean?", "To reveal a secret"),
    ]
    quiz = QuizEngine(sample_questions)
    quiz.start_quiz()

if __name__ == "__main__":
    main()
