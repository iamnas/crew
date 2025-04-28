from tools.question_generator_tool import QuestionGeneratorTool

class QuestionProcessor:
    @staticmethod
    def ask_user_for_risks(risk_text: str) -> dict:
        """Ask the user questions based on risks detected."""
        questions = QuestionGeneratorTool.generate_questions(risk_text)
        
        # ✅ LIMIT TO 5 QUESTIONS
        limited_questions = questions[:5]

        user_responses = {}

        for question in limited_questions:
            while True:
                answer = input(question).strip().lower()
                if answer in ['y', 'n']:
                    break
                else:
                    print("Please enter 'y' or 'n' only.")
            risk_description = question.split('\n')[0].replace('Detected: ', '')
            user_responses[risk_description] = answer

        return user_responses
