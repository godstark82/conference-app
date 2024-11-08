from dataclasses import dataclass
from typing import Dict, Any
from enum import Enum

class CommitteeRole(Enum):
    ORGANISING_COMMITTEE = 'Organising Committee'
    SCIENTIFIC_LEAD = 'Scientific Lead'
    SCIENTIFIC_COMMITTEE_MEMBER = 'Scientific Committee Member'

    @staticmethod
    def from_json(json: str) -> 'CommitteeRole':
        for role in CommitteeRole:
            if role.value == json:
                return role
        return CommitteeRole.ORGANISING_COMMITTEE  # Default value


@dataclass
class CommitteeMemberModel:
    id: str
    position: str
    designation: str
    image: str
    role: CommitteeRole
    name: str

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'CommitteeMemberModel':
        return CommitteeMemberModel(
            id=json['id'],
            position=json['position'],
            designation=json['designation'],
            image=json['image'],
            role=CommitteeRole.from_json(json['role']),
            name=json['name']
        )