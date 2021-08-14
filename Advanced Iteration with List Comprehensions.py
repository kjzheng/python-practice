import argparse

parser = argparse.ArgumentParser(description="search for words include partial word")
parser.add_argument("snippet", help="partial or complete string for search for words")

args = parser.parse_args()
snippet = args.snippet.lower()

with open("words") as f:  # use "words" as words file is in same folder as .py script
    words = f.readlines()

matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)

print(matches)
