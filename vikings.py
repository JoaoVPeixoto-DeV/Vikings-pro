import os
def clear():
	os.system("clear")
def calcular_dados():
	global agua_d, TMBm, TMBf
	agua_d = 35 * peso / 1000
	TMBm = 10 * peso + 6.25 * altura - 5 * idade + 5
	TMBf = 10 * peso + 6.25 * altura - 5 * idade - 161
	SUPERf = TMBf * 0.20
	SUPERm = TMBm * 0.20
print(" ██╗   ██╗██╗██╗  ██╗██╗███╗   ██╗ ██████╗  ██████╗")
print(" ██║   ██║██║██║ ██╔╝██║████╗  ██║██╔════╝ ██╔════╝")
print(" ██║   ██║██║█████╔╝ ██║██╔██╗ ██║██║  ███╗╚█████╗  ")
print(" ╚██╗ ██╔╝██║██╔═██╗ ██║██║╚██╗██║██║   ██║ ╚═══██╗ ")
print("  ╚████╔╝ ██║██║  ██╗██║██║  ████║╚██████╔╝██████╔╝ ")
print("   ╚═══╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═════╝  ")
print("========O seu app de consultoria esportiva=========")
print()
linha2 = "-" *55
linha = "=" * 55
while True:
	try:
		global nome, idade, altura, peso, agua_d, TMBm, TMBf
		nome = input("qual o seu nome? ")
		print (linha)
		print ("seja bem vindo ao viking's!!!")
		print (nome, "para começar, vamos calcular sua TMB(taxa metabolica basal)")
		print ("mas primeiro, o que é o TMB?, o TMB é nada mais do que a quantidade de kcal que seu corpo gasta para manter as funçoes vitais, e isso ³ essencial para montarmos uma consultoria de qualidade")
		print (linha)
		print ("mas para saber disso, precisaremos de alguns dados:")
		print ("qual sua idade?")
		idade = float(input())
		if idade <= 0 or idade >= 120:
			print (nome, ",a idade é invalida")
		else:
			break
	except ValueError:
		print("Idade inválida! Digite apenas números.")
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
        	print("altura inválida! Digite apenas números.")
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
		print("peso inválida! Digite apenas números.")
while True:
	sexo = input("qual seu genero?(digite M para masculino e F para feminino)")
	if sexo == "M" or sexo == "m" or sexo == "F" or sexo == "f":
		break
	print ("opção invalida")
calcular_dados()
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
clear()
linha = "=" * 55
while True:
	try:
		print (linha)
		print ("============qual se objetivo?============")
		print (linha)
		print ("[01] hipertrofia, quem nao quer ficar gigante né")
		print ("[02] powerlifter, entao vc quer aumemtar seus PR's")
		print ("[03] secar/definição, então vc quer definir esse habdomen")
		print ("[04] ver meu perfil")
		print ("[05]sair")
		resp = input( ).strip() .lower()
		print ()
		if resp == "1" or resp == "01" or resp == "um":
			print ("E-X-E-L-E-N-T-E, vamos começar a brincadeira!!")
			print ("        █  █ █ █▀█ █▀▀ █▀█ ▀█▀ █▀█ █▀█ █▀▀ █ █▀█         ")
			print ("   约翰-█▀▀█ █ █▀▀ █▀▀ █▀▄  █  █▀▄ █ █ █▀▀ █ █▀█​-佩克索托")
			print ("        ▀  ▀ ▀ ▀   ▀▀▀ ▀ ▀  ▀  ▀ ▀ ▀▀▀ ▀   ▀ ▀ ▀         ")
			print (linha)
			print ("Já se perguntou o porque no decorrer de determinado tempo de treino o musculo cresce?")
			print ("Se vc esta aqui ja deve conhecer o termo, mas para que nao sabe, hipertrofia é nada mais do que uma adaptação biologica das fibras musculare por conta do desgaste, da tensao mechanica e da carga, surreal nosso corpo né?")
			print ("ja que estamos aqui, vamos calcular um superávit e um déficit calorico")
			print (linha)
			print ("o superavit é nada mais do que a QUANTIDADE de KCAL que seu organismo precisa consumir a mais do que sua TMB(vimos isso no começo do app), para hipertrofiar/construir musculos")
			print ("uma quantidade exepcional para isso, se dá de 10% a 20% do seu TMB ")
			SUPERf = TMBf * 0.20
			SUPERm = TMBm * 0.20
			if sexo == "m" or sexo == "masculino":
				print ("seu superávit se dá por: ", SUPERm)
			else:
				print ("seu superávit se dá por: ", SUPERf)
			break
		elif resp == "2" or resp == "02" or resp == "dois":
			print ("muito bem, vamos comstruir uma força inigualavel")
			break
