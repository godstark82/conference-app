from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class CardModel:
    image: Optional[str] = None
    title: str = 'No Title'
    description: str = 'No Description'

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'CardModel':
        return CardModel(
            image=json.get('image', 'No Image'),
            title=json.get('title', 'No Title'),
            description=json.get('description', 'No Description')
        )