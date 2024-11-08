from typing import List
from db_instance import get_db
from models.committee_model import CommitteeMemberModel


db = get_db()

def get_all_committee_members() -> List[CommitteeMemberModel]:
    try:
        # Assuming firestore is already initialized
        snapshot = db.collection('committee').get()
        members = [CommitteeMemberModel(**member.to_dict()) for member in snapshot]
        return members
    except Exception as e:
        print(f"Error: {str(e)}")  # Using print instead of Get.printError
        return  []
    