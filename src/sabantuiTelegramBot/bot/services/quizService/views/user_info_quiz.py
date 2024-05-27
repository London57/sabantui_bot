from .leaders_quiz import format_time_string

def user_quiz_info_response(data):
    print(data)
    place, username, good_answer_count, time = data
    return f"@{username}\nВаше место: {place}\nПравильных ответов: {good_answer_count}\nВремя прохождения: {format_time_string(time)}"