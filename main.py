from flashcard_manager import FlashcardManager


def main():
    manager = FlashcardManager()
    while True:
        print("\nMenu:")
        print("1. Add Flashcard")
        print("2. Edit Flashcard")
        print("3. Delete Flashcard")
        print("4. List Flashcards")
        print("5. Review Flashcard")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            question = input("Enter the question: ")
            answer = input("Enter the answer: ")
            manager.add_flashcard(question, answer)

        elif choice == "2":
            question = input("Enter the current question: ")
            new_question = input("Enter the new question: ")
            new_answer = input("Enter the new answer: ")
            manager.edit_flashcard(question, new_question, new_answer)

        elif choice == "3":
            question = input("Enter the question to delete: ")
            manager.delete_flashcard(question)

        elif choice == "4":
            manager.list_flashcards()

        elif choice == "5":
            manager.review_flashcard()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()