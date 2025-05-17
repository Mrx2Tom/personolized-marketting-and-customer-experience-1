# data_generator.py

import pandas as pd
from faker import Faker
import random
import os

fake = Faker()

CATEGORIES = ["Tech", "Sports", "Fashion", "Health", "Gaming", "Travel"]

def generate_user(n=200):
    data = []
    for _ in range(n):
        data.append({
            "user_id": fake.uuid4(),
            "name": fake.first_name(),
            "email": fake.email(),
            "age": random.randint(18, 70),
            "location": fake.city(),
            "preferred_category": random.choice(CATEGORIES),
            "purchase_count": random.randint(0, 30),
            "avg_spent": round(random.uniform(5.0, 1000.0), 2),
            "last_purchase_days_ago": random.randint(0, 365),
        })
    return pd.DataFrame(data)

def save_to_csv(df, path="data/users.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[✓] Saved {len(df)} users to {path}")

if __name__ == "__main__":
    users = generate_user(200)
    save_to_csv(users)
