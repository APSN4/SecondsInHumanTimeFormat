input_number = 2147483647 # Long int

resultMinutes = 0
resultHours = 0
resultDays = 0
resultYears = 0
resultDecades = 0
resultCenturies = 0

def _converter(number, critical_var):
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

resultMinutes, input_number  = _converter(input_number, 60)
if resultMinutes >= 60:
    resultHours, resultMinutes = _converter(resultMinutes, 60)
if resultHours >= 24:
    resultDays, resultHours = _converter(resultHours, 24)
if resultDays >= 365:
    resultYears, resultDays = _converter(resultDays, 365)
if resultYears >= 10:
    resultDecades, resultYears = _converter(resultYears, 10)
if resultDecades >= 10:
    resultCenturies, resultDecades = _converter(resultDecades, 10)

def _text(number, name, words):
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
if resultCenturies != 0:
    _outputString += str(resultCenturies) + " " + _text(resultCenturies, "век", ['век', 'века', 'веков'])
    if not(resultDecades == 0) and not(resultYears == 0) and not(resultDays == 0) and not(resultHours == 0) and not(resultMinutes == 0) and not(input_number == 0):
        _outputString += ","
    elif not(resultDecades == 0) or not(resultYears == 0) or not(resultDays == 0) or not(resultHours == 0) or not(resultMinutes == 0) or not(input_number == 0):
        _outputString += " и"
if resultDecades != 0:
    _outputString += " " + str(resultDecades) + " " + _text(resultDecades, "декад", ['декада', 'декады', 'декад'])
    if not(resultYears == 0) and not(resultDays == 0) and not(resultHours == 0) and not(resultMinutes == 0) and not(input_number == 0):
        _outputString += ","
    elif not(resultYears == 0) or not(resultDays == 0) or not(resultHours == 0) or not(resultMinutes == 0) or not(input_number == 0):
        _outputString += " и"
if resultYears != 0:
    _outputString += " " + str(resultYears) + " " + _text(resultYears, "год", ['год', 'года', 'лет'])
    if not(resultDays == 0) and not(resultHours == 0) and not(resultMinutes == 0) and not(input_number == 0):
        _outputString += ","
    elif not(resultDays == 0) or not(resultHours == 0) or not(resultMinutes == 0) or not(input_number == 0):
        _outputString += " и"
if resultDays != 0:
    _outputString += " " + str(resultDays) + " " + _text(resultDays, "ден", ['день', 'дня', 'дней'])
    if not(resultHours == 0) and not(resultMinutes == 0) and not(input_number == 0):
        _outputString += ","
    elif not(resultHours == 0) or not(resultMinutes == 0) or not(input_number == 0):
        _outputString += " и"
if resultHours != 0:
    _outputString += " " + str(resultHours) + " " + _text(resultHours, "час", ['час', 'часа', 'часов'])
    if not(resultMinutes == 0) and not(input_number == 0):
        _outputString += ","
    elif not(resultMinutes == 0) or not(input_number == 0):
        _outputString += " и"
if resultMinutes != 0:
    _outputString += " " + str(resultMinutes) + " " + _text(resultMinutes, "минут", ['минута', 'минуты', 'минут'])
    if not(input_number == 0):
        _outputString += " и"
if input_number != 0:
    _outputString += " " + str(input_number) + " " + _text(input_number, "секунд", ['секунда', 'секунды', 'секунд'])

_outputString = _outputString.lstrip(' ')
print(_outputString)