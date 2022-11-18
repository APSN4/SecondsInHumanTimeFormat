import re

input_time = "6 декад, 8 лет, 35 дней, 3 часа, 14 минут и 7 секунд"

def main_function(input_time):
	if not(isinstance(input_time, str)):
		raise ValueError("incorrect input")
	input_time = input_time.lower()

	sum_ = 0
	numbers = []

	for s in input_time.split():
		if s.isdigit():
			numbers.append(s)
	try:
		if re.findall(r'\w+', input_time)[0] != numbers[0]:
			raise ValueError("incorrect input")
	except: raise ValueError("incorrect input")

	array_values = [3155760000, 31536000 * 10, 31536000, 86400, 3600, 60, 1]
	n = 1
	error_checker = 0
	if len(numbers) == 1:
		try:
			first_search = re.findall(r'\w+', input_time)[n]
		except IndexError:
			raise IndexError("incorrect input")
		if first_search == 'век' or first_search == 'века' or first_search == 'веков':
			sum_ += int(numbers[0]) * array_values[0]
			error_checker += 1
		elif first_search == 'декада' or first_search == 'декады' or first_search == 'декад':
			sum_ += int(numbers[0]) * array_values[1]
			error_checker += 1
		elif first_search == 'год' or first_search == 'года' or first_search == 'лет':
			sum_ += int(numbers[0]) * array_values[2]
			error_checker += 1
		elif first_search == 'день' or first_search == 'дня' or first_search == 'дней':
			sum_ += int(numbers[0]) * array_values[3]
			error_checker += 1
		elif first_search == 'час' or first_search == 'часа' or first_search == 'часов':
			sum_ += int(numbers[0]) * array_values[4]
			error_checker += 1
		elif first_search == 'минута' or first_search == 'минуты' or first_search == 'минут':
			sum_ += int(numbers[0]) * array_values[5]
			error_checker += 1
		elif first_search == 'секунда' or first_search == 'секунды' or first_search == 'секунд':
			sum_ += int(numbers[0]) * array_values[6]
			error_checker += 1
	else:
		for i in range(len(numbers)):
			if i+1 == len(numbers):
				first_search = re.findall(r'\w+', input_time)[n+1]
			else:
				first_search = re.findall(r'\w+', input_time)[n]
			if first_search == 'век' or first_search == 'века' or first_search == 'веков':
				sum_ += int(numbers[i]) * array_values[0]
				error_checker += 1
			elif first_search == 'декада' or first_search == 'декады' or first_search == 'декад':
				sum_ += int(numbers[i]) * array_values[1]
				error_checker += 1
			elif first_search == 'год' or first_search == 'года' or first_search == 'лет':
				sum_ += int(numbers[i]) * array_values[2]
				error_checker += 1
			elif first_search == 'день' or first_search == 'дня' or first_search == 'дней':
				sum_ += int(numbers[i]) * array_values[3]
				error_checker += 1
			elif first_search == 'час' or first_search == 'часа' or first_search == 'часов':
				sum_ += int(numbers[i]) * array_values[4]
				error_checker += 1
			elif first_search == 'минута' or first_search == 'минуты' or first_search == 'минут':
				sum_ += int(numbers[i]) * array_values[5]
				error_checker += 1
			elif first_search == 'секунда' or first_search == 'секунды' or first_search == 'секунд':
				sum_ += int(numbers[i]) * array_values[6]
				error_checker += 1
			n += 2

	for symbol in input_time:
		if symbol == '-':
			raise ValueError("incorrect input")

	if error_checker == 0:
		raise ValueError("incorrect input")
	return sum_

print(main_function(input_time))