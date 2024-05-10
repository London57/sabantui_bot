from dataclasses import dataclass
from typing import List


@dataclass
class Question:
    question: str
    bad_answers: List[str]
    good_answer: str

    def __post_init__(self):
        self.attrs = self.question, self.bad_answers, self.good_answer


@dataclass
class QuestionNode(Question):
    prevQuestion: "QuestionNode"
    nextQuestion: "QuestionNode"
    index: int
    state: bool = None
    # правильный или нет

    def __post_init__(self):
        answers = self.bad_answers
        answers.append(self.good_answer)
        self.answers = answers
