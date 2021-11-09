#Desejo que minha função receba 2 valores e retorne sucesso caso seja possível fazer a divisão Objetivo do teste:
#Verificar se a divisão entre 2 valores numéricos retorna sucesso
#d. Caso

from unittest import TestCase

def divisao(valor1, valor2):
    return valor1 / valor2

class validadivisao(TestCase):
    def testedivisao(self):
        self.assertTrue(divisao(10, 2))

def divisao(valor1, valor2):
    try:
        valor1 / valor2
        return True
    except:
        return False

