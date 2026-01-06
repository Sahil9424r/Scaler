import uuid

def build_task(project_id, user_id, title):
    return {
        "id": str(uuid.uuid4()),
        "project_id": project_id,
        "assignee": user_id,
        "title": title
    }