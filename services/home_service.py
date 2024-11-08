import os
import sys
# Add the project root directory to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from db_instance import get_db  # Now we can use direct import
from models import *

from typing import Union


db = get_db()


def get_home_data() -> Union[str, HomeModel]:
   
    response = db.collection('home').get()

    print('response')
    print(response)

    if not response:
        return 'No data found'

    hero_data = next((doc for doc in response if doc.id == 'hero'), None)
    publication_data = next((doc for doc in response if doc.id == 'publication'), None)
    president_welcome_data = next((doc for doc in response if doc.id == 'president-welcome'), None)
    congress_scope_data = next((doc for doc in response if doc.id == 'congress-scope'), None)
    congress_stream_data = next((doc for doc in response if doc.id == 'congress-stream'), None)
    why_choose_us_data = next((doc for doc in response if doc.id == 'why-choose-us'), None)

    if not all([hero_data, publication_data, president_welcome_data, congress_scope_data, congress_stream_data, why_choose_us_data]):
        return 'Some data not found'

    # Convert each document to dict and handle potential None values
    # We can safely use to_dict() here since we checked for None values above
    hero_dict = hero_data.to_dict() if hero_data else {}
    president_dict = president_welcome_data.to_dict() if president_welcome_data else {}
    scope_dict = congress_scope_data.to_dict() if congress_scope_data else {}
    stream_dict = congress_stream_data.to_dict() if congress_stream_data else {}
    publication_dict = publication_data.to_dict() if publication_data else {}
    why_choose_dict = why_choose_us_data.to_dict() if why_choose_us_data else {}

    return HomeModel(
        hero=HomeHeroModel.from_json(hero_dict),
        president_welcome=HomePresidentWelcomeModel.from_json(president_dict),
        congress_scope=HomeCongressScopeModel.from_json(scope_dict),
        congress_stream=HomeCongressStreamModel.from_json(stream_dict),
        publication=HomePublicationModel.from_json(publication_dict),
        why_choose_us=HomeWhyChooseUsModel.from_json(why_choose_dict),
    )
