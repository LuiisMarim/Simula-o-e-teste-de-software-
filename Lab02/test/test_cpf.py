import pytest
import sys
sys.path.insert(0, '/workspaces/Simula-o-e-teste-de-software-/Lab02/src')

from cpf import (
	formatar_cpf,
	validar_cpf
)


class TestFormatarCpf:
	"""Testes para a funcao formatar_cpf"""

	def test_formatar_cpf_valido(self):
		"""Testa formatacao de cpf valido"""
		cpf = "52998224725"
		resultado = formatar_cpf(cpf)
		assert resultado == "529.982.247-25"

	def test_formatar_cpf_com_pontuacao(self):
		"""Testa formatacao mantendo padrao"""
		cpf = "529.982.247-25"
		resultado = formatar_cpf(cpf)
		assert resultado == "529.982.247-25"

	def test_formatar_cpf_com_tamanho_invalido(self):
		"""Testa se levanta excecao com cpf menor que 11"""
		cpf = "1234567890"
		with pytest.raises(ValueError, match="CPF deve conter 11 digitos"):
			formatar_cpf(cpf)

	def test_formatar_cpf_com_tamanho_maior(self):
		"""Testa se levanta excecao com cpf maior que 11"""
		cpf = "529982247251"
		with pytest.raises(ValueError, match="CPF deve conter 11 digitos"):
			formatar_cpf(cpf)

	def test_formatar_cpf_com_letras(self):
		"""Testa se levanta excecao com cpf contendo letras"""
		cpf = "abc.def.ghi-jk"
		with pytest.raises(ValueError, match="CPF deve conter 11 digitos"):
			formatar_cpf(cpf)


class TestValidarCpf:
	"""Testes para a funcao validar_cpf"""

	def test_validar_cpf_valido(self):
		"""Testa cpf valido"""
		cpf = "529.982.247-25"
		resultado = validar_cpf(cpf)
		assert resultado == True

	def test_validar_cpf_valido_outro(self):
		"""Testa outro cpf valido"""
		cpf = "39053344705"
		resultado = validar_cpf(cpf)
		assert resultado == True

	def test_validar_cpf_valido_com_zeros(self):
		"""Testa cpf valido com zeros"""
		cpf = "000.000.001-91"		# Act
		resultado = validar_cpf(cpf)
		assert resultado == True

	def test_validar_cpf_invalido_tamanho(self):
		"""Testa cpf com tamanho invalido"""
		cpf = "1234567890"
		resultado = validar_cpf(cpf)
		assert resultado == False

	def test_validar_cpf_invalido_tamanho_maior(self):
		"""Testa cpf com tamanho maior que 11"""
		cpf = "529982247251"
		resultado = validar_cpf(cpf)
		assert resultado == False

	def test_validar_cpf_invalido_com_letras(self):
		"""Testa cpf com letras"""
		cpf = "abc.def.ghi-jk"
		resultado = validar_cpf(cpf)
		assert resultado == False

	def test_validar_cpf_invalido_digitos_iguais(self):
		"""Testa cpf com todos os digitos iguais"""
		cpf = "111.111.111-11"
		resultado = validar_cpf(cpf)
		assert resultado == False

	def test_validar_cpf_invalido_digitos_verificadores(self):
		"""Testa cpf com digitos verificadores invalidos"""
		cpf = "529.982.247-26"
		resultado = validar_cpf(cpf)
		assert resultado == False

	def test_validar_cpf_none(self):
		"""Testa cpf None"""
		cpf = None
		with pytest.raises(TypeError):
			validar_cpf(cpf)

	def test_validar_cpf_string_vazia(self):
		"""Testa cpf string vazia"""
		cpf = ""
		resultado = validar_cpf(cpf)
		assert resultado == False
