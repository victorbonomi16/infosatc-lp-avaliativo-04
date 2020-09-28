#Crie uma função que receba por parâmetro
#DUAS palavras e verifique se uma é o inverso da outra.
#adicionei um print para as pessoas que nao sabem muito de ingles
#e ficam perdidas em true e false apesar de ser algo simples.

def check (name,comparename):
    if comparename == name [::-1]:
        return True 
    else:
        return False
name        = input("Informe o nome a ser verificado:") 
comparename = input ("Informe o nome invertido a ser comparado:") 
compare     = check (comparename,name)
print("Para conferir basta verificar - Verdadeiro = True / Falso = False.")
print ("o nome comparado é:",compare)