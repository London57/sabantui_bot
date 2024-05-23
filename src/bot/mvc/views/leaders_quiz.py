from datetime import datetime
def leaders_quiz(data: list):
    """
    Example data:
    # [['saka', 4], ['florian', 3], ['wirz', 3], ['ronaldo', 3], ['messi', 2], ['LukADon4ts', 1]]
    """
    list_of_strings = []
    for index, value in enumerate(data):
        list_of_strings.append(f"""{index + 1}. @{value[0]}\nПравильных ответов: {value[1]}\nВремя прохождения: {format_time_string(datetime.strptime(value[2], "%H:%M:%S.%f"))}\n\n""")

    return ''.join(list_of_strings)

# def convert_time(data):

def format_time_string(current_time):
    time_components = []
    hours, minutes, seconds, microseconds = current_time.hour, current_time.minute, current_time.second, current_time.microsecond
    if hours:
        time_components.append(f"{hours} часов")

    if minutes:
        time_components.append(f"{minutes} минут")


    if microseconds and seconds:
        time_components.append(f"{seconds}.{str(microseconds)[:2]} секунд")
    
    elif seconds:
        time_components.append(f"{seconds} секунд")

    if not time_components:
        return "0 секунд"

    return " ".join(time_components)




# list_of_strings.append(f"""{index + 1}. @{value[0]}\nПравильных ответов: {value[1]}\nВремя прохождения: {datetime.strptime(value[2], "%H:%M:%S.%f").strftime("%H:%M:%S.%f")[:-4]} секунд\n\n""")