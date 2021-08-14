import glob
import os
import shutil
import json

try:
    os.mkdir("./receipts/processed")
except OSError:
    print("'processed' directory already exists")

# Get a list of receipts
receipts = glob.glob('new/receipt-[0-9]*.json')  # remove "./"

subtotal = 0.0

for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('\\')[-1]  # change "/" to "\\"
    destination = f"processed/{name}"  # remove "./"
    shutil.move(path, destination)
    print(f"moved '{path}' to '{destination}'")

print("Receipt subtotal: $%.2f" % subtotal)

# Follow the comments on line 12, 20, 21 for changes to the code copied from the cloudguru pdf
# to run the code, make sure gen_receipts.py ran successfully before
# For Windows users
# run it under /receipts