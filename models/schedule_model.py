from dataclasses import dataclass
from datetime import datetime
from typing import List, Dict, Any, Optional

@dataclass
class DayDetailModel:
    start_time: Optional[datetime]
    end_time: Optional[datetime] 
    description: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'DayDetailModel':
        if json is None:
            raise ValueError('json cannot be null')

        return DayDetailModel(
            start_time=datetime.fromisoformat(json['startTime']) if json.get('startTime') else None,
            end_time=datetime.fromisoformat(json['endTime']) if json.get('endTime') else None,
            description=json.get('description', '')
        )

@dataclass
class DetailedScheduleModel:
    id: str
    date: datetime
    day_details: List[DayDetailModel]

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'DetailedScheduleModel':
        if json is None:
            raise ValueError('json cannot be null')

        return DetailedScheduleModel(
            id=json['id'],
            date=datetime.fromisoformat(json['date']) if json.get('date') else datetime.now(),
            day_details=[
                DayDetailModel.from_json(e) for e in json.get('dayDetails', [])
            ]
        )