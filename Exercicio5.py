from tools.ReceiveUserInput import ReceiveUserInput
from tools.ShowResult import ShowResult

def GetStudentGrade(Grade):
    if  0 <= Grade < 5:
        return "E"
    elif 5 <= Grade < 6:
        return "D"
    elif 6 <= Grade < 7:
        return "C"
    elif 7 <= Grade < 9:
        return "B"
    elif Grade >= 9:
        return "A"

def index():
    Student = 1

    while(Student < 11):
        Grade = int(ReceiveUserInput(f"Informe a nota do estudante {Student}"))
        if(Grade > 10 or Grade < 0):
            print("Insira uma nota válida")
        else:
            ShowResult("O conceito da nota do estudante é", GetStudentGrade(Grade))

        Student = 1 + Student


index()