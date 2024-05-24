from datetime import datetime
def leaders_quiz(data: list):
    """
    Example data:
    [['saka', 4, '03:01:03.1'], ['florian', 3, '03:01:03.1']
    
    """
    list_of_strings = []
    for index in range(10):
        list_of_strings.append(f"""{index + 1}. @{data[index][0]}\nПравильных ответов: {data[index][1]}\nВремя прохождения: {format_time_string(data[index][2])}\n\n""")

    return ''.join(list_of_strings)

# def convert_time(data):

def format_time_string(current_time) -> str:
    """
    Input Type: Datetime.now()
    """
    current_time = datetime.strptime(current_time, "%H:%M:%S.%f")
    time_components = []
    hours, minutes, seconds, microseconds = current_time.hour, current_time.minute, current_time.second, current_time.microsecond
    if hours:
        time_components.append(f"{hours} часов")

    if minutes:
        time_components.append(f"{minutes} минут")


    if microseconds and seconds:
        time_components.append(f"{seconds}.{str(microseconds)[:2]} секунд")
    
    elif microseconds and not seconds:
        time_components.append(f'{str(microseconds)[:2]} миллисекунд')
    
    elif seconds:
        time_components.append(f"{seconds} секунд")


    return " ".join(time_components)




# list_of_strings.append(f"""{index + 1}. @{value[0]}\nПравильных ответов: {value[1]}\nВремя прохождения: {datetime.strptime(value[2], "%H:%M:%S.%f").strftime("%H:%M:%S.%f")[:-4]} секунд\n\n""")