#Crie uma função que receba uma palavra por parâmetro
#E permita inverter a ordem dessa palavra. Exemplo: ATOR = ROTA 

def occupation(name):
    value=len(name)+1
    for i in range(1,value):
       count=i*-1
       print(name[count])    
invert=input("Qual nome/palavra voce deseja inverter? - ") 
occupation(invert)
 