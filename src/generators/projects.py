import uuid

def build_projects(team_id):
    return [{
        "id": str(uuid.uuid4()),
        "team_id": team_id,
        "name": "Mobile App Launch",
        "type": "Engineering"
    }]