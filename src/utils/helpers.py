import random
from datetime import datetime, timedelta

def random_date():
    return datetime.now() - timedelta(days=random.randint(0, 30))