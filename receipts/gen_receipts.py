import json
import os
import random

count = int(os.getenv("FILE_COUNT") or 100)
words = [word.strip() for word in open("words").readlines()]

for identifier in range(count):
    amount = random.uniform(1.0, 1000)
    content = {
        "topic": random.choice(words),
        "value": "%.2f" % amount
    }
    with open(f"./receipts/new/receipt-{identifier}.json", "w") as f:
        json.dump(content, f)

# run it under /pythonProject
