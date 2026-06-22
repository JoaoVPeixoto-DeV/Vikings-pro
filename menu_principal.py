import sys
from hipertrofia import hipertrofia
def meio_fim(sexo, TMBf, TMBm, SUPERf, SUPERm, nome):
	while True:
		try:
#			print (linha)
			pass
			print ("============qual se objetivo?============")
#			print (linha)
			print ("[01] hipertrofia, quem nao quer ficar gigante né?")
			print ("[02] powerlifter, entao vc quer aumemtar seus PR's")
			print ("[03] secar/definição, então vc quer definir esse habdomen")
			print ("[04] ver meu perfil")
			print ("[05]sair")
			opçao = input().strip() .lower()
			print (repr(opçao))
			match opçao:
				case "1"| "01" | "um" | "hipertrofia":
					print ("debug")
					hipertrofia (sexo, TMBm, TMBf, SUPERm, SUPERf, nome)
				case "2" | "02" | "dois" | "powelifiter":
					pass #powerlifter()
				case "3" | "03" | "tres" | "três" | "secar" | "definição":
					pass #secar()
				case "4" | "04" | "quatro" | "meu perfil":
					pass #meu_perfil()
				case "5" | "05" | "cinco" | "sair":
					print ("que pena, deseja mesmo sair?🥺(sim/não)")
					sair_confirmar = input( ).lower().strip()
					match sair_confirmar:
						case "sim" | "s":
							print ("\nestamos a disposição quando precisar, a equipe da Viking's agradece!!")
							sys.exit()
						case "não" | "nao" | "n":
							print ("\nufa, voltando ao menu🥳🥳")
						#	print (linha)
							print ("Pressione ENTER para continuar")
							input()
		except ValueError:
			print ("opção invalida, tente novamente")
