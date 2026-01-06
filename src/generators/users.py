import uuid
import random

def build_users(count):
    roles = ['Engineer', 'Product Manager', 'Designer']
    return [{
        "id": str(uuid.uuid4()),
        "name": f"User_{i}",
        "email": f"user{i}@company.ai",
        "role": random.choice(roles)
    } for i in range(count)]