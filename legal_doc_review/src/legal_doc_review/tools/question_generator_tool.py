class QuestionGeneratorTool:
    @staticmethod
    def generate_questions(risk_text: str) -> list:
        """Generate yes/no questions from detected risks."""
        questions = []
        for line in risk_text.splitlines():
            if line.strip() and not line.startswith('❗'):
                questions.append(f"Detected: {line.strip()}.\nWould you like to improve this clause? [y/n]: ")
        return questions
