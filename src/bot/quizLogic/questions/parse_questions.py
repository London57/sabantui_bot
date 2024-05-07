import xml.etree.ElementTree as ET
from random import shuffle

def get_quetions(result_list = []):
    print(__file__)
    tree = ET.parse('questions.xml')
    root = tree.getroot()
    questions = root.findall('Question')
    for question in questions:
        result_list.append(
            {
                'question': question.find('question').text,
                'bad_answers': [
                    q.text for q in question.findall('bad_answer') 
                ],
                'good_answer': question.find('good_answer').text,
            }
            )
    return result_list


Questions = get_quetions()
shuffle(Questions)