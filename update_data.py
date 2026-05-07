import pandas as pd
import json
import subprocess
import os

# ===== FILE PATH =====

excel_file = r"C:\Users\hi\Documents\GitHub\NTH\data.xlsx"

json_file = r"C:\Users\hi\Documents\GitHub\NTH\data.json"

repo_path = r"C:\Users\hi\Documents\GitHub\NTH"

print("🔄 Reading Excel...")

# ===== READ EXCEL =====

df = pd.read_excel(
    excel_file,
    usecols=[0, 1],
    dtype=str
)

# đổi tên cột
df.columns = ["code", "value"]

# ===== RESULT =====

result = []

# ===== LOOP =====

for _, row in df.iterrows():

    code = str(row["code"]).strip()

    value = str(row["value"]).strip()

    # ===== LINK =====
    if "http" in value:

        result.append({

            "code": code,

            "name": "",

            "url": value

        })

    # ===== FILE NAME =====
    else:

        result.append({

            "code": code,

            "name": value,

            "url": ""

        })

# ===== EXPORT JSON =====

with open(json_file, "w", encoding="utf-8") as f:

    json.dump(
        result,
        f,
        ensure_ascii=False,
        indent=2
    )

print("✅ data.json updated!")

# ===== GIT AUTO PUSH =====

os.chdir(repo_path)

subprocess.run(["git", "pull"])

subprocess.run(["git", "add", "."])

subprocess.run([
    "git",
    "commit",
    "-m",
    "auto update"
])

subprocess.run(["git", "push"])

print("🚀 GitHub Pages updated!")