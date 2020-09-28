nome=[]
cpf=[]
senha=[]
apto=[]

def printFinal():
    print("Nome:   ",nome," \nCPF:    ",cpf," \nSenha:  ",senha," \nAptidão:",apto)
def cadastroDados():
    nome.append(input("-- Qual seu nome? : "))
    cpf.append(input("-- Qual seu cpf? : "))
    senha.append(input("-- Insira sua senha: "))
    apto.append(input("Você apto para doação de sangue? : "))
    printFinal()

vidade = 0
vpeso = 0
vhoras =0
cadastrado=0

idade=(int(input("-- Qual a sua idade? - ")))
peso=(float(input("-- Qual o seu peso? - ")))
horas=(int(input("-- Quantas horas voce dormiu na ultima noite? - ")))

if idade>=16 and idade<=69:
    vidade+=1
else:
    print("Voce nao tem idade a idade necessaria!")
if peso>50:
    vpeso+=1
else:
    print("Seu peso está fora da media necessaria!")
if horas>=6:
    vhoras+=1
else:
    print("Voce nao dormiu o suficiente!")
if vidade == 1 and vpeso == 1 and vhoras == 1:
    print("Você pode ser um doador!")
    cadastro = (input(" Gostaria de se cadastrar?, Digite 1-Sim ou 2-Não:"))
    if cadastro=="1":
        cadastrado = cadastrado+1
        cadastroDados() 
    else:
        print("Cadastro recusado.")
else:
    print("Você não pode ser um doador.")
    cadastro = (input("Você não possui os minimos requisitos necessarios, mas ainda pode se cadastrar. Digite 1-Sim ou 2-Não:"))
    if cadastro=="1":
        cadastrado = cadastrado+1
        cadastroDados() 
    else:
        print("Cadastro recusado.") 