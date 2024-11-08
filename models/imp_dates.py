from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

@dataclass
class DateModel:
    date: datetime
    description: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'DateModel':
        return DateModel(
            date=datetime.fromisoformat(json['date']) if json.get('date') else datetime.now(),
            description=json.get('description', '')
        )