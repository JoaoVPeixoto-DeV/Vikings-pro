from menu_principal import meio_fim
def clear():
	os.system("clear")
def calcular_dados(peso, altura, idade):
	TMBm = 10 * peso + 6.25 * altura - 5 * idade + 5
	TMBf = 10 * peso + 6.25 * altura - 5 * idade - 161
	SUPERf = TMBf * 0.20
	SUPERm = TMBm * 0.20
	return TMBm, TMBf, SUPERf, SUPERm,
def fachada():
	print (" ██╗   ██╗██╗██╗  ██╗██╗███╗   ██╗ ██████╗  ██████╗")
	print (" ██║   ██║██║██║ ██╔╝██║████╗  ██║██╔════╝ ██╔════╝")
	print (" ╚██╗ ██╔╝██║██╔═██╗ ██║██║╚██╗██║██║   ██║ ╚═══██╗ ")
	print ("  ╚████╔╝ ██║██║  ██╗██║██║  ████║╚██████╔╝██████╔╝ ")
	print ("   ╚═══╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ")
	print ("========O seu app de consultoria esportiva=========")
	print ()
	linha2 = "-" * 55
def pegar_dados():
	linha2 = "-" * 55
	linha = "=" * 55
	while True:
		try:
			nome = input("qual o seu nome? ")
			print (linha)
			print ("seja bem vindo ao viking's!!!")
			print (nome, "para começar, vamos calcular sua TMB(taxa metabolica basal)")
			print ("mas primeiro, o que é o TMB?, o TMB é nada mais do que a quantidade de kcal que seu corpo gasta para manter as funçoes vitais, e isso é essencial para montarmos uma consultoria de qualidade")
			print (linha)
			print ("mas para saber disso, precisaremos de alguns dados:")
			print (nome, "qual sua idade?")
			idade = float(input())
			if idade <= 0 or idade >= 120:
				print (nome, ",a idade é invalida")
			else:
				break
		except ValueError:
			print ("Idade inválida! Digite apenas números.")
	while True:
		try:
			print ("qual sua altura? em centimetros")
			altura = float(input())
			if altura <= 0 or altura >= 272:
				print (nome, "a altura é altura invalida!")
#o cara mais alto da historia tem 272cm
			else:
				break
		except ValueError:
			print ("altura inválida! Digite apenas números.")
	while True:
		try:
			print ("qual o seu peso?(em kg)")
			peso = float(input())
			if peso <= 0 or peso >= 635:
				print (nome, ", o peso é invalido!")
#o cara mais pesado da historia  pesava 635kg
			else:
				break
		except ValueError:
			print ("peso inválida! Digite apenas números.")
	while True:
		sexo = input("qual seu genero?(digite M para masculino e F para feminino)")
		match sexo:
			case "m" | "f":
				print ()
			case _:
        			print ("opção invalida")
		break
	TMBm, TMBf, SUPERf, SUPERm = calcular_dados(peso, altura, idade)
	if sexo == "M" or "m":
		print (linha)
		print (linha2)
		print ("sua taxa metabolica é de", TMBm)
	elif sexo == "F" or "f":
		print ("sua taxa metabolia é de", TMBf)
	print (linha2)
	print (linha)
	print (nome, "agora que ja sabemos sua TMB, conseguimos te oferecer um atendimento personalizado a partir do seu foco")
#print ("aproveite que o app esta em desenvolvimento, depois vamos cobrar")
	input("pressione ENTER para continuar")
	meio_fim(sexo, TMBm, TMBf, SUPERf, SUPERm, nome)
fachada()
pegar_dados()

