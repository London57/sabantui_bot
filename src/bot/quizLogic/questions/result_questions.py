from dataclasses import dataclass
from .parse_questions import get_xml_data

@dataclass
class Question:
    question: str
    bad_answers: list[str]
    good_answer: str


QUESTIONS = [
    Question(**question) for question in get_xml_data()
]