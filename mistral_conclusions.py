import re
from syllo import syllogisms
from collections import defaultdict
import pandas as pd
from mistral import model_conclusions


conclusions = []
i = 0
for prem1, prem2,mood, type_ in syllogisms:

        conclusion = model_conclusions[i]
        if re.search("^.+Some", conclusion) or re.search("^Some", conclusion):
            if re.search(".+not", conclusion):
                conclusion = [mood, conclusion, "O", type_]
            else:
                conclusion = [mood, conclusion, "I", type_]
        elif re.search("^.+All", conclusion) or re.search("^All", conclusion):
            conclusion = [mood, conclusion, "A", type_]
        elif re.search("^.+No", conclusion) or re.search("^No", conclusion):
            conclusion = [mood, conclusion, "E", type_]
        else:
            conclusion = [mood, conclusion, "NVC", type_]

        conclusions.append(conclusion)
        i += 1


conclusion_count = defaultdict(dict)
for syllo_mood, _, conclusion_mood, type_ in conclusions:
  conclusion_count[syllo_mood][conclusion_mood] = conclusion_count[syllo_mood].get(conclusion_mood, 0) + 1


type_count = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
for syllo_mood, _, conclusion_mood, type_ in conclusions:
    type_count[syllo_mood][type_][conclusion_mood] += 1



data = conclusion_count
columns = ["A", "E", "I", "O", "NVC"]


df = pd.DataFrame(index=data.keys(), columns=columns).fillna(0)
for key, inner_dict in data.items():
    for inner_key, count in inner_dict.items():
        df.at[key, inner_key] = count

df.reset_index(inplace=True)
df.rename(columns={"index": "syllogism"}, inplace=True)


excel_file_path = "mistral_syllogism_conclusions.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"DataFrame saved to {excel_file_path}")


flattened_data = []
for mood, types in type_count.items():
    for type_, moods in types.items():
        row = {"syllogism": mood, "type": type_, "A": 0, "E": 0, "I": 0, "O": 0, "NVC": 0}
        for conclusion_mood, count in moods.items():
            row[conclusion_mood] = count
        flattened_data.append(row)

columns = ["syllogism", "type", "A", "E", "I", "O", "NVC"]
df = pd.DataFrame(flattened_data, columns=columns)

excel_file_path = "mistral_syllogism_type_conclusions.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Excel file created at: {excel_file_path}")