#o .strip() serve para apagar qualquer espaço que a pesso tenha deixado ao responder
#o .lower() deixa a rwsposta da pessoa tudo minusculo, usei ele para reduzir o uso de .replace()
#vale ressaltar que eles sao sempre companheiros do input() junto com o .replace()
		elif resp == "3" or resp == "03" or resp == "três" or resp == "tres":
			print ("sensacional, vamos trincar esse habdomen!!")
		elif resp == "4" or resp == "04" or resp == "quatro":
			print
			while True:
				try:
					print (linha2)
					print ("Sensacional, vamos dar uma olhada nos seus dados!!")
					print ("========MEU PERFIL=======")
					print (linha)
					print ("Nome: ", nome)
					print (linha2)
					print ("Idade: ", idade)
					print (linha2)
					print ("Altura: ", altura)
					print (linha2)
					print ("Peso: ", peso)
					print (linha2)
					if sexo == "m":
						print ("Genero: ", sexo)
						print (linha2)
					else:
						print ("Genero: ", sexo)
						print (linha2)
					if sexo == "f":
						print ("Taxa metabólica: ", TMBf)
					else:
						print ("Taxa metabólica: ", TMBm)
					print ("Agua diaria:(em Litros) ", agua_d)
					print ("Deseja alterar algo?(sim/não)")
					alterar_perfil = input().strip().lower()
					if alterar_perfil == "sim" or alterar_perfil == "s":
						print ("o que deseja alterar?")
						print ("[01] Nome")
						print ("[02] Idade")
						print ("[03] Altura")
						print ("[04] peso")
						alterar = input().strip().lower()
						if alterar == "1" or alterar == "01" or alterar == "nome":
							nome = input("digite o seu nome: ")
							print ("nome alterado com susseso!!!")
							TMBm = 10 * peso + 6.25 * altura - 5 * idade + 5
							TMBf = 10 * peso + 6.25 * altura - 5 * idade - 161
							calcular_dados()
						elif alterar == "2" or alterar == "02" or alterar == "idade":
							idade = float(input("digite sua idade: "))
							print ("idade alterada com susesso!!!")
							TMBm = 10 * peso + 6.25 * altura - 5 * idade + 5
							TMBf = 10 * peso + 6.25 * altura - 5 * idade - 161
						elif alterar == "3" or alterar == "03" or alterar == "altura":
							altura = float(input("digite sua altura: "))
							print ("altura alterada com susseso")
							TMBm = 10 * peso + 6.25 * altura - 5 * idade + 5
							TMBf = 10 * peso + 6.25 * altura - 5 * idade - 161
							calcular_dados()
						elif alterar == "4" or alterar == "04" or alterar == "peso":
							peso = float(input("digite seu peso: "))
							print ("peso alterada com susesso!!!")
							TMBm = 10 * peso + 6.25 * altura - 5 * idade + 5
							TMBf = 10 * peso + 6.25 * altura - 5 * idade - 161
							calcular_dados()
						input("\nAperte ENTER para concluir a atualização do perfil")
						continue
					else:
						print ("voltando ao menu principal...")
						print("...")
						input("aperte ENTER para proseguir")
						break
				except ValueError:
					print ("opção invalida, tente novamente")
					continue
		elif resp == "5" or resp == "05" or resp == "cinco":
			print ("que pena, deseja mesmo sair?🥺(sim/não)")
			sair_confirmar = input( ).lower().strip()
			if sair_confirmar == "sim" or sair_confirmar == "s" or sair_confirmar == "ss" or resp == "sin":
				print ("\nestamos a disposição quando precisar, a equipe da vikings agradece.... até logo!!!")
				exit()
			else:
				print ("\nufa, voltando ao menu🥳🥳")
				print(linha)
				continue
	except ValueError:
		print ("opção invalida, tente novamente")
