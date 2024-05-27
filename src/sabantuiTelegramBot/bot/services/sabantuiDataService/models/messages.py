from .categories import Categories, Competitions



def send_info(message):
    d = [[i['value'], i['photo']] for i in Categories.categories if i['name'] == message]
    return d[0]

def send_competitions(message):
    d = [[i['value'], i['photo']] for i in Competitions.competitions if i['name'] == message]
    return d[0]
