# Crie um sistema para cadastrar alunos de uma turma, deve conter nas informação
# dos alunos o nome e as notas de cada disciplina. Aluno deve ser uma classe para
# salvar as informações, e deverá ter um método para calcular o coeficiente do aluno,
# e outro para printar as informações do aluno com o nome, o nome de cada
# disciplina com a nota do aluno, e o coeficiente.

class Aluno:
    #atributos
    def __init__(self, name):
        self.name = name
        self.grade = {}

    #metodos
    def add_grades(self, subject, grade):
        self.grade[subject] = grade

    def calculate_average(self):
        if len(self.average) == 0:
            return 0

        total = 0  
        for key in self.grade.values():
            total += key
        return total / len(self.grade)

    def show_informations(self):
        print("Student:", self.name)

        for subject, grade in self.grade.items():
            print(f"{subject}: {grade}")

        print("Average:", self.calculate_average())

aluno1 = Aluno("Victor")

aluno1.add_grades("POO", 9.0)
aluno1.add_grades("Data Structure", 6.0)

aluno1.calculate_average()

aluno1.show_informations()