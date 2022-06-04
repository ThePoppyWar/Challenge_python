class SingleChoiceQuestion:
    def __init__(self, question: str, response):
        self.question = question
        self.response = response

    def ask(self):
        print(self.question)
        for i, quest in enumerate(self.response):
            print(chr(97 + i) + ')' + quest)
        answer = input("Odpowiedź: ")
        while ord(answer) < 97 or ord(answer) >= 97 + len(self.response):
            answer = input("Niepoprawna odpowiedź, spróbuj ponownie: ")
        return answer

class NumberQuestion:
    def __init__(self, text, min, max):
        self.text = text
        self.min = min
        self.max = max

    def ask(self):
        print(self.text)

        while True:
            odp = input(f"Odpowiedź [{self.min} - {self.max}]: ")
            try:
                odp = input(odp)
            except ValueError:
                print("To nie jest liczba, spróbój ponownie")
                continue
            if odp < self.min or odp > self.max:
                print("Odpowiedź jest za mała lub za duża")
                continue
            return odp

class Questionnaire:
    def __init__(self, title: str):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)
    def run(self):
        print(self.title)
        print()
        answers = {}
        for i, question in enumerate(self.questions):
            answer = question.ask()
            answers[i] = answer
        print("Dziękuję")
        return answers
questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?', ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])
questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)
answers = questionnaire.run()
print(answers)



