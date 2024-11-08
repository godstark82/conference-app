from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

from models.card_model import CardModel

@dataclass
class HomeHeroModel:
    image: Optional[str] = field(default='No Image')
    html_content: str = field(default='No Content')

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomeHeroModel':
        return HomeHeroModel(
            image=json.get('image', 'No Image'),
            html_content=json.get('html_content', 'No Content')
        )



@dataclass
class HomePresidentWelcomeModel:
    title: str
    image: Optional[str] = field(default='No Image')
    html_content: str = field(default='No Content')

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomePresidentWelcomeModel':
        return HomePresidentWelcomeModel(
            title=json.get('title', 'No Title'),
            image=json.get('image', 'No Image'),
            html_content=json.get('html_content', 'No Content')
        )



@dataclass
class HomePublicationModel:
    image: Optional[str] = field(default='No Image')
    html_content: str = field(default='No Content')

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomePublicationModel':
        return HomePublicationModel(
            image=json.get('image', 'No Image'),
            html_content=json.get('html_content', 'No Content')
        )



@dataclass
class HomeCongressScopeModel:
    description: str
    title: str
    cards: List['CardModel']

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomeCongressScopeModel':
        return HomeCongressScopeModel(
            description=json.get('description', 'No Description'),
            title=json.get('title', 'No Title'),
            cards=[CardModel.from_json(card) for card in json.get('cards', [])]
        )



@dataclass
class HomeWhyChooseUsModel:
    title: str
    description: str
    cards: List['CardModel']

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomeWhyChooseUsModel':
        return HomeWhyChooseUsModel(
            title=json.get('title', 'No Title'),
            description=json.get('description', 'No Description'),
            cards=[CardModel.from_json(card) for card in json.get('cards', [])]
        )



@dataclass
class HomeCongressStreamModel:
    title: str
    description: str
    cards: List['StreamCardModel']

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomeCongressStreamModel':
        return HomeCongressStreamModel(
            title=json.get('title', 'No Title'),
            description=json.get('description', 'No Description'),
            cards=[StreamCardModel.from_json(card) for card in json.get('cards', [])]
        )

    def to_json(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'description': self.description,
            'cards': [card.to_json() for card in self.cards]
        }

@dataclass
class StreamCardModel:
    title: str
    descriptions: List[str]

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'StreamCardModel':
        return StreamCardModel(
            title=json.get('title', 'No Title'),
            descriptions=json.get('descriptions', [])
        )

    def to_json(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'descriptions': self.descriptions
        }

    def copy_with(self, title: Optional[str] = None, descriptions: Optional[List[str]] = None) -> 'StreamCardModel':
        return StreamCardModel(
            title=title if title is not None else self.title,
            descriptions=descriptions if descriptions is not None else self.descriptions
        )
    

@dataclass
class HomeModel:
    hero: 'HomeHeroModel'
    president_welcome: 'HomePresidentWelcomeModel'
    congress_scope: 'HomeCongressScopeModel'
    congress_stream: 'HomeCongressStreamModel'
    why_choose_us: 'HomeWhyChooseUsModel'
    publication: 'HomePublicationModel'

    @staticmethod
    def from_json(json: Dict[str, Any]) -> 'HomeModel':
        return HomeModel(
            hero=HomeHeroModel.from_json(json['hero']),
            president_welcome=HomePresidentWelcomeModel.from_json(json['presidentWelcome']),
            congress_scope=HomeCongressScopeModel.from_json(json['congressScope']),
            congress_stream=HomeCongressStreamModel.from_json(json['congressStream']),
            why_choose_us=HomeWhyChooseUsModel.from_json(json['whyChooseUs']),
            publication=HomePublicationModel.from_json(json['publication']),
        )