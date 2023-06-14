class Execucao:
	def executar(self):
		print('Método do módulo 4 executado')

# O bloco abaixo funciona da seguinte forma:
# 1) Caso esse módulo (script) esteja sendo executado de forma direta (ex. pelo terminal ou pressionando build - CTRL + B), o bloco dentro da condição será executado
# 2) Caso o módulo esteja sendo importado por outro arquivo de código para ser utilizado (executado), o bloco dentro da condição if não será executado

if __name__ == '__main__':

	e = Execucao() # Instanciação da classe
	e.executar() # Execução do método