import json
import matplotlib.pyplot as plt
from collections import Counter
import os

json_file_path = 'data/coding_language.json'

if not os.path.exists(json_file_path):
    print(f"Error: The file {json_file_path} does not exist.")
    exit(1)

with open(json_file_path, "r") as file:
    data = json.load(file)

first_lang_counter = Counter([entry["first_language"] for entry in data])
current_lang_counter = Counter([entry["current_language"] for entry in data])

def create_bar_chart(data, title, filename):
    languages = list(data.keys())
    counts = list(data.values())
    
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.bar(languages, counts, color="skyblue")
    plt.title(title)
    plt.xlabel("Language")
    plt.ylabel("Count")
    plt.tight_layout()
    
    print(f"Saving chart: {filename}")
    plt.savefig(filename)
    plt.close()

create_bar_chart(first_lang_counter, "First Language of Contributors", "first_language_chart.png")
create_bar_chart(current_lang_counter, "Current Language of Contributors", "current_language_chart.png")

print("Charts generation completed.")
