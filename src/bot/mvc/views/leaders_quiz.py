


def leaders_quiz(data: list):
    """
    Example data:
    # [['saka', 4], ['florian', 3], ['wirz', 3], ['ronaldo', 3], ['messi', 2], ['LukADon4ts', 1]]
    """
    list_of_strings = []
    for index, value in enumerate(data):
        list_of_strings.append(f"""{index + 1}. @{value[0]}\nПравильных ответов: {value[1]}\nВремя прохождения: {value[2]}\n\n""")
        
    return ''.join(list_of_strings)