from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class FaqQuestionModel:
    question: str
    answer: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'FaqQuestionModel':
        return FaqQuestionModel(
            question=json['question'],
            answer=json['answer']
        )

    @staticmethod
    def from_json_list(json_list: List[Dict[str, Any]]) -> List['FaqQuestionModel']:
        return [FaqQuestionModel.from_json(item) for item in json_list]

@dataclass
class FaqModel:
    id: str
    questions: List[FaqQuestionModel]
    description: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'FaqModel':
        return FaqModel(
            id=json['id'],
            questions=FaqQuestionModel.from_json_list(json['questions']),
            description=json['description']
        )