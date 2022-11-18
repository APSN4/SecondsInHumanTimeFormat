input_number = 2147483647 # Long int

resultMinutes = 0
resultHours = 0
resultDays = 0
resultYears = 0
resultDecades = 0
resultCenturies = 0

def converter(number, critical_var):
    if not(isinstance(number, int)) or not(isinstance(critical_var, int)):
        raise TypeError("number or critical_var not <int>")
    elif number < 0 or critical_var < 0:
        raise ValueError("number negative values are not allowed")
    NextValue = 0
    old_number = 0
    if number >= critical_var:
        while number >= critical_var:
            number -= critical_var
            if not(number < 0):
                NextValue += 1
            elif number == 0:
                NextValue += 1
    if number != critical_var:
        old_number = abs(number)
    return NextValue, old_number

resultMinutes, input_number  = converter(input_number, 60)
if resultMinutes >= 60:
    resultHours, resultMinutes = converter(resultMinutes, 60)
if resultHours >= 24:
    resultDays, resultHours = converter(resultHours, 24)
if resultDays >= 365:
    resultYears, resultDays = converter(resultDays, 365)
if resultYears >= 10:
    resultDecades, resultYears = converter(resultYears, 10)
if resultDecades >= 10:
    resultCenturies, resultDecades = converter(resultDecades, 10)

def text(number, words):
    if len(words) != 3:
        raise RuntimeError("the number of words should be 3")
    if not(number >= 0):
        raise ValueError("number negative values are not allowed")
    for i in range(len(words)):
        if not(words[i] == str(words[i])):
            raise TypeError("only strings are accepted")
    myList = [21, 31, 41, 51, 61, 71, 81, 91]
    number_local = str(number)
    number_local = number_local[len(number_local)-1]
    number_local = int(number_local)
    local = ""
    if number > 100:
        number = str(number)
        number = number[1:]
        number.lstrip('0')
        number = int(number)
    if number < 21:
        for timer_loop in range(1, number+1):
            if timer_loop == 1:
                local = words[0]
            elif timer_loop > 1 and timer_loop <= 4:
                local = words[1]
            elif timer_loop > 4 and timer_loop < 21:
                local = words[2]
    elif number >= 21 and number <= 100:
        timer_loop = 0
        if number % 10 == 1:
            local = words[0]
        local = min(myList, key=lambda x:abs(x-number))
        if local > number:
            for i in myList:
                if number > i:
                    local = i
        checker = abs(local - number)
        if checker == 0:
            local = words[0]
        elif checker == 1 or checker == 2 or checker == 3:
            local = words[1]
        else:
            local = words[2]
    return local

_outputString = ""
local_data_i = -1
i_used = False
array_str_index = []
if resultCenturies != 0:
    _outputString += str(resultCenturies) + " " + text(resultCenturies, ['век', 'века', 'веков']) + ","
    array_str_index.append(len(_outputString) - 1)
if resultDecades != 0:
    _outputString += " " + str(resultDecades) + " " + text(resultDecades, ['декада', 'декады', 'декад']) + ","
    array_str_index.append(len(_outputString) - 1)
if resultYears != 0:
    _outputString += " " + str(resultYears) + " " + text(resultYears, ['год', 'года', 'лет']) + ","
    array_str_index.append(len(_outputString) - 1)
if resultDays != 0:
    _outputString += " " + str(resultDays) + " " + text(resultDays, ['день', 'дня', 'дней']) + ","
    array_str_index.append(len(_outputString) - 1)
if resultHours != 0:
    _outputString += " " + str(resultHours) + " " + text(resultHours, ['час', 'часа', 'часов']) + ","
    array_str_index.append(len(_outputString) - 1)
if resultMinutes != 0:
    _outputString += " " + str(resultMinutes) + " " + text(resultMinutes, ['минута', 'минуты', 'минут']) + ","
    array_str_index.append(len(_outputString) - 1)
if input_number != 0:
    _outputString += " " + str(input_number) + " " + text(input_number, ['секунда', 'секунды', 'секунд'])
    array_str_index.append(len(_outputString) - 1)

_outputString = _outputString.lstrip(' ')

if input_number != 0:
    local_data_i = input_number
elif resultMinutes != 0:
    local_data_i = resultMinutes
elif resultHours != 0:
    local_data_i = resultHours
elif resultDays != 0:
    local_data_i = resultDays
elif resultYears != 0:
    local_data_i = resultYears
elif resultDecades != 0:
    local_data_i = resultDecades
elif resultCenturies != 0:
    local_data_i = resultCenturies

array_results = [input_number, resultMinutes, resultHours, resultDays, resultYears, resultDecades, resultCenturies]
array_value = 0
for value in range(0, len(array_results)):
    if array_results[value] != 0:
        array_value += 1
if array_value == 1 or array_value == 0:
    local_data_i = -1

if local_data_i != -1:
    index_i = _outputString.rfind(str(local_data_i))
    _outputString = _outputString[:index_i] + 'и ' + _outputString[index_i:]
    _outputString = _outputString[:index_i-2] + _outputString[index_i-1:]
    if array_value == 2 and input_number == 0:
        _outputString = _outputString[:-1]
if array_value == 1 and input_number == 0:
    _outputString = _outputString[:-1]


print(_outputString)