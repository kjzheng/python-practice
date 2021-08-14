import os

stage = os.getenv("STAGE", default="abc").upper()

output = f"We're running in {stage}"

if stage.startswith("PROD"):
    output += ' DANGER!!!'

print(output)
