from source.TimeConverterToSeconds import *
import pytest

def test_converter_1():
	assert main_function("6 декад, 8 лет, 35 дней, 3 часа, 14 минут и 7 секунд") == 2147483647
def test_converter_2():
	assert main_function("3 года, 35 дней, 14 минут и 2 секунды") == 97632842
def test_converter_3():
	assert main_function("1 секунда") == 1
def test_converter_4():
	with pytest.raises(ValueError):
		main_function("какой-то неправильный ввод 0 1 2 33___")
def test_converter_5():
	with pytest.raises(ValueError):
		main_function("-2 дня, 50 минут и 2 секунды")
def test_converter_6():
	assert main_function("0 секунд") == 0
def test_converter_7():
	with pytest.raises(IndexError):
		main_function("0")
def test_converter_8():
	with pytest.raises(ValueError):
		main_function(1)
def test_converter_9():
	assert main_function("3 года") == 94608000
def test_converter_10():
	assert main_function("7 дней, 20 часов, 15 минут и 2 секунды") == 677702

"""
def test_converter_2():
	assert converter(70, 24) == (2,22)
def test_converter_3():
	with pytest.raises(TypeError):
		converter('22', 24)
def test_converter_4():
	with pytest.raises(ValueError):
		converter(-12, 24)
"""