import random
from flashcard import Flashcard

class FlashcardManager:
    def __init__(self):
        self.flashcards = {}

    def add_flashcard(self, question, answer):
        if question in self.flashcards:
            print(f"Flashcard with the question '{question}' already exists.")
        else:
            self.flashcards[question] = Flashcard(question, answer)
            print(f"Flashcard '{question}' added successfully.")

    def edit_flashcard(self, question, new_question, new_answer):
        if question in self.flashcards:
            self.flashcards[new_question] = Flashcard(new_question, new_answer)
            if new_question != question:
                del self.flashcards[question]
            print(f"Flashcard '{question}' updated successfully.")
        else:
            print(f"Flashcard with the question '{question}' not found.")

    def delete_flashcard(self, question):
        if question in self.flashcards:
            del self.flashcards[question]
            print(f"Flashcard '{question}' deleted successfully.")
        else:
            print(f"Flashcard with the question '{question}' not found.")

    def list_flashcards(self):
        if self.flashcards:
            print("Flashcards:")
            for flashcard in self.flashcards.values():
                print(flashcard.display_question())
        else:
            print("No flashcards available.")

    def review_flashcard(self):
        if self.flashcards:
            question = random.choice(list(self.flashcards.keys()))
            flashcard = self.flashcards[question]
            print(flashcard.display_question())
            input("Press Enter to show the answer...")
            print(flashcard.display_answer())
        else:
            print("No flashcards to review!")