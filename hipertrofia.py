def hipertrofia(sexo, TMBm, TMBf, SUPERm, SUPERf, nome):
	print ("E-X-E-L-E-N-T-E, vamos começar a brincadeira!!")
	print ("        █  █ █ █▀█ █▀▀ █▀█ ▀█▀ █▀█ █▀█ █▀▀ █ █▀█         ")
	print ("   约翰-█▀▀█ █ █▀▀ █▀▀ █▀▄  █  █▀▄ █ █ █▀▀ █ █▀█​-佩克索托")
	print ("        ▀  ▀ ▀ ▀   ▀▀▀ ▀ ▀  ▀  ▀ ▀ ▀▀▀ ▀   ▀ ▀ ▀         ")
#	print (linha)
	print ("Já se perguntou o porque no decorrer de determinado tempo de treino o musculo cresce?")
	print ("Se vc esta aqui ja deve conhecer o termo, mas para que nao sabe, hipertrofia é nada mais do que os estimulos nessesarios  para o crescimento de musculos")
	print ("ja que estamos aqui, vamos calcular um superávit e um déficit calorico")
#	print (linha)
	print ("o superavit é nada mais do que a QUANTIDADE de KCAL que seu organismo precisa consumir a mais do que seu tmb para que maximize os ganhos musculares")
	print ("uma quantidade exepcional para isso, se dá de 10% a 20% do seu TMB ")
	SUPERf = TMBf * 0.20
	SUPERm = TMBm * 0.20
	if sexo == "m" or sexo == "masculino":
		print ("seu superávit se dá por: ", SUPERm)
	else:
		print ("seu superávit se dá por: ", SUPERf)
	print ("muito bem! agora que ja sabemos de alguns dados, vamos definir qual seria sua melhor divisão de treino")
	print ("quantos dias da semana você esta disposto(a) treinar? (semanalmente)")
	dias = input().strip().lower()
	if dias == "1" or dias == "um":
		print ("ai nao sobra muitas opçoões né😅")
		print ("mas vamos la")
		print ("quanto tempo vc esta livre nesse dia?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas ou mais")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("bom, ai nos limitamos um pouco, mas relaxa que da pra encaixar algo bem legal ai")
				print ("o treino mais recomendado para você que deseja hipertrofia, seria um full body")
				print ("ok, mas o que é um treino full body?")
				print (" o treino consiste em nada mais que estimular todos os musculos do corpo, com uma intensidade moderada")
				print ("entao seriam dois exercicios por grupo muscular, o que podemos até reduzir para um, caso seu tempo nao encaixe")
			elif horas == "2" or horas == "duas":
				print ("show, ja da para montarmos um treino bem legal!")
				print ("o treino mais recomendado para você que deseja hipertrofia, seria um full body")
				print ("ok, mas o que é um treino full body?")
				print (" o treino consiste em nada mais que estimular todos os musculos do corpo, com uma intensidade moderada")
				print ("entao seriam dois exercicios por grupo muscular, o que podemos até reduzir para um, caso seu tempo nao encaixe")
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("ai sim ein, da pra montar algo muito bom")
				print ("o mais recomendado para hipertrofia, é um treino full body em alta frequencia")
				print ("ta, mas oq é full body de alta frequencia?")
				print ("é nada mais do que o foco em exercicios composto, assim realizando-os em alta frequencia")
			else:
				print ("tente novamente!")
				break
	elif dias == "2" or dias == "dois":
		print ("show de bola!!!")
		print ("dois dias ja da para montar algo bem interessante")
		print ("quantas horas você consegue treinar?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você prefere?")
				print ("[01] upper/lower")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "2" or horas == "duas" or horas == "02":
				print ("muito bem!!!")
				print ("isso é muito bom, ja temos um bom tempo para treinar!!")
				print ("bom, existem duas divisoes de treino muito eficases que chamamos de full bod e upper/lower")
				print ("full body, upper/lower que loucura😵‍")
				print ("vamos destrinchar isso ai!")
				print ("o full body é nada mais que estimular todos os musculos do corpo, com exercicios que estimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você mais se adequa?")
				print ("[01] upper/lower")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você prefere?")
				print ("[01] upper/lower")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
	elif dias == "3" or dias == "03" or dias == "tres" or dias == "três":
		print ("show de bola!!!")
		print ("três dias são tudo o que precizamos para lapidar esse fisico!!!")
		print ("quantas horas você consegue treinar?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("perfeito!")
				print ("isso é muito bom, com essa disponibilidade ja conseguimos montar um treino muito eficiente")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de PPL e ABC")
				print ("tá, mas oq sao esses treinos?")
				print ("o PPL  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que abrangem todos os grupos musculares, dividido em 3 treinos na semana, com uma intensidade moderada")
				print ("ja o ABC consiste em dividir os estimulos em 3 grandes grupos musculares, peito, dorsal e inferiores")
				print ("qual treino você prefere?")
				print ("[01] ABC")
				print ("[02] PPL")
				treino = input().lower().strip()
				if treino == "abc" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "ppl" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o ppl é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "2" or horas == "duas" or horas == "02":
				print ("ótimo!!!")
				print ("agora vamos escolher a estrategia que melhor se encaixa na sua rotina")
				print ("bom, existem duas divisoes de treino muito eficases que chamamos de full body e upper/lower")
				print ("ABC, PPL que loucura😵‍")
				print ("vamos destrinchar isso ai!")
				print ("o PPL,(do ingles, push, pull and legs) é nada mais que estimular todos os musculos do corpo, dividido em 3 treinos, com exercicios pesados e com uma intensidade moderada")
				print ("ja o ABC consiste em estimular os 3 grupo musculares, divididos em peito, dorsal e pernas, com o treino dividido assim, é possivel estimular de forma mais eficiente cada grupo, a diferença do PPL é a forma com que os exercicios sao divididos")
				print ("qual treino você mais se adequa?")
				print ("[01] ABC")
				print ("[02] PPL")
				treino = input().lower().strip()
				if treino == "abc" or treino == "ABC" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "ppl" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada, recomendado para quem nao tem disponibilidade de 3 dias seguidos")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("ja o ABC consiste em estimular os 3 grupo musculares, divididos em peito, dorsal e pernas, com o treino dividido assim, é possivel estimular de forma mais eficiente cada grupo, a diferença do PPL é a forma com que os exercicios sao divididos")
				print ("qual treino você prefere?")
				print ("[01] full body")
				print ("[02] upper/lower")
				print ("[03] ABC")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
				elif treino == "abc" or treino == "03" or treino == "3" or treino == "três" or treino == "tres":
					print ("excelente escolha, o treino certo é o lrincipal fator de crescimento muscular, claro acompanhado da dieta")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
	elif dias == "4" or dias == "04" or dias == "quatro" or dias == "4":
		print ("show de bola!!!")
		print ("quatro dias é tudo o que precizamos!!")
		print ("quantas horas você esta disponivel para treinar?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("perfeito!")
				print ("isso é muito bom, com essa disponibilidade ja conseguimos montar um treino muito eficiente")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e ABC")
				print ("tá, mas oq sao esses treinos?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o ABC consiste em dividir os estimulos em 3 grandes grupos musculares, peito, dorsal e inferiores")
				print ("qual treino você prefere?")
				print ("[01] ABC")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "abc" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "2" or horas == "duas" or horas == "02":
				print ("ótimo!!!")
				print ("agora vamos escolher a estrategia que melhor se encaixa na sua rotina")
				print ("bom, existem duas divisoes de treino muito eficases que chamamos de full body e upper/lower")
				print ("full body, upper/lower que loucura😵‍")
				print ("vamos destrinchar isso ai!")
				print ("o full body é nada mais que estimular todos os musculos do corpo, com exercicios que estimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você mais se adequa?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você prefere?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break

	elif dias == "3" or dias == "03" or dias == "tres" or dias == "três":
		print ("show de bola!!!")
		print ("três dias são tudo o que precizamos para lapidar esse fisico!!!")
		print ("quantas horas você consegue treinar?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("perfeito!")
				print ("isso é muito bom, com essa disponibilidade ja conseguimos montar um treino muito eficiente")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e ABC")
				print ("tá, mas oq sao esses treinos?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o ABC consiste em dividir os estimulos em 3 grandes grupos musculares, peito, dorsal e inferiores")
				print ("qual treino você prefere?")
				print ("[01] ABC")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "abc" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "2" or horas == "duas" or horas == "02":
				print ("ótimo!!!")
				print ("agora vamos escolher a estrategia que melhor se encaixa na sua rotina")
				print ("bom, existem duas divisoes de treino muito eficases que chamamos de full body e upper/lower")
				print ("full body, upper/lower que loucura😵‍")
				print ("vamos destrinchar isso ai!")
				print ("o full body é nada mais que estimular todos os musculos do corpo, com exercicios que estimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você mais se adequa?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você prefere?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break

	elif dias == "3" or dias == "03" or dias == "tres" or dias == "três":
		print ("show de bola!!!")
		print ("três dias são tudo o que precizamos para lapidar esse fisico!!!")
		print ("quantas horas você consegue treinar?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("perfeito!")
				print ("isso é muito bom, com essa disponibilidade ja conseguimos montar um treino muito eficiente")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e ABC")
				print ("tá, mas oq sao esses treinos?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o ABC consiste em dividir os estimulos em 3 grandes grupos musculares, peito, dorsal e inferiores")
				print ("qual treino você prefere?")
				print ("[01] ABC")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "abc" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "2" or horas == "duas" or horas == "02":
				print ("ótimo!!!")
				print ("agora vamos escolher a estrategia que melhor se encaixa na sua rotina")
				print ("bom, existem duas divisoes de treino muito eficases que chamamos de full body e upper/lower")
				print ("full body, upper/lower que loucura😵‍")
				print ("vamos destrinchar isso ai!")
				print ("o full body é nada mais que estimular todos os musculos do corpo, com exercicios que estimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você mais se adequa?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você prefere?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break

	elif dias == "3" or dias == "03" or dias == "tres" or dias == "três":
		print ("show de bola!!!")
		print ("três dias são tudo o que precizamos para lapidar esse fisico!!!")
		print ("quantas horas você consegue treinar?")
		print ("1 hora")
		print ("2 horas")
		print ("3 horas")
		while True:
			horas = input().lower().strip()
			if horas == "1" or horas == "uma":
				print ("perfeito!")
				print ("isso é muito bom, com essa disponibilidade ja conseguimos montar um treino muito eficiente")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e ABC")
				print ("tá, mas oq sao esses treinos?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o ABC consiste em dividir os estimulos em 3 grandes grupos musculares, peito, dorsal e inferiores")
				print ("qual treino você prefere?")
				print ("[01] ABC")
				print ("[02] full body")
				treino = input().lower().strip()
				if treino == "abc" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "2" or horas == "duas" or horas == "02":
				print ("ótimo!!!")
				print ("agora vamos escolher a estrategia que melhor se encaixa na sua rotina")
				print ("bom, existem duas divisoes de treino muito eficases que chamamos de full body e upper/lower")
				print ("full body, upper/lower que loucura😵‍")
				print ("vamos destrinchar isso ai!")
				print ("o full body é nada mais que estimular todos os musculos do corpo, com exercicios que estimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você mais se adequa?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break
			elif horas == "3" or horas == "três" or horas == "tres":
				print ("sensacional!")
				print ("isso é muito bom, ja podemos encaixar dois treinos diferentes")
				print ("bom, existem duas divisoes de treino muito eficientes que chamamos de full bod e upper/lower")
				print ("tá, mas oq sao essas coisas?")
				print ("o full body  consiste em nada mais que estimular todos os musculos do corpo, com exercicios que esyimulam grandes grupos musculares, com uma intensidade moderada")
				print ("ja o upper/lower consiste em estimular os grupo musculares em superior e inferior, com o treuno dividido em dois, é possivel estimular de forma mais eficiente cada grupo")
				print ("qual treino você prefere?")
				print ("[01] full body")
				print ("[02] upper/lower")
				treino = input().lower().strip()
				if treino == "upper lower" or treino == "upper/lower" or treino == "01" or treino == "1" or treino == "um":
					print ("show de bola, esse é um treino equilibrado, intenso na medida, da elite para a elite né?")
				elif treino == "full body" or treino == "dois" or treino == "02" or treino == "2":
					print ("ai sim ein, quando o ponto é estimulo muscular, o full body é imbativel!")
					break
				else:
					print ("tente novamente")
				print ("precione ENTER para continuar")
				input()
				break

	else:
		pass

