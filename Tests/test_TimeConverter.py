from source.TimeConverter import *
import pytest

def test_converter_1():
	assert converter(30, 60) == (0,30)
def test_converter_2():
	assert converter(70, 24) == (2,22)
def test_converter_3():
	with pytest.raises(TypeError):
		converter('22', 24)
def test_converter_4():
	with pytest.raises(ValueError):
		converter(-12, 24)

def test_text_1():
	assert text(20, ['час', 'часа', 'часов']) == 'часов'
def test_text_2():
	assert text(234, ['день', 'дня', 'дней']) == 'дня'
def test_text_3():
	assert text(1, ['декада', 'декады', 'декад']) == 'декада'
def test_text_4():
	with pytest.raises(ValueError):
		assert text(-32, ['минута', 'минуты', 'минут'])
def test_text_5():
	with pytest.raises(TypeError):
		assert text(32, [1, 'минуты', 'минут'])
def test_text_6():
	with pytest.raises(RuntimeError):
		assert text(88, ['день', 'дня'])