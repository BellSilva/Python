
# coding: utf-8

# In[5]:


#Atividade 1

altura= int(input("Digite a altura do retângulo: "))
largura= int(input("Digite a largura do retângulo: "))

perimetro  = ((altura*2) + (largura*2))
area = altura * largura
print("perimetro:", perimetro, "-", " area:", area)


# In[81]:


#Atividade 2

pagamento=float(input("Valor total da compras: "))
escolha=int(input("Escolha uma forma de pagamento, sendo:\n
1. À vista em dinheiro, recebe 10% de desconto;\n
2. À vista no cartão de crédito, recebe 5% de desconto; \n
3. Em 2 vezes, preço normal de etiqueta sem juros;\n
4. Em 3 vezes, preço normal de etiqueta mais 10% de juros: "))
total = 0
if escolha==1:
    total=(pagamento - (0.1*pagamento))
    print("O Valor a ser pago será de: ", total)
else: 
    if escolha==2:
        total=(pagamento-(0.05*pagamento))
        print("O Valor a ser pago será de: ", total)
    else: 
        if escolha==3:
            total=pagamento/2
            print("O Valor a ser pago será de: ", total , "Parcelado de 2x sem juros")
        else:
            if escolha==4:
                total=((pagamento+(0.1*pagamento))/3)
                print("O Valor a ser pago será de: ", total , "Parcelado de 3x com 10% de juros")   


# In[77]:


#Atividade 3

altura=float(input("Digite sua altura: "))
peso= int(input("Digite seu peso: "))
imc =peso/(altura*altura)

if (imc<18.5):
        print("abaixo do peso")
else:
    if ((imc>=18.5) and (imc<=25)):
        print("peso normal")
    else:
        if ((imc>25) and (imc<=30)):
            print("acima do peso")
        else:
            if (imc>30):
                print("obeso")


# In[79]:


#Atividade 4

mes = int(input("Qual o número do mês: "))

if mes == 1:
    print('Janeiro')
elif mes == 2:
    print('Fevereiro')
elif mes == 3:
    print('Março')
elif mes == 4:
    print('Abril')
elif mes == 5:
    print('Maio')
elif mes == 6:
    print('Junho')
elif mes == 7:
    print('Julho')
elif mes == 8:
    print('Agosto')
elif mes == 9:
    print('Setembro')
elif mes == 10:
    print('Outubro')
elif mes == 11:
    print('Novembro')
elif mes == 12:
    print('Dezembro')
else:
    print("Nenhum mês correspondente com o ", mes)


# In[84]:


#Atividade 5

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
print("Escolha a operação que deseja realizar:\n 1. Média entre os números digitados \n 2. Diferença do maior pelo menor\n 3. Produto entre os números digitados\n 4. Divisão do primeiro pelo segundo")
operacao = int(input('Digite o código de operação: '))

if operacao == 1:
    resultado = (numero1+numero2)/2
elif operacao == 2:
    if numero1 > numero2:
        resultado = numero1-numero2
    else:
        resultado = numero2-numero1
elif operacao == 3:
    resultado = numero1*numero2
elif operacao == 4:
    resultado = numero1/numero2

print("Resultado: ", resultado)


# In[88]:


#Atividade 6

pluviometrico = list()
for x in range(31):
    print('Informe o indice pluviometrico do dia ', x+1 ,':', end="",sep="")
    pluviometrico.append(float(input()))
print('Indice pluviométrico médio:',sum(pluviometrico)/len(pluviometrico))
print('Indice pluviométrico máximo:',max(pluviometrico),'| Dia de ocorrência:',pluviometrico.index(max(pluviometrico))+1)


# In[92]:


#Atividade 7

idade = 1
numero = 1
feminino = 0
while(idade > 0):
    print(numero,'ª Pessoa')
    sexo = input('Sexo: [M|F] ')
    corOlho = input('Cor dos olhos: [Azuis|Verdes|Castanhos] ')
    corCabelo = input('Cor dos Cabelos: [Louros|Castanhos|Pretos] ')
    idade = int(input('Idade: '))
    if ((sexo in 'Ff') and (idade > 18) and (idade < 35)):
        feminino += 1
print("O número de habitante do sexo feminino entre 18 e 35 anos é de: ", feminino)


# In[93]:


#Atividade 8

massa = float(input('Informe a massa do material: '))
massaInic = massa
tempo = 0
while massa > 0.5:
    massa = massa / 2
    tempo += 50

print('Massa Inicial: ', massaInic ,' gramas\n Massa Final: ', massa ,' gramas\n Tempo decorrido: ' , tempo ,' segundos') 


# In[ ]:


#Atividade 9

salario = float(input('Informe o Salário do funcionário: '))
while salario <=0 :
    salario = float(input('Salário inválido, informe novamente o Salário: '))
opcao = 0
while opcao != 4:
    opcao = int(input('Selecione uma das opção abaixo: \n     [ 1. ] Novo Salário \n     [ 2. ] Férias \n     [ 3. ] Décimo Terceiro \n     [ 4. ] Sair\n'))

    if opcao == 1:
        
        salario = float(input('Informe o novo Salário:'))
        if salario < 1000:
            salario = salario = (salario * 0.15)
            print('O novo salário é de: ',salario)
        elif salario >= 1000 and salario >= 2000:
            salario = salario = (salario * 0.10)
            print('O novo salário teve um aumento de: ',salario)
        else:
            salario = salario = (salario * 0.05)
            print('O novo salário teve um aumento de: ' , salario )
    elif opcao == 2:
        ferias = salario + (salario/3)
        print('O valor das férias é de: ',ferias)
    elif opcao == 3:
        meses = int(input('Informe à quantidade de meses trabalhado no ano: '))
        while meses < 0 and meses >12:
            meses = int(input('Quantidade de meses trabalhado inválida! Informe corretamente a quantidade de meses trabalhado: '))
        if meses == 0:
            print('Você não possui direito ao 13º')
        else:
            dec_13 = (salario * meses) / 12
            print('O valor do 13º é:',dec_13)
    elif opcao == 4:
        print('Sessão Finalizada!')
    else:
        print('Opção Inválida!!!')

