import random
import time


class FunQuizGame:
    def __init__(self):
        # Nested list containing quiz questions, options, and correct answers
        self.quiz_data = [
            {
                'question': 'What is the capital of France?',
                'options': ['London', 'Berlin', 'Paris', 'Madrid'],
                'correct': 2,
                'category': 'Geography'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Venus', 'Mars', 'Jupiter', 'Saturn'],
                'correct': 1,
                'category': 'Science'
            },
            {
                'question': 'What is 7 × 8?',
                'options': ['54', '56', '58', '60'],
                'correct': 1,
                'category': 'Math'
            },
            {
                'question': 'Who painted the Mona Lisa?',
                'options': ['Van Gogh', 'Picasso', 'Da Vinci', 'Michelangelo'],
                'correct': 2,
                'category': 'Art'
            },
            {
                'question': 'What is the largest mammal?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippo'],
                'correct': 1,
                'category': 'Science'
            },
            {
                'question': 'Which language uses "print" for output?',
                'options': ['Java', 'Python', 'C++', 'JavaScript'],
                'correct': 1,
                'category': 'Programming'
            },
            {
                'question': 'What is the square root of 64?',
                'options': ['6', '7', '8', '9'],
                'correct': 2,
                'category': 'Math'
            },
            {
                'question': 'Which element has the chemical symbol "O"?',
                'options': ['Gold', 'Oxygen', 'Osmium', 'Oganesson'],
                'correct': 1,
                'category': 'Science'
            }
        ]

        self.score = 0
        self.total_questions = 0
        self.used_questions = set()
        self.categories = self.get_unique_categories()

    def get_unique_categories(self):
        """Extract unique categories from quiz data"""
        categories = []
        for question in self.quiz_data:
            if question['category'] not in categories:
                categories.append(question['category'])
        return categories

    def shuffle_options(self, options, correct_index):
        """Shuffle options while keeping track of correct answer"""
        indexed_options = list(enumerate(options))
        random.shuffle(indexed_options)

        new_options = [opt for _, opt in indexed_options]
        new_correct = next(i for i, (orig_idx, _) in enumerate(indexed_options)
                           if orig_idx == correct_index)

        return new_options, new_correct

    def display_welcome(self):
        """Display welcome message and instructions"""
        print("🎯" * 30)
        print("🌟 WELCOME TO THE ULTIMATE FUN QUIZ GAME! 🌟")
        print("🎯" * 30)
        print("\nRules:")
        print("- Answer questions from various categories")
        print("- Each correct answer gives you 1 point")
        print("- You can choose to play specific categories")
        print("- Type 'quit' at any time to end the game")
        print("\n" + "=" * 50)

    def select_category(self):
        """Let user select a category or choose random"""
        print("\nAvailable Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")

        print(f"{len(self.categories) + 1}. Random Mix")

        while True:
            try:
                choice = input(f"\nChoose a category (1-{len(self.categories) + 1}): ").strip()
                if choice.lower() == 'quit':
                    return None

                choice = int(choice)
                if 1 <= choice <= len(self.categories):
                    return self.categories[choice - 1]
                elif choice == len(self.categories) + 1:
                    return 'Random'
                else:
                    print("Invalid choice! Please try again.")
            except ValueError:
                print("Please enter a valid number!")

    def get_questions_by_category(self, category):
        """Filter questions by selected category"""
        if category == 'Random':
            return [q for q in self.quiz_data]
        return [q for q in self.quiz_data if q['category'] == category]

    def ask_question(self, question_data):
        """Ask a single question and get user's answer"""
        print(f"\n{'=' * 60}")
        print(f"Category: {question_data['category']}")
        print(f"Question: {question_data['question']}")
        print('-' * 40)

        # Shuffle options for variety
        shuffled_options, correct_index = self.shuffle_options(
            question_data['options'], question_data['correct']
        )

        # Display options
        for i, option in enumerate(shuffled_options, 1):
            print(f"{i}. {option}")

        # Get user input
        while True:
            answer = input("\nYour answer (1-4): ").strip().lower()

            if answer == 'quit':
                return None

            try:
                answer_num = int(answer)
                if 1 <= answer_num <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4!")
            except ValueError:
                print("Please enter a valid number!")

        # Check if answer is correct
        is_correct = (answer_num - 1) == correct_index

        if is_correct:
            print("✅ CORRECT! Well done! 🎉")
            return True
        else:
            correct_answer = shuffled_options[correct_index]
            print(f"❌ WRONG! The correct answer was: {correct_answer}")
            return False

    def show_progress(self):
        """Show current progress and score"""
        print(f"\n📊 Progress: {self.score}/{self.total_questions} correct")
        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0
        print(f"📈 Score: {percentage:.1f}%")

    def show_final_results(self):
        """Display final results"""
        print("\n" + "🌟" * 25)
        print("🎮 QUIZ COMPLETE! 🎮")
        print("🌟" * 25)

        percentage = (self.score / self.total_questions * 100) if self.total_questions > 0 else 0

        print(f"\n📊 Final Score: {self.score}/{self.total_questions}")
        print(f"📈 Percentage: {percentage:.1f}%")

        if percentage >= 80:
            print("🎯 EXCELLENT! You're a quiz master! 🌟")
        elif percentage >= 60:
            print("👍 GOOD JOB! Well played! 🏆")
        elif percentage >= 40:
            print("😊 NOT BAD! Keep practicing! 💪")
        else:
            print("📚 Keep learning! You'll do better next time! 🌱")

    def play_again(self):
        """Ask if user wants to play again"""
        while True:
            choice = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if choice in ['yes', 'y']:
                return True
            elif choice in ['no', 'n', 'quit']:
                return False
            else:
                print("Please enter 'yes' or 'no'!")

    def run(self):
        """Main game loop"""
        self.display_welcome()

        while True:
            # Reset game state
            self.score = 0
            self.total_questions = 0
            self.used_questions = set()

            # Select category
            category = self.select_category()
            if category is None:
                break

            # Get questions for selected category
            available_questions = self.get_questions_by_category(category)

            if not available_questions:
                print("No questions available for this category!")
                continue

            # Shuffle questions for randomness
            random.shuffle(available_questions)

            print(f"\nStarting {category} quiz! Get ready...")
            time.sleep(1)

            # Ask questions
            for question in available_questions:
                if len(self.used_questions) >= len(available_questions):
                    break

                # Ensure we don't repeat questions in the same session
                question_idx = available_questions.index(question)
                if question_idx in self.used_questions:
                    continue

                self.used_questions.add(question_idx)
                self.total_questions += 1

                result = self.ask_question(question)
                if result is None:  # User quit
                    break

                if result:
                    self.score += 1

                self.show_progress()
                time.sleep(1)

            # Show final results
            self.show_final_results()

            # Ask to play again
            if not self.play_again():
                print("\nThank you for playing! 👋")
                break


# Run the game
if __name__ == "__main__":
    game = FunQuizGame()
    game.run()

