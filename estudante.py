nome=str(input("nome: "))
idade=int(input("idade: "))
nota1=int(input("nota1: "))
nota2=int(input("nota2: "))
curso=str(input("curso: "))



estudante = {"nome": nome , "idade": idade, "nota1": nota1, "nota2": nota2, "curso":curso }
             

estudante["media"] = (estudante["nota1"] + estudante["nota2"]) / 2

print(estudante